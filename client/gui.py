import tkinter as tk
from PIL import Image
import customtkinter as ctk
from client.frame_builder import FrameBuilder
from client.add_to_frame import AddToFrame
from classes.number_counter import NumberCounter
from model.songs_record_db import get_song


class Gui():
    main_color = "#1b1b1b"
    text_color = "#ffffff"

    def __init__(self, frame):
        self.frame = frame

    def search_frame_method(self):
        self.search_frame = FrameBuilder(self.frame)
        self.search_frame.configure(
            width=310, height=50, fg_color=self.main_color)
        self.search_frame.grid(
            row=0, column=0, padx=10, pady=(10, 700), sticky="nsw")

        self.search_entry = ctk.CTkEntry(self.frame)
        self.search_entry.configure(border_color=self.text_color, width=230, bg_color=self.main_color, text_color=self.text_color,
                                    placeholder_text="search", placeholder_text_color=self.text_color, font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.search_entry.grid(row=0, column=0, padx=(
            0, 30), pady=(10, 700))

        search_icon = ctk.CTkImage(dark_image=Image.open("./img/search_icon.png"),
                                   size=(20, 20))

        self.search_button = ctk.CTkButton(self.frame)
        self.search_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color, text="",
                                     image=search_icon, text_color=self.main_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.search_button.grid(row=0, column=0, padx=(
            250, 0), pady=(10, 700))

    def menu_frame_method(self):
        self.menu_frame = FrameBuilder(self.frame)
        self.menu_frame.configure(
            width=310, height=590, fg_color=self.main_color)
        self.menu_frame.grid(
            row=0, column=0, padx=10, pady=(130, 100), sticky="nsw")

        self.my_music_button = ctk.CTkButton(
            self.frame, command=self.my_music_frame)
        self.my_music_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="My Music", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.my_music_button.grid(row=0, column=0, padx=(
            10, 200), pady=(10, 500), sticky="ew")

        self.recently_played_button = ctk.CTkButton(
            self.frame, command=self.recently_played_frame)
        self.recently_played_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                              text="Recently Played", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.recently_played_button.grid(row=0, column=0, padx=(
            10, 160), pady=(10, 430), sticky="ew")

        self.playing_now_button = ctk.CTkButton(
            self.frame, command=self.playing_now_frame)
        self.playing_now_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Playing Now", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.playing_now_button.grid(row=0, column=0, padx=(
            10, 179), pady=(10, 360), sticky="ew")

        self.library_button = ctk.CTkButton(
            self.frame, command=self.library_frame)
        self.library_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                      text="Library", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.library_button.grid(row=0, column=0, padx=(
            10, 215), pady=(10, 290), sticky="ew")

        self.settings_button = ctk.CTkButton(
            self.frame, command=self.settings_frame)
        self.settings_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Settings", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.settings_button.grid(row=0, column=0, padx=(
            10, 215), pady=(550, 10), sticky="ew")

    def my_music_frame(self):
        self.main_frame = FrameBuilder(self.frame)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.my_music_label = ctk.CTkLabel(self.frame)
        self.my_music_label.configure(
            text="My Music", text_color=self.text_color,  font=("Segoe UI", 30, "bold"),  fg_color=self.main_color)
        self.my_music_label.grid(
            row=0, column=3, padx=(10, 807), pady=(10, 745))

        self.songs_button = ctk.CTkButton(
            self.frame, command=self.my_music_songs)
        self.songs_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                    text="Songs", text_color=self.text_color,  font=("Segoe UI", 20, "bold"),  fg_color=self.main_color)
        self.songs_button.grid(row=0, column=3, padx=(
            10, 890), pady=(10, 665))

        self.artist_button = ctk.CTkButton(
            self.frame, command=self.my_music_artist)
        self.artist_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                     text="Artists", text_color=self.text_color,  font=("Segoe UI", 20, "bold"),  fg_color=self.main_color)
        self.artist_button.grid(row=0, column=3, padx=(
            10, 700), pady=(10, 665))

        self.albums_button = ctk.CTkButton(
            self.frame, command=self.my_music_albums)
        self.albums_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                     text="Albums", text_color=self.text_color,  font=("Segoe UI", 20, "bold"),  fg_color=self.main_color)
        self.albums_button.grid(row=0, column=3, padx=(
            10, 500), pady=(10, 665))

        self.divisor = ctk.CTkProgressBar(
            self.frame, progress_color="#878787", width=1010, height=5, bg_color="#878787", fg_color="#878787", border_color="#878787")
        self.divisor.grid(row=0, column=3, padx=(
            0, 10), pady=(10, 620))

        self.my_music_songs()

    def my_music_songs(self):
        self.music_songs_frame = FrameBuilder(self.frame)
        self.music_songs_frame.configure(
            width=1010, height=605, fg_color=self.main_color)
        self.music_songs_frame.grid(row=0, column=3, padx=(0, 10),
                                    pady=(105, 100), sticky="nsew")

        self.random_play_button = ctk.CTkButton(self.frame)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Shuffle all", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 870), pady=(10, 580))

        self.order_by_button = ctk.CTkButton(self.frame)
        self.order_by_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Order by:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 670), pady=(10, 580))

        self.gender_button = ctk.CTkButton(self.frame)
        self.gender_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                     text="Gender:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.gender_button.grid(row=0, column=3, padx=(
            10, 350), pady=(10, 580))

        self.song_name_button = ctk.CTkButton(self.frame)
        self.song_name_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                        text="Song title", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_name_button.grid(row=0, column=3, padx=(
            10, 825), pady=(10, 520))

        self.song_artist_button = ctk.CTkButton(self.frame)
        self.song_artist_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Artist", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_artist_button.grid(row=0, column=3, padx=(
            10, 400), pady=(10, 520))

        self.song_album_button = ctk.CTkButton(self.frame)
        self.song_album_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                         text="Album", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_album_button.grid(row=0, column=3, padx=(
            10, 20), pady=(10, 520))

        self.song_gender_button = ctk.CTkButton(self.frame)
        self.song_gender_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Genre", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_gender_button.grid(row=0, column=3, padx=(
            370, 10), pady=(10, 520))

        self.song_duration_button = ctk.CTkButton(self.frame)
        self.song_duration_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                            text="Duration", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.song_duration_button.grid(row=0, column=3, padx=(
            760, 10), pady=(10, 520))

        self.song_list_frame = ctk.CTkScrollableFrame(
            self.frame, bg_color=self.main_color, border_color=self.main_color, fg_color=self.main_color, border_width=1)
        self.song_list_frame.configure(
            width=980, height=530)
        self.song_list_frame.grid(
            row=0, column=3, padx=(0, 10), pady=(140, 80))

        self.fill = ctk.CTkProgressBar(
            self.frame, progress_color=self.main_color, width=1010, height=2, bg_color=self.main_color, fg_color=self.main_color, border_color=self.main_color)
        self.fill.grid(row=0, column=3, padx=(
            0, 10), pady=(10, 615))
        self.add_songs()

    def my_music_artist(self):
        self.music_artist_frame = FrameBuilder(self.frame)
        self.music_artist_frame.configure(
            width=1010, height=605, fg_color=self.main_color)
        self.music_artist_frame.grid(row=0, column=3, padx=(0, 10),
                                     pady=(105, 100), sticky="nsew")

        self.random_play_button = ctk.CTkButton(self.frame)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Random Play", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 580))

        self.order_by_button = ctk.CTkButton(self.frame)
        self.order_by_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Order By:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 660), pady=(10, 580))

    def my_music_albums(self):
        self.music_albums_frame = FrameBuilder(self.frame)
        self.music_albums_frame.configure(
            width=1010, height=605, fg_color=self.main_color)
        self.music_albums_frame.grid(row=0, column=3, padx=(0, 10),
                                     pady=(105, 100), sticky="nsew")
        self.random_play_button = ctk.CTkButton(self.frame)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Random Play", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 580))

        self.order_by_button = ctk.CTkButton(self.frame)
        self.order_by_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Order By:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 660), pady=(10, 580))

        self.gender_button = ctk.CTkButton(self.frame)
        self.gender_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                     text="Gender:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.gender_button.grid(row=0, column=3, padx=(
            10, 500), pady=(10, 580))

    def recently_played_frame(self):
        self.main_frame = FrameBuilder(self.frame)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.recently_played_label = ctk.CTkLabel(self.frame)
        self.recently_played_label.configure(
            text="Recently played", text_color=self.text_color,  font=("Segoe UI", 30, "bold"),  fg_color=self.main_color)
        self.recently_played_label.grid(
            row=0, column=3, padx=(10, 720), pady=(10, 720))

        self.random_play_button = ctk.CTkButton(self.frame)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="Random play all music", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 780), pady=(10, 650))

        self.recently_played_song_list_frame = tk.Frame(
            self.frame, background=self.main_color)
        self.recently_played_song_list_frame.configure(
            width=600, height=15)
        self.recently_played_song_list_frame.grid(
            row=0, column=3, padx=(0, 128), pady=(10, 250))

    def playing_now_frame(self):
        self.main_frame = FrameBuilder(self.frame)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.playing_now_label = ctk.CTkLabel(self.frame)
        self.playing_now_label.configure(
            text="Playing now", text_color=self.text_color,  font=("Segoe UI", 30, "bold"),  fg_color=self.main_color)
        self.playing_now_label.grid(
            row=0, column=3, padx=(10, 770), pady=(10, 720))

    def library_frame(self):
        self.main_frame = FrameBuilder(self.frame)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.library_label = ctk.CTkLabel(self.frame)
        self.library_label.configure(
            text="Library", text_color=self.text_color,  font=("Segoe UI", 30, "bold"),  fg_color=self.main_color)
        self.library_label.grid(
            row=0, column=3, padx=(10, 845), pady=(10, 720))

        self.random_play_button = ctk.CTkButton(self.frame)
        self.random_play_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text="New Playlist", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 650))

        self.order_by_button = ctk.CTkButton(self.frame)
        self.order_by_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                       text="Order By:", text_color=self.text_color,  font=("Segoe UI", 15, "bold"),  fg_color=self.main_color)
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 640), pady=(10, 650))

    def settings_frame(self):
        self.main_frame = FrameBuilder(self.frame)
        self.main_frame.configure(
            width=1010, height=710, fg_color=self.main_color)
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")

        self.settings_label = ctk.CTkLabel(self.frame)
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
                self.frame, self.song_list_frame, self.main_color, self.text_color)
            add_to_frame.set_values(song.title())
            add_to_frame.set_display(counter.increase_counter())
