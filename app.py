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
from flask import Flask, render_template, request, jsonify #redirect
from werkzeug.utils import secure_filename
import subprocess
import os
import configparser
import vlc_integration  # Assuming vlc_integration.py is in the same directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create an instance of VLCPlayer and ChannelManager at the beginning
vlc_player = vlc_integration.VLCPlayer()
channel_manager = vlc_integration.ChannelManager(vlc_player)


#INDEXING
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html') 
#INDEXING 

#UPLOADING
@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if 'file-upload' in request.files:
        uploaded_file = request.files['file-upload']
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return render_template('upload.html')

#SERVING3.0

@app.route('/contentmanager', methods=['GET', 'POST'])
def content_manager():

    if request.method == 'POST':
        channel = request.form.get('Channel-Selection')
        file = request.form.get('File-Selection')

        if not channel or not file:
            return jsonify(error="Invalid selection. Please select both a channel and a file."), 400

        config = configparser.ConfigParser()
        try:
            config.read('config.ini')
            if not config.has_option('Channels', channel):
                print(channel)
                return jsonify(error="Invalid channel. Please select a valid channel."), 400
                
        except configparser.Error as e:
            return jsonify(error="Error reading configuration file: " + str(e)), 500

        file_path = os.path.join('uploads', file)
        if not os.path.isfile(file_path):
            return jsonify(error="File not found: " + file), 404

        try:
            channel_manager.select_channel(channel, file_path)
        except subprocess.CalledProcessError as e:
            return jsonify(error="Error initiating streaming: " + str(e)), 500

    files = os.listdir('uploads')
    #NEW
    playlists = channel_manager.get_current_playlists()
    return render_template('contentmanager.html', files=files, playlists=playlists)

'''
    files = os.listdir('uploads')
    return render_template('contentmanager.html', files=files)
'''

# Switch flask.escape module for deployment to prevent depracated and broken features 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug=True)
'''
# Turn off debug mode for production 
# Use production WSGI server for deployment
    #Wrap server in a production WSGI server such as gunicorn
https://gunicorn.org/
'''

'''
At 1100 on 05/06/2023 Snyk and AWS scanning returned ZERO errors or vulnerabilities. 
Version 1.0 of full basic functionality is ready for further deployment testing upon CMND hardware. 

VULN1: 
Cross-site Scripting (XSS): Unsanitized input from a web form flows into the return value of content...
CWE-20,79,80 - Cross-site scripting: User-controllable input must be sanitized before it's included in output used to dynamically generate a web page. Unsanitized user input can introduce cross-side scripting (XSS) vulnerabilities that can lead to inadvertedly running malicious code in a trusted context.

VULN2: 
Debug mode enabled. 
'''
