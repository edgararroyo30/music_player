import time
import math
from threading import Thread
from tkinter import filedialog, ttk
import tkinter as tk
from ttkthemes import ThemedStyle
import os
import pygame
from PIL import Image
import customtkinter as ctk
from model.admin_dao import save_directory, get_directory
from model.admin_dao import create_songs_table, create__directory_table
from model.admin_dao import create_recently_played_table
from model.admin_dao import create_playlist_name_table, create_queue_table, get_song, add_to_queue
from model.admin_dao import get_queue_songs_id, get_playing_song_id, get_playing_next_song
from model.admin_dao import create_playing_next_table, create_playing_back_table
from model.admin_dao import add_to_playing_next, play_next, play_back

current_song = ''
paused = False


class FormatString:

    def iterate(self, argument):
        list = []
        for string in argument:
            string = str(string)
            string = string.strip("[]")
            string = string.strip("()")
            string = string.strip(",")
            string = string.strip("'")

            list.append(string)

        return list

    def iterate_first_value(self, argument):
        list = []
        for value in argument:
            value1, value2 = value
            list.append(value1)
        return list

    def iterate_second_value(self, argument):
        list = []
        for value in argument:
            value1, value2 = value
            list.append(value2)

        return list

    def format(self, string, level):
        string = str(string)
        if level == 1:
            string = string.strip("[]")
        elif level == 2:
            string = string.strip("[]")
            string = string.strip("()")

        elif level == 3:
            string = string.strip("[]")
            string = string.strip("()")
            string = string.strip(",")

        elif level == 4:
            string = string.strip("[]")
            string = string.strip("()")
            string = string.strip(",")
            string = string.strip("'")

        return string


class NumberCounter:
    def __init__(self):
        self.counter = 0

    def increase_counter(self):
        self.counter += 2


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


