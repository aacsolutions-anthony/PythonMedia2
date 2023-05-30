'''
███████╗██╗      █████╗ ███████╗██╗  ██╗
██╔════╝██║     ██╔══██╗██╔════╝██║ ██╔╝
█████╗  ██║     ███████║███████╗█████╔╝ 
██╔══╝  ██║     ██╔══██║╚════██║██╔═██╗ 
██║     ███████╗██║  ██║███████║██║  ██╗
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
'''
'''
AAC Solutions 
Anthony Grace 
app.py version 32.5.1
Using webflow to manage the front end. 
Using Python to manage form submissions and VLC integration
'''
from flask import Flask, render_template, request, escape #redirect
from werkzeug.utils import secure_filename
import subprocess
import os
import configparser
import vlc_integration  # Assuming vlc_integration.py is in the same directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/index', methods=['GET'])
def index():
    # Render the index page for GET requests
    return render_template('index.html') 

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if 'file-upload' in request.files:
        uploaded_file = request.files['file-upload']
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return render_template('upload.html')

@app.route('/contentmanager', methods=['GET', 'POST'])
def content_manager():
    if request.method == 'POST':
        channel = request.form.get('Channel-Selection') # form field name for channel selection is 'Channel-Selection'
        file = secure_filename(request.form.get('File-Selection')) # form field name for file selection is 'File-Selection'

        # Perform any necessary validation and processing
        if not channel or not file:
            return "Invalid selection. Please select both a channel and a file."

        # Verify the channel
        try:
            config = configparser.ConfigParser()
            config.read('config.ini')
            if not config.has_option('Channels', channel):
                return "Invalid channel. Please select a valid channel."
        except configparser.Error as e:
            return "Error reading configuration file: " + str(e)

        # Call the VLC integration app with the selected channel and file
        file_path = os.path.join('uploads', file) # Assuming 'uploads' directory
        try:
            vlc_integration.VLCPlayer.select_channel(channel)
            subprocess.run(['python3', 'vlc_integration.py', '--file', file_path])
        except Exception as e:
            return "Error initiating streaming: " + str(e)

        # Optionally, you can provide a success message or redirect to another page
        return "Streaming initiated for channel {} with file {}".format(escape(channel), escape(file))

    # Get the list of files in the uploads directory for GET requests
    files = os.listdir('uploads') # Assuming 'uploads' directory
    return render_template('contentmanager.html', files=files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=False)

'''
VULN1: 
Cross-site Scripting (XSS): Unsanitized input from a web form flows into the return value of content...
CWE-20,79,80 - Cross-site scripting: User-controllable input must be sanitized before it's included in output used to dynamically generate a web page. Unsanitized user input can introduce cross-side scripting (XSS) vulnerabilities that can lead to inadvertedly running malicious code in a trusted context.

VULN2: 
Debug mode enabled. 
'''
