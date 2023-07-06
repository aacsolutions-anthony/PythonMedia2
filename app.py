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
app.py version 35
ASSUMING ONE CHANNEL

Changes made to the original Flask app:

    Removed the channel-related logic from the content_manager function since the new version of vlc_integration.py assumes that there's only one channel.
    The channel parameter has been removed from the calls to channel_manager.select_channel(), channel_manager.add_to_queue(), and channel_manager.clear_queue().
    channel_manager.get_current_playlists() has been replaced with channel_manager.get_current_playlist(), and the playlists variable has been replaced with playlist.

'''
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import subprocess
import vlc_integration  # Assuming vlc_integration.py is in the same directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create an instance of VLCPlayer and ChannelManager at the beginning
vlc_player = vlc_integration.VLCPlayer()
channel_manager = vlc_integration.ChannelManager(vlc_player)

@app.route('/', methods=['GET'])
@app.route('/Home.html', methods=['GET'])  # Update the route to match the URL
def index():
    return render_template('Home.html')

@app.route('/Upload.html', methods=['POST', 'GET'])  # Update the route to match the URL
def upload_file():
    if 'file-upload' in request.files:
        uploaded_file = request.files['file-upload']
        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template('Upload.html')

@app.route('/Content-Manager.html', methods=['GET', 'POST'])  # Update the route to match the URL
def content_manager():
    if request.method == 'POST':
        file = request.form.get('File-Selection')
        action = request.form.get('action')

        if not file:
            return jsonify(error="Invalid selection. Please select a file."), 400

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
        if not os.path.isfile(file_path):
            return jsonify(error="File not found: " + file), 404

        if action == 'Play':
            try:
                channel_manager.select_channel(file_path)
            except subprocess.CalledProcessError as e:
                return jsonify(error="Error initiating streaming: " + str(e)), 500
        elif action == 'Add to Queue':
            channel_manager.add_to_queue(file_path)
        elif action == 'Clear Queue':
            channel_manager.clear_queue()

    files = os.listdir(app.config['UPLOAD_FOLDER'])
    playlist = channel_manager.get_current_playlist()
    return render_template('Content-Manager.html', files=files, playlist=playlist)

@app.route('/Contact-Us.html' , methods=['GET'])  # Update the route to match the URL
def contact_us():
    return render_template('Contact-Us.html')


if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=8088, debug=True)
    except KeyboardInterrupt:
        vlc_player.stop()
