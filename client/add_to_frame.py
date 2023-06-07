"""
Create the list of songs and all interface options related to it
"""
import tkinter as tk
import customtkinter as ctk
from client.frame_builder import FrameBuilder
from client.play_bar import PlayBar
from classes.music import Music
from model.artists_db import get_artist_name, asign_artist
from model.album_db import get_album_name, asign_album
from model.songs_record_db import get_artist_id, get_album_id


class AddToFrame(ctk.CTkButton):
    """
    Frame, main_color, text_color
    """
    class SongData(ctk.CTkToplevel):
        """
        Load the song info into a toplevel frame.
        Makes the info editable
        """
        text_color = "#ffffff"
        main_color = "#1b1b1b"

        def __init__(self, song_name, master, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.geometry("654x608")
            self.configure(fg_color="black")
            self.resizable(0, 0)
            self.title('Edit song info')
            self.lift(aboveThis=self)
            self.overrideredirect(False)
            self.song_name = song_name
            self.master = master
            self.grab_set()

            self.frame = FrameBuilder(self)
            self.frame.configure(fg_color=self.main_color,
                                 width=490, height=590)
            self.frame.grid(padx=10, pady=10)

            self.edit_song_info_label = ctk.CTkLabel(self.frame, fg_color=self.main_color,
                                                     text="Edit Song Info", text_color=self.text_color,
                                                     font=("Segoe UI", 20, "bold"))
            self.edit_song_info_label.grid(
                column=0, row=0, padx=(10, 490), pady=(10, 550))

            self.file_location_label = ctk.CTkLabel(self.frame, fg_color=self.main_color,
                                                    text="File location", text_color=self.text_color,
                                                    font=("Segoe UI", 15, "bold"))
            self.file_location = ctk.CTkLabel(self.frame, fg_color=self.main_color,
                                              text="Here goes the file location", text_color=self.text_color,
                                              font=("Segoe UI", 15))

            self.song_title = ctk.CTkLabel(
                self.frame, text="Song title", font=("Segoe UI", 15, "bold"))
            self.song_title_entry = ctk.CTkEntry(
                self.frame, font=("Segoe UI", 15), border_color="black", width=250,
                bg_color=self.main_color, text_color=self.text_color, height=5, border_width=1, fg_color=self.main_color)
            self.song_artist = ctk.CTkLabel(
                self.frame, text="Song artist", font=("Segoe UI", 15, "bold"))
            self.artist_variable = ctk.StringVar()
            self.song_artist_entry = ctk.CTkEntry(
                self.frame, textvariable=self.artist_variable, font=("Segoe UI", 15), border_color="black", width=250,
                bg_color=self.main_color, text_color=self.text_color, height=5, border_width=1, fg_color=self.main_color)
            self.album_title = ctk.CTkLabel(
                self.frame, text="Album title", font=("Segoe UI", 15, "bold"))
            self.album_variable = ctk.StringVar()
            self.album_title_entry = ctk.CTkEntry(
                self.frame, textvariable=self.album_variable, font=("Segoe UI", 15), border_color="black", width=250,
                bg_color=self.main_color, text_color=self.text_color, height=5, border_width=1, fg_color=self.main_color)
            self.album_artist = ctk.CTkLabel(
                self.frame, text="Album artist", font=("Segoe UI", 15, "bold"))
            self.album_artist_entry = ctk.CTkEntry(
                self.frame, font=("Segoe UI", 15), border_color="black", width=250,
                bg_color=self.main_color, text_color=self.text_color, height=5, border_width=1, fg_color=self.main_color)
            self.genre = ctk.CTkLabel(
                self.frame, text="Genre", font=("Segoe UI", 15, "bold"))
            self.genre_entry = ctk.CTkEntry(
                self.frame, font=("Segoe UI", 15), border_color="black", width=250,
                bg_color=self.main_color, text_color=self.text_color, height=5, border_width=1, fg_color=self.main_color)
            self.year = ctk.CTkLabel(
                self.frame, text="Year", font=("Segoe UI", 15, "bold"))
            self.year_entry = ctk.CTkEntry(
                self.frame, font=("Segoe UI", 15), border_color="black", width=250,
                bg_color=self.main_color, text_color=self.text_color, height=5, border_width=1, fg_color=self.main_color)

            self.cancel_button = ctk.CTkButton(self.frame, width=1, bg_color=self.main_color, hover_color=self.main_color,
                                               text="Cancel ", text_color=self.text_color,
                                               font=("Segoe UI", 15, "bold"),  fg_color=self.main_color,
                                               border_color="Black", border_width=1,
                                               command=self.close)

            self.save_button = ctk.CTkButton(self.frame, width=1, bg_color=self.main_color, hover_color=self.main_color,
                                             text=" Save ", text_color=self.text_color,
                                             font=("Segoe UI", 15, "bold"),  fg_color=self.main_color,
                                             border_color="Black", border_width=1,
                                             command=self.save)

            self.song_title_elements()

            self.song_artist_elements()

            self.album_title_elements()

            self.album_artist_elements()

            self.genre_elements()

            self.year_elements()

            self.file_location_elements()

            self.cancel_button_method()

            self.save_button_method()

        def song_title_elements(self):
            """
            Song title label and entry
            """

            self.song_title.grid(
                column=0, row=0, padx=(10, 550), pady=(10, 450))
            self.song_title_entry.grid(
                column=0, row=0, padx=(10, 370), pady=(10, 400))
            self.song_title_entry.insert(0, self.song_name)

        def song_artist_elements(self):
            """
            Song artist label and entry
            """

            self.song_artist.grid(
                column=0, row=0, pady=(10, 450), padx=(200, 10))
            self.song_artist_entry.grid(
                column=0, row=0, padx=(370, 10), pady=(10, 400))
            name = self.song_name + '.mp3'
            if get_artist_id(name.lower()) is False:
                self.song_artist_entry.insert(0, "Unknown")

            else:
                artist_name = get_artist_name(get_artist_id(name.lower()))

                self.song_artist_entry.insert(0, artist_name)

        def album_title_elements(self):
            """
            Album title label and entry
            """

            self.album_title.grid(
                column=0, row=0, padx=(10, 535), pady=(10, 250))
            self.album_title_entry.grid(
                column=0, row=0, padx=(10, 370), pady=(10, 200))
            name = self.song_name + '.mp3'
            if get_album_id(name.lower()) is False or get_album_id(name.lower()) is None or get_album_id(name.lower()) == "" or get_album_id(name.lower()) == "None":
                self.album_title_entry.insert(0, "Unknown")
            else:
                album_name = get_album_name(get_album_id(name.lower()))

                self.album_title_entry.insert(0, album_name)

        def album_artist_elements(self):
            """
            Album artist label and entry
            """

            self.album_artist.grid(
                column=0, row=0, pady=(10, 250), padx=(210, 10))
            self.album_artist_entry.grid(
                column=0, row=0, padx=(370, 10), pady=(10, 200))
            self.album_artist_entry.insert(0, "Album artist here")

        def genre_elements(self):
            """
            Genre label and entry
            """

            self.genre.grid(column=0, row=0, padx=(10, 575), pady=(0, 40))
            self.genre_entry.grid(
                column=0, row=0, padx=(10, 370), pady=(10, 0))
            self.genre_entry.insert(0, "Song genre here")

        def year_elements(self):
            """
            Year label and entry
            """

            self.year.grid(column=0, row=0, pady=(0, 40), padx=(155, 10))
            self.year_entry.grid(
                column=0, row=0, padx=(370, 10), pady=(10, 0))
            self.year_entry.insert(0, "Song year here")

        def file_location_elements(self):
            """
            File location label and entry
            """
            self.file_location_label.grid(
                column=0, row=0, padx=(10, 525), pady=(130, 0))
            self.file_location.grid(
                column=0, row=0, padx=(10, 400), pady=(180, 0))

        def save_button_method(self):
            """
            Save button grid
            """
            self.save_button.grid(
                column=0, row=0, padx=(400, 10), pady=(500, 0))

        def cancel_button_method(self):
            """
            Cancel button grid
            """
            self.cancel_button.grid(
                column=0, row=0, padx=(550, 10), pady=(500, 0))

        def close(self):
            """
            Closes the frame
            """
            self.destroy()

        def save(self):
            """
            Saves the maded changes
            """
            song = self.song_name + '.mp3'
            artist_changes = self.artist_variable.get()
            album_changes = self.album_variable.get()
            if artist_changes == "Unknown":
                pass
            else:
                asign_artist(song, artist_changes)

            if album_changes == "Unknown":
                pass
            else:
                asign_album(song, album_changes)

            self.destroy()
            self.master.update_values()

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

    def set_values(self, song_name, song_gender='Unknown', song_album='Unknown', song_duration='Unknown'):
        """
        Recieve the names for each label.
        With that data can infer the gender, album and artist
        """
        self.song_name = song_name

        self.song_name_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                        text=song_name, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        artist_name = get_artist_name(
            get_artist_id(self.song_name.lower() + '.mp3'))

        if artist_name == 'None':

            self.song_artist_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                              text='Unknown', text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)
        else:
            self.song_artist_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                              text=artist_name, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        self.song_gender_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text=song_gender, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        album_name = get_album_name(
            get_album_id(self.song_name.lower() + '.mp3'))

        if album_name == 'None' or album_name is None or album_name == '':
            self.song_album_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                             text='Unknown', text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)
        else:
            self.song_album_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                             text=album_name, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        self.song_duration_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                            text=song_duration, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

    def update_values(self, song_gender='Unknown', song_album='Unknown', song_duration='Unknown'):
        """
        Update the values on each label
        """
        self.song_name_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                        text=self.song_name, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        artist_name = get_artist_name(
            get_artist_id(self.song_name.lower() + '.mp3'))

        if artist_name == 'None':

            self.song_artist_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                              text='Unknown', text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)
        else:
            self.song_artist_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                              text=artist_name, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        self.song_gender_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                          text=song_gender, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

        album_name = get_album_name(
            get_album_id(self.song_name.lower() + '.mp3'))

        if album_name == 'None' or album_name is None or album_name == '':
            self.song_album_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                             text='Unknown', text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)
        else:
            self.song_album_button.configure(width=1, bg_color=self.main_color, hover_color=self.main_color,
                                             text=album_name, text_color=self.text_color,  font=("Segoe UI", 15),  fg_color=self.main_color)

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

        # Song Name column width
        self.frame.columnconfigure(
            0, weight=5, minsize=280)
        self.frame.columnconfigure(
            1, weight=1, minsize=185)  # Artist column width
        self.frame.columnconfigure(
            2, weight=1, minsize=190)  # Album column width
        self.frame.columnconfigure(
            3, weight=1, minsize=185)  # Genre column width
        self.frame.columnconfigure(
            4, weight=1, minsize=100)  # Duration column width

        self.song_name_button.grid(
            column=0, row=0, padx=padx, pady=(0), sticky="w")
        self.song_artist_button.grid(
            column=1, row=0, padx=(0, 0), pady=(0), sticky="w")
        self.song_album_button.grid(
            column=2, row=0, padx=(0, 0), pady=(0), sticky="w")
        self.song_gender_button.grid(
            column=3, row=0, padx=(0, 0), pady=(0), sticky="w")
        self.song_duration_button.grid(
            column=4, row=0, padx=(0, 0), pady=(0), sticky="w")

        # self.add_spaces()

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
        self.SongData(self.song_name, self)
