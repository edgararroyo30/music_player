"""
Create the list of songs and all interface options related to it
"""

import customtkinter as ctk
from client.frame_builder import FrameBuilder
from client.play_bar import PlayBar
from classes.music import Music
from client.song_data import SongData
import tkinter as tk


class AddToFrame(ctk.CTkButton):
    """
    Frame, main_color, text_color
    """

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

        self.song_menu = tk.Menu(self.frame, tearoff=0)
        self.song_menu.add_command(
            label="Play Song", command=self.get_song_name)
        self.song_menu.add_command(label="Go to Artist")
        self.song_menu.add_command(label="Go to Album")
        self.song_menu.add_command(label="Edit", command=self.load_song_data)
        self.artist_menu = tk.Menu(self.frame, tearoff=0)
        self.artist_menu.add_command(label="Go to Artist")
        self.artist_menu.add_command(label="Edit")
        self.album_menu = tk.Menu(self.frame, tearoff=0)
        self.album_menu.add_command(label="Go to Album")
        self.album_menu.add_command(label="Edit")

        self.play_bar.play_bar()
        self.play_bar.toggle_buttons()
        self.song_artist_button.bind("<Button-3>", self.show_artist_menu)
        self.song_album_button.bind("<Button-3>", self.show_album_menu)
        self.song_name_button.bind("<Button-3>", self.show_song_menu)

    def set_values(self, song_name, song_artist='Unknown', song_gender='Unknown', song_album='Unknown', song_duration='Unknown'):
        """
        Recieve the names for each label.
        With that dta can infer the gender, album and artist
        """
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
        """
        Create the spaces needed for the label to display
        """
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

        self.separator1.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
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
        """
        Set the label into the frame
        """
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
        """
        Retrieve the songname that has been given in the
        set_values method
        """

        music = Music()
        name = self.song_name + '.mp3'
        self.play_bar.get_song_name(self.song_name)

        music.load_music_to_play(name)
        music.play()
        music.read_queue()

    def show_artist_menu(self, event):
        """
        set the coordinates where the menu is being called
        """
        self.artist_menu.post(event.x_root, event.y_root)

    def show_album_menu(self, event):
        """
        set the coordinates where the menu is being called
        """
        self.album_menu.post(event.x_root, event.y_root)

    def show_song_menu(self, event):
        """
        set the coordinates where the menu is being called
        """
        self.song_menu.post(event.x_root, event.y_root)

    def load_song_data(self):
        """
        Gives the song name to the Song Data frame class
        """

        SongData(self.song_name)