class FrameBuilder(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class PlayBar():
    def __init__(self, frame):
        self.frame = frame
        self.play_button = ctk.CTkButton(self.frame, command=self.play)
        self.pause_button = ctk.CTkButton(self.frame, command=self.pause)
        self.skip_f_button = ctk.CTkButton(self.frame, command=self.skip_f)
        self.skip_b_button = ctk.CTkButton(self.frame)
        self.mute_button = ctk.CTkButton(self.frame, command=self.mute)
        self.unmute_button = ctk.CTkButton(self.frame, command=self.unmute)
        self.slider = ctk.CTkSlider(
            self.frame, from_=0, to=1, command=self.volume)
        self.progress_bar = ctk.CTkProgressBar(
            self.frame, progress_color='#ffffff', width=250, height=5)
        self.song_name_label = ctk.CTkLabel(self.frame)

    def play_bar(self):
        play_icon = ctk.CTkImage(dark_image=Image.open("./img/play.png"),
                                 size=(25, 25))

        self.play_button.configure(width=1, bg_color="black", image=play_icon,
                                   text="", text_color="black",  font=("Segoe UI", 15, "bold"),  fg_color="black")
        self.play_button.grid(row=0, column=3, padx=(10, 350), pady=(720, 10))

        pause_icon = ctk.CTkImage(dark_image=Image.open("./img/pause.png"),
                                  size=(25, 25))

        self.pause_button.configure(width=1, bg_color="black", image=pause_icon,
                                    text="", text_color="black",  font=("Segoe UI", 15, "bold"),  fg_color="black")

        skip_f_icon = ctk.CTkImage(dark_image=Image.open("./img/fast-forward.png"),
                                   size=(25, 25))

        self.skip_f_button.configure(width=1, bg_color="black",
                                     text="", text_color="black", image=skip_f_icon, font=("Segoe UI", 15, "bold"),  fg_color="black")
        self.skip_f_button.grid(
            row=0, column=3, padx=(10, 260), pady=(720, 10))

        skip_b_icon = ctk.CTkImage(dark_image=Image.open("./img/fast-backward.png"),
                                   size=(25, 25))

        self.skip_b_button.configure(width=1, bg_color="black",
                                     text="", text_color="black", image=skip_b_icon, font=("Segoe UI", 15, "bold"),  fg_color="black")
        self.skip_b_button.grid(
            row=0, column=3, padx=(10, 440), pady=(720, 10))

        speaker_icon = ctk.CTkImage(dark_image=Image.open("./img/speaker.png"),
                                    size=(25, 25))

        self.mute_button.configure(width=1, bg_color="black",
                                   text="", text_color="black", image=speaker_icon, font=("Segoe UI", 15, "bold"),  fg_color="black")
        self.mute_button.grid(
            row=0, column=3, padx=(400, 10), pady=(720, 10))

        muted_icon = ctk.CTkImage(dark_image=Image.open("./img/muted_speaker.png"),
                                  size=(25, 25))

        self.unmute_button.configure(width=1, bg_color="black",
                                     text="", text_color="black", image=muted_icon, font=("Segoe UI", 15, "bold"),  fg_color="black")

        self.slider.configure(button_color="#ffffff")
        self.slider.grid(row=0, column=3, padx=(650, 10), pady=(720, 10))

        self.progress_bar.grid(row=0, column=3, padx=(10, 340), pady=(780, 10))

    def toggle_buttons(self):
        if self.pause_button.winfo_ismapped():

            self.pause_button.grid_remove()
            self.play_button.grid(
                row=0, column=3, padx=(10, 350), pady=(720, 10))

        else:
            self.play_button.grid_remove()
            self.pause_button.grid(
                row=0, column=3, padx=(10, 350), pady=(720, 10))

    def toggle_muted_buttons(self):
        if self.unmute_button.winfo_ismapped():

            self.unmute_button.grid_remove()
            self.mute_button.grid(
                row=0, column=3, padx=(400, 10), pady=(720, 10))

        else:
            self.mute_button.grid_remove()
            self.unmute_button.grid(
                row=0, column=3, padx=(400, 10), pady=(720, 10))

    def pause(self):
        music = Music()
        music.pause_music()
        self.toggle_buttons()

    def mute(self):
        music = Music()
        music.mute()
        self.toggle_muted_buttons()

    def unmute(self):
        music = Music()
        music.unmute()
        self.toggle_muted_buttons()

    def volume(self, value):
        music = Music()
        music.volume(value)

    def play(self):
        music = Music()
        music.play()
        self.toggle_buttons()

    def get_song_name(self, song_name):
        self.song_name_label.configure(text=song_name.title(
        ), text_color="#ffffff",  font=("Segoe UI", 20, "bold"))

        self.song_name_label.grid_remove()
        self.song_name_label.grid(
            row=0, column=0, padx=(10, 10), pady=(720, 10))

    def skip_f(self):
        music = Music()

        new_song = play_next()
        music.load_music_to_play(new_song)
        music.play()

    def skip_b(self):
        music = Music()

        new_song = play_back()
        music.load_music_to_play(new_song)
        music.play()


class App(ctk.CTk):

    main_color = "#1b1b1b"
    text_color = "#ffffff"

    def __init__(self):
        super().__init__()
        self.counter = 0

        self.title("Music Player")
        self.geometry("1350x810")
        self.resizable(0, 0)
        self.configure(fg_color="Black")
        create__directory_table()
        create_songs_table()
        create_recently_played_table()
        create_playlist_name_table()
        create_queue_table()
        create_playing_back_table()
        create_playing_next_table()
        add_to_queue()
        self.search_frame_method()
        self.my_music_frame()
        self.my_music_songs()
        self.menu_frame_method()

    def search_frame_method(self):
        self.search_frame = FrameBuilder(self)
        self.search_frame.configure(
            width=310, height=50, fg_color=self.main_color)
        self.search_frame.grid(
            row=0, column=0, padx=10, pady=(10, 700), sticky="nsw")

        self.search_entry = ctk.CTkEntry(self)
        self.search_entry.configure(border_color=self.text_color, width=230, bg_color=self.main_color, text_color=self.text_color,
                                    placeholder_text="search", placeholder_text_color=self.text_color, font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.search_entry.grid(row=0, column=0, padx=(
            0, 30), pady=(10, 700))

        search_icon = ctk.CTkImage(dark_image=Image.open("./img/search_icon.png"),
                                   size=(20, 20))

        self.search_button = ctk.CTkButton(self)
        self.search_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color, text="",
                                     image=search_icon, text_color=self.main_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.search_button.grid(row=0, column=0, padx=(
            250, 0), pady=(10, 700))

    def menu_frame_method(self):
        self.menu_frame = FrameBuilder(self)
        self.menu_frame.configure(
            width=310, height=590, fg_color=self.main_color)
        self.menu_frame.grid(
            row=0, column=0, padx=10, pady=(130, 100), sticky="nsw")

        self.my_music_button = ctk.CTkButton(self, command=self.my_music_frame)
        self.my_music_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="My Music", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.my_music_button.grid(row=0, column=0, padx=(
            10, 200), pady=(10, 500), sticky="ew")

        self.recently_played_button = ctk.CTkButton(
            self, command=self.recently_played_frame)
        self.recently_played_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                              text="Recently Played", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.recently_played_button.grid(row=0, column=0, padx=(
            10, 160), pady=(10, 430), sticky="ew")

        self.playing_now_button = ctk.CTkButton(
            self, command=self.playing_now_frame)
        self.playing_now_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Playing Now", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.playing_now_button.grid(row=0, column=0, padx=(
            10, 179), pady=(10, 360), sticky="ew")

        self.library_button = ctk.CTkButton(self, command=self.library_frame)
        self.library_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                      text="Library", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.library_button.grid(row=0, column=0, padx=(
            10, 215), pady=(10, 290), sticky="ew")

        self.settings_button = ctk.CTkButton(self, command=self.settings_frame)
        self.settings_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Settings", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.settings_button.grid(row=0, column=0, padx=(
            10, 215), pady=(550, 10), sticky="ew")

    def my_music_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.my_music_label = ctk.CTkLabel(self)
        self.my_music_label.configure(
            text="My Music", text_color=self.text_color,  font=("Segoe UI", 30, "bold"),  fg_color=self.main_color)
        self.my_music_label.grid(
            row=0, column=3, padx=(10, 807), pady=(10, 745))

        self.songs_button = ctk.CTkButton(self, command=self.my_music_songs)
        self.songs_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                    text="Songs", text_color=self.text_color,  font=("Segoe UI", 20, "bold"),  fg_color=self.main_color)
        self.songs_button.grid(row=0, column=3, padx=(
            10, 890), pady=(10, 665))

        self.artist_button = ctk.CTkButton(self, command=self.my_music_artist)
        self.artist_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                     text="Artists", text_color=self.text_color,  font=("Segoe UI", 20, "bold"),  fg_color=self.main_color)
        self.artist_button.grid(row=0, column=3, padx=(
            10, 700), pady=(10, 665))

        self.albums_button = ctk.CTkButton(self, command=self.my_music_albums)
        self.albums_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                     text="Albums", text_color=self.text_color,  font=("Segoe UI", 20, "bold"),  fg_color=self.main_color)
        self.albums_button.grid(row=0, column=3, padx=(
            10, 500), pady=(10, 665))

        self.divisor = ctk.CTkProgressBar(
            self, progress_color="#878787", width=1010, height=5, bg_color="#878787", fg_color="#878787", border_color="#878787")
        self.divisor.grid(row=0, column=3, padx=(
            0, 10), pady=(10, 620))

        self.my_music_songs()

    def my_music_songs(self):
        self.music_songs_frame = FrameBuilder(self)
        self.music_songs_frame.configure(
            width=1010, height=605, fg_color=self.main_color)
        self.music_songs_frame.grid(row=0, column=3, padx=(0, 10),
                                    pady=(105, 100), sticky="nsew")

        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Shuffle all", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 870), pady=(10, 580))

        self.order_by_button = ctk.CTkButton(self)
        self.order_by_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Order by:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 670), pady=(10, 580))

        self.gender_button = ctk.CTkButton(self)
        self.gender_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                     text="Gender:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.gender_button.grid(row=0, column=3, padx=(
            10, 350), pady=(10, 580))

        self.style = ThemedStyle(self)
        self.style.set_theme("equilux")
        self.style.theme_use('equilux')

        self.song_name_button = ctk.CTkButton(self)
        self.song_name_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                        text="Song name", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_name_button.grid(row=0, column=3, padx=(
            10, 815), pady=(10, 520))

        self.song_artist_button = ctk.CTkButton(self)
        self.song_artist_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Artist", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_artist_button.grid(row=0, column=3, padx=(
            10, 400), pady=(10, 520))

        self.song_album_button = ctk.CTkButton(self)
        self.song_album_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                         text="Album", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_album_button.grid(row=0, column=3, padx=(
            10, 20), pady=(10, 520))

        self.song_gender_button = ctk.CTkButton(self)
        self.song_gender_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Gender", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_gender_button.grid(row=0, column=3, padx=(
            380, 10), pady=(10, 520))

        self.song_duration_button = ctk.CTkButton(self)
        self.song_duration_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                            text="Duration", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_duration_button.grid(row=0, column=3, padx=(
            760, 10), pady=(10, 520))

        self.song_list_frame = ctk.CTkScrollableFrame(
            self, bg_color=self.main_color, border_color=self.main_color, fg_color=self.main_color, border_width=1)
        self.song_list_frame.configure(
            width=980, height=530)
        self.song_list_frame.grid(
            row=0, column=3, padx=(0, 10), pady=(140, 80))

        self.fill = ctk.CTkProgressBar(
            self, progress_color=self.main_color, width=1010, height=2, bg_color=self.main_color, fg_color=self.main_color, border_color=self.main_color)
        self.fill.grid(row=0, column=3, padx=(
            0, 10), pady=(10, 615))
        self.add_songs()

    def my_music_artist(self):
        self.music_artist_frame = FrameBuilder(self)
        self.music_artist_frame.configure(
            width=1010, height=605, fg_color=self.main_color)
        self.music_artist_frame.grid(row=0, column=3, padx=(0, 10),
                                     pady=(105, 100), sticky="nsew")

        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Random Play", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 580))

        self.order_by_button = ctk.CTkButton(self)
        self.order_by_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Order By:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 660), pady=(10, 580))

    def my_music_albums(self):
        self.music_albums_frame = FrameBuilder(self)
        self.music_albums_frame.configure(
            width=1010, height=605, fg_color=self.main_color)
        self.music_albums_frame.grid(row=0, column=3, padx=(0, 10),
                                     pady=(105, 100), sticky="nsew")
        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Random Play", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 580))

        self.order_by_button = ctk.CTkButton(self)
        self.order_by_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Order By:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 660), pady=(10, 580))

        self.gender_button = ctk.CTkButton(self)
        self.gender_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                     text="Gender:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.gender_button.grid(row=0, column=3, padx=(
            10, 500), pady=(10, 580))

    def recently_played_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.recently_played_label = ctk.CTkLabel(self)
        self.recently_played_label.configure(
            text="Recently played", text_color=self.text_color,  font=("Segoe UI", 30, "bold"),  fg_color=self.main_color)
        self.recently_played_label.grid(
            row=0, column=3, padx=(10, 720), pady=(10, 720))

        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Random play all music", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 780), pady=(10, 650))

        self.recently_played_song_list_frame = tk.Frame(
            self, background=self.main_color)
        self.recently_played_song_list_frame.configure(
            width=600, height=15)
        self.recently_played_song_list_frame.grid(
            row=0, column=3, padx=(0, 128), pady=(10, 250))

        self.recently_played = ttk.Treeview(
            self.recently_played_song_list_frame, columns=('Song Name', 'Format', 'Artist', 'Gender'))

        self.scroll = ttk.Scrollbar(self,
                                    orient='vertical', command=self.recently_played.yview)
        self.scroll.grid(row=4, column=4, padx=(
            1, 10), pady=(0, 10), sticky='nse')
        self.recently_played.configure(yscrollcommand=self.scroll.set)
        self.recently_played.heading('#0', text='ID')
        self.recently_played.heading('#1', text='Song Name')
        self.recently_played.heading('#2', text='Format')
        self.recently_played.heading('#3', text='Artist')
        self.recently_played.heading('#4', text='Gender')
        self.recently_played.grid(row=0, column=0, sticky='nse', columnspan=10)
        self.recently_played.column("#0", width=0, stretch=False)
        self.recently_played.config(displaycolumns=(
            'Song Name', 'Format', 'Artist', 'Gender'))

    def playing_now_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.playing_now_label = ctk.CTkLabel(self)
        self.playing_now_label.configure(
            text="Playing now", text_color=self.text_color,  font=("Segoe UI", 30, "bold"),  fg_color=self.main_color)
        self.playing_now_label.grid(
            row=0, column=3, padx=(10, 770), pady=(10, 720))

    def library_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.library_label = ctk.CTkLabel(self)
        self.library_label.configure(
            text="Library", text_color=self.text_color,  font=("Segoe UI", 30, "bold"),  fg_color=self.main_color)
        self.library_label.grid(
            row=0, column=3, padx=(10, 845), pady=(10, 720))

        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="New Playlist", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 650))

        self.order_by_button = ctk.CTkButton(self)
        self.order_by_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Order By:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 640), pady=(10, 650))

    def settings_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.settings_label = ctk.CTkLabel(self)
        self.settings_label.configure(
            text="Settings", text_color=self.text_color,  font=("Segoe UI", 30, "bold"),  fg_color=self.main_color)
        self.settings_label.grid(
            row=0, column=3, padx=(10, 820), pady=(10, 720))

    def add_songs(self):
        counter = NumberCounter()

        for song in get_song():
            song = str(song)
            song = song.strip("[]")
            song = song.strip(",")
            song = song.strip("'")
            song = song[:-4]

            add_to_frame = AddToFrame(
                self, self.song_list_frame, self.main_color, self.text_color)
            add_to_frame.set_values(song.title())
            add_to_frame.set_display(counter.increase_counter())


