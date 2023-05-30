"""
vlc_integration.py
VLC Controller 
Using python to control VLC from the Python web app.py program 
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
    Implementing a config.ini file to store the channel URLs
"""
import vlc
import configparser

class VLCPlayer:
    def __init__(self):
        self.instance = vlc.Instance("--no-xlib")
        self.player = self.instance.media_player_new()

    def play_media(self, media_path):
        media = self.instance.media_new(media_path)
        self.player.set_media(media)
        self.player.play()

    def stop_playback(self):
        self.player.stop()

    @staticmethod
    def select_channel(channel):
        # Parse the config file
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Get the channel url
        channel_url = config.get('Channels', channel, fallback=None)
        
        # Check if the channel URL is valid
        if channel_url:
            player = VLCPlayer()  # Create an instance of VLCPlayer
            player.stop_playback()  # Stop any current playback

            # Play the channel by providing the channel URL to the player
            player.play_media(channel_url)
        else:
            # Handle the case when the channel is not found or unavailable
            raise ValueError("Channel not found or unavailable")
