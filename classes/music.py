import os
import pygame
from tkinter import filedialog
from classes.format_string import FormatString
from model.directory_db import get_directory, save_directory
from model.queue_db import get_queue_songs_id, get_playing_song_id, get_playing_next_song
from model.playing_back_next_db import add_to_playing_next

current_song = ''
paused = False


class Music():
    pygame.mixer.init()

    def add_directory(self):
        obtain_directory = filedialog.askdirectory()
        save_directory(obtain_directory)

    def load_music_to_play(self, song_name):
        global current_song
        set_format = FormatString()
        song_name = set_format.format(song_name, 4)

        song_full = song_name.lower()
        current_song = song_full

    def play(self):
        global paused, current_song
        if not paused:
            pygame.mixer.music.load(os.path.join(
                get_directory(), current_song))
            pygame.mixer.music.play()

            print(os.path.join(get_directory(), current_song))

        else:
            pygame.mixer.music.unpause()
            paused = False

    def pause_music(self):
        global paused
        pygame.mixer.music.pause()
        paused = True

    def volume(self, value):
        pygame.mixer.music.set_volume(value)

    def mute(self):
        pygame.mixer.music.set_volume(0)

    def unmute(self):
        pygame.mixer.music.set_volume(.5)

    def read_queue(self):
        global current_song
        playing_next_id = []
        playing_next = []

        apply_format = FormatString()
        lista = apply_format.iterate(get_queue_songs_id())
        song_id = apply_format.format(get_playing_song_id(current_song), 3)

        for value in lista:
            if value > song_id:
                playing_next_id.append(value)

        for value2 in playing_next_id:
            song = get_playing_next_song(value2)
            playing_next.append(song)

        playing_next = apply_format.iterate(playing_next)

        for song in playing_next:
            add_to_playing_next(song)

        print(lista)
        print(song_id)
        print(playing_next_id)
        print(playing_next)
