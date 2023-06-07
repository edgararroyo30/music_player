"""
Module contain all pygame.mixer interaction needed 
for the app to work properly
"""

import os
from tkinter import filedialog
from pathlib import Path
import pygame
from classes.format_string import FormatString
from model.directory_db import get_directory, save_directory
from model.queue_db import get_queue_songs_id, get_playing_song_id, get_playing_next_song
from model.playing_back_next_db import add_to_playing_next, add_to_playing_back
from model.songs_record_db import save_songs

current_song = ''
paused = False


class Music():
    """
    Class to call all pygame.mixer interactions needed 
    for the app to work properly
    """

    pygame.mixer.init()

    def save_songs(self):
        """
        Upload the songs in the given directory to 
        songs_record table
        """

        path = Path(get_directory())
        songs_list = []

        for p in path.iterdir():
            songs_list.append(p.name)

        save_songs(songs_list, get_directory())

    def add_directory(self):
        """
        Ask the user to select a directory
        Is added to music_directory table
        """
        obtain_directory = filedialog.askdirectory()
        save_directory(obtain_directory)

    def load_music_to_play(self, song_name):
        """
        Load the selected song and set it ready to be played

        Arguments: 
        song_name -> Str
        """

        global current_song
        set_format = FormatString()
        song_name = set_format.format(song_name, 4)

        song_full = song_name.lower()
        current_song = song_full

    def play(self):
        """
        Play the song loaded in the method
        load_music_to_play

        Play the song on its related directory path
        """
        global paused, current_song
        if not paused:
            if current_song == "None" or current_song is None or current_song == "none":
                print("No song")

            else:
                pygame.mixer.music.load(os.path.join(
                    get_directory(), current_song))
                pygame.mixer.music.play()

        else:
            if current_song == "None" or current_song is None or current_song == "none":
                print("No song")

            else:
                pygame.mixer.music.unpause()
                paused = False

    def pause_music(self):
        """
        Just pause the music
        """
        global paused
        pygame.mixer.music.pause()
        paused = True

    def volume(self, value):
        """
        Change the volume by a given parameter

        Argument:
        value -> int
        """
        pygame.mixer.music.set_volume(value)

    def mute(self):
        """
        Set the volume to 0
        """
        pygame.mixer.music.set_volume(0)

    def unmute(self):
        """
        Set the volume to .5
        """
        pygame.mixer.music.set_volume(.5)

    def get_current_song(self):
        """
        Returns the current_song name
        """

        global current_song

        return current_song

    def read_queue(self):
        """
        Read de queue 
        and upload to play_next and play_back tables
        the songs that play next and back to each table
        """

        global current_song
        playing_next_id = []
        playing_next = []

        playing_back_id = []
        playing_back = []

        apply_format = FormatString()
        lista = apply_format.iterate(get_queue_songs_id())
        song_id = apply_format.format(get_playing_song_id(current_song), 3)

        for value in lista:
            if value > song_id:
                playing_next_id.append(value)

        for value in playing_next_id:
            song = get_playing_next_song(value)
            playing_next.append(song)

        for value in lista:
            if value < song_id:
                playing_back_id.append(value)

        for value in playing_back_id:
            song = get_playing_next_song(value)
            playing_back.append(song)

        playing_next = apply_format.iterate(playing_next)
        playing_back = apply_format.iterate(playing_back)

        if playing_next is None:
            add_to_playing_next(None)
            add_to_playing_back(playing_back)

        else:

            add_to_playing_next(playing_next)
            add_to_playing_back(playing_back)

    def play_forward(self):
        """
        Play current song
        """
        global paused, current_song
        if not paused:
            if current_song == "None" or current_song is None or current_song == "none":
                print("No song")
            else:
                pygame.mixer.music.load(os.path.join(
                    get_directory(), current_song))
                pygame.mixer.music.play()

        else:
            if current_song == "None" or current_song is None or current_song == "none":
                print("No song")
            else:
                pygame.mixer.music.unpause()
                pygame.mixer.music.load(os.path.join(
                    get_directory(), current_song))
                pygame.mixer.music.play()
                paused = False

    def play_backward(self):
        """
        Play current song
        """
        global paused, current_song
        if not paused:
            if current_song == "None" or current_song is None or current_song == "none":
                print("No song")
            else:
                pygame.mixer.music.load(os.path.join(
                    get_directory(), current_song))
                pygame.mixer.music.play()

        else:
            if current_song == "None" or current_song is None or current_song == "none":
                print("No song")
            else:
                pygame.mixer.music.unpause()
                pygame.mixer.music.load(os.path.join(
                    get_directory(), current_song))
                pygame.mixer.music.play()
                paused = False

    def give_pause_state(self):
        """
        Returns the actual pause state
        Can be True or False
        """

        global paused
        return paused
