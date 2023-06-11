"""
vlc_integration.py
VLC Controller 
Using python to control CVLC from the Python web app.py program 
██╗   ██╗██╗      ██████╗
██║   ██║██║     ██╔════╝
██║   ██║██║     ██║     
╚██╗ ██╔╝██║     ██║     
 ╚████╔╝ ███████╗╚██████╗
  ╚═══╝  ╚══════╝ ╚═════╝
  2.1 - May 2023

AAC SOLUTIONS
ANTHONY GRACE - WEEK 2 
VERSION 2.1   
Implementing a queue system 
"""
import subprocess
import configparser
import shlex
from queue import Queue

class VLCPlayer:
    def __init__(self):
        self.process = None
        self.queue = Queue()

    def play_media(self, media_path, channel_url):
        # Split the VLC output string into parts
        part1 = "#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:rtp{dst="
        part2 = ",port=5004,mux=ts}"
    
        # Combine the parts, inserting the channel_url in the middle
        transcode_options = part1 + channel_url + part2

        # Create the command string
        cmd = f'cvlc {media_path} --sout "{transcode_options}"'

        # Use shlex.split to handle spaces in filenames and arguments correctly
        cmd_list = shlex.split(cmd)

        # Check if there is an existing process running
        if self.process and self.process.poll() is None:
            # Process is still running, enqueue the media file
            self.queue.put((media_path, channel_url))
        else:
            # Start the new process
            self.process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Check if there are any media files in the queue
            if not self.queue.empty():
                media_path, channel_url = self.queue.get()
                self.play_media(media_path, channel_url)

        return self.process

    def stop_playback(self):
        if self.process:
            # Send SIGTERM to the process
            self.process.terminate()
            output, errors = self.process.communicate()
            self.process = None

    def kill_stream(self):
        if self.process:
            # Send SIGKILL to the process
            self.process.kill()
            output, errors = self.process.communicate()
            self.process = None

    def clear_queue(self):
        self.queue = Queue()
    #NEW
    def get_queue(self):
        queue_contents = list(self.queue.queue)
        return queue_contents

class ChannelManager:
        
    def __init__(self, player):
        self.player = player
        self.channels = {}

    def select_channel(self, channel, file_path):
        # Parse the config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Get the channel url
        channel_url = config.get('Channels', channel, fallback=None)

        # Check if the channel URL is valid
        if channel_url:
            if channel in self.channels:
                self.player.stop_playback()

            self.channels[channel] = self.player.play_media(file_path, channel_url)
            self.channels[channel].wait()  # Wait for the new process to start
        else:
            # Handle the case when the channel is not found or unavailable
            raise ValueError("Channel not found or unavailable")
    #NEW    
    def get_current_playlists(self):
        playlists = {}
        for channel in self.channels:
            playlists[channel] = self.player.get_queue()
        return playlists

vlc_player = VLCPlayer()
channel_manager = ChannelManager(vlc_player)


