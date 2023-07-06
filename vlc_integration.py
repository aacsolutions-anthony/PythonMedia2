'''
AAC Solutions
Anthony Grace
VLC media player library
Assuming one channel operation

Changes to original library include:

    Removed the processes and queues dictionaries from VLCPlayer and replaced them with process and queue respectively, as there's only one channel.
    Removed the channel parameter from various methods and adjusted the logic accordingly.
    In ChannelManager, channels dictionary is removed and channel_url is introduced as there's only one channel.
    The _get_channel_url method now retrieves the URL for the single channel and stores it in channel_url.
    Removed the channel parameter from various methods in ChannelManager and adjusted the logic accordingly.
    Renamed get_current_playlists to get_current_playlist because there's only one playlist now.
    Adjusted the instantiation of ChannelManager and VLCPlayer at the end of the script.
'''

import subprocess
import configparser
import shlex
from queue import Queue

class VLCPlayer:
    def __init__(self):
        self.process = None
        self.queue = Queue()

    def play_media(self, media_path, channel_url):
        if self.process is None or self.process.poll() is not None:
            # Split the VLC output string into parts
            part1 = "#transcode{vcodec=h264,acodec=mpga,ab=128,channels=2,samplerate=44100,scodec=none}:rtp{dst="
            part2 = ",port=5004,mux=ts}"
            transcode_options = part1 + channel_url + part2

            # Create the command string
            cmd = f'cvlc {media_path} --sout "{transcode_options}"'

            # Use shlex.split to handle spaces in filenames and arguments correctly
            cmd_list = shlex.split(cmd)

            # Start the new process
            self.process = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        else:
            self.queue.put((media_path, channel_url))

    def clear_queue(self):
        self.queue = Queue()

    def get_queue(self):
        queue_contents = list(self.queue.queue)
        return queue_contents

class ChannelManager:
    def __init__(self, player):
        self.player = player
        self.channel_url = None
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.config = config
        self._get_channel_url()

    def _get_channel_url(self):
        self.channel_url = self.config.get('Channels', 'channel', fallback=None)

    def add_to_queue(self, file_path):
        if not self.channel_url:
            raise ValueError("Channel not found or unavailable")
        self.player.play_media(file_path, self.channel_url)

    def select_channel(self, file_path):
        if not self.channel_url:
            raise ValueError("Channel not found or unavailable")
        self.player.play_media(file_path, self.channel_url)

    def get_current_playlist(self):
        return self.player.get_queue()

vlc_player = VLCPlayer()
channel_manager = ChannelManager(vlc_player)

