import subprocess
import configparser
import shlex
from queue import Queue
from threading import Thread
import time


#Removed from update:
'''
class VLCPlayer:
    def __init__(self):
        self.process = None
        self.queue = Queue()
        self.player_thread = Thread(target=self._player_thread)
        self.player_thread.start()

    def _player_thread(self):
        while True:
            if self.process is None or self.process.poll() is not None:
                if not self.queue.empty():
                    media_path, channel_url = self.queue.get()
                    self._start_process(media_path, channel_url)
            time.sleep(1)  # don't busy-wait
'''
class VLCPlayer:

    def __init__(self):

        self.process = None
        self.queue = Queue()
        self.thread_stop = False
        self.player_thread = Thread(target=self._player_thread)
        self.player_thread.daemon = True  # set the thread as a daemon thread
        self.player_thread.start()
        print("VLC_PLAYER DAEMON INITIALIZED \n // \n vlc_integration.py")

    def _player_thread(self):
        while not self.thread_stop:
            if self.process is None or self.process.poll() is not None:
                if not self.queue.empty():
                    media_path, channel_url = self.queue.get()
                    self._start_process(media_path, channel_url)
            time.sleep(1)  # don't busy-wait

    def _start_process(self, media_path, channel_url):
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

    def play_media(self, media_path, channel_url):
        if self.process is None or self.process.poll() is not None:
            self._start_process(media_path, channel_url)
        else:
            self.queue.put((media_path, channel_url))

    def clear_queue(self):
        self.queue = Queue()

    def get_queue(self):
        queue_contents = list(self.queue.queue)
        return queue_contents

    def stop(self):
        self.thread_stop = True
        if self.player_thread.is_alive():
            self.player_thread.join()

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
        self.player.queue.put((file_path, self.channel_url))

    def select_channel(self, file_path):
        if not self.channel_url:
            raise ValueError("Channel not found or unavailable")
        self.player.play_media(file_path, self.channel_url)

    def get_current_playlist(self):
        return self.player.get_queue()

vlc_player = VLCPlayer()
channel_manager = ChannelManager(vlc_player)