class AddToFrame(ctk.CTkButton):
    def __init__(self, master, frame, main_color, text_color):
        super().__init__(master)
        self.main_frame = frame
        self.frame = FrameBuilder(self.main_frame)
        self.main_color = main_color
        self.text_color = text_color
        self.frame.configure(
            width=50, height=50, fg_color=self.main_color)
        self.song_name_label = ctk.CTkButton(self.frame)
        self.song_artist_label = ctk.CTkButton(self.frame)
        self.song_album_label = ctk.CTkButton(self.frame)
        self.song_gender_label = ctk.CTkButton(self.frame)
        self.song_duration_label = ctk.CTkButton(self.frame)
        self.song_name_button = ctk.CTkButton(
            self.frame,  command=self.get_song_name)
        self.song_artist_button = ctk.CTkButton(self.frame)
        self.song_album_button = ctk.CTkButton(self.frame)
        self.song_gender_button = ctk.CTkButton(self.frame)
        self.song_duration_button = ctk.CTkButton(self.frame)
        self.separator1 = ctk.CTkButton(self.frame)
        self.separator2 = ctk.CTkButton(self.frame)
        self.separator3 = ctk.CTkButton(self.frame)
        self.separator4 = ctk.CTkButton(self.frame)
        self.separator5 = ctk.CTkButton(self.frame)
        self.play_bar = PlayBar(master)
        self.play_bar.play_bar()
        self.play_bar.toggle_buttons()

    def set_values(self, song_name, song_artist='Unknown', song_gender='Unknown', song_album='Unknown', song_duration='Unknown'):
        self.song_name = song_name

        self.song_name_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                        text=song_name, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        self.song_artist_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text=song_artist, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        self.song_gender_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text=song_gender, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        self.song_album_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                         text=song_album, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        self.song_duration_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                            text=song_duration, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

    def add_spaces(self):
        name = self.song_name
        length = len(name.strip())

        if length < 8:
            padx1 = (50, 100)
            padx2 = (50, 50)
            padx3 = (50, 50)
            padx4 = (50, 50)

        elif length > 15:
            padx1 = (30, 25)
            padx2 = (99, 2)
            padx3 = (89, 10)
            padx4 = (40, 60)

        else:
            padx1 = (50, 50)
            padx2 = (50, 50)
            padx3 = (50, 50)
            padx4 = (50, 50)

        self.separator1.configure(width=1, bg_color=self.main_color,
                                  text='', text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)
        self.separator2.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                  text='', text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)
        self.separator3.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                  text='', text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)
        self.separator4.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                  text='', text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)
        self.separator5.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                  text='', text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)
        self.separator1.grid(column=1, row=0, padx=padx1, pady=(0))
        self.separator2.grid(column=3, row=0, padx=padx2, pady=(0))
        self.separator3.grid(column=5, row=0, padx=padx3, pady=(0))
        self.separator4.grid(column=7, row=0, padx=padx4, pady=(0))

    def set_display(self, row):
        name = self.song_name
        length = len(name.strip())

        if length < 8:
            padx = (50, 0)

        else:
            padx = (50, 0)

        self.frame.grid(
            column=0, row=row, padx=(0, 0), pady=(0))

        self.song_name_button.grid(
            column=0, row=0, padx=padx, pady=(0))
        self.song_artist_button.grid(
            column=2, row=0, padx=(0, 0), pady=(0))
        self.song_album_button.grid(
            column=4, row=0, padx=(0, 0), pady=(0))
        self.song_gender_button.grid(
            column=6, row=0, padx=(0, 0), pady=(0))
        self.song_duration_button.grid(
            column=10, row=0, padx=(0, 0), pady=(0))

        self.add_spaces()

    def get_song_name(self):

        music = Music()
        name = self.song_name + '.mp3'
        self.play_bar.get_song_name(self.song_name)

        music.load_music_to_play(name)
        music.play()
        music.read_queue()


app = App()
app.mainloop()
