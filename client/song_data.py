import customtkinter as ctk
from client.frame_builder import FrameBuilder


class SongData(ctk.CTkToplevel):
    text_color = "#ffffff"
    main_color = "#1b1b1b"

    def __init__(self, song_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("654x608")
        self.configure(fg_color="black")
        self.resizable(0, 0)
        self.title('Edit song info')
        self.lift(aboveThis=self)
        self.overrideredirect(False)
        self.song_name = song_name
        self.grab_set()

        self.frame = FrameBuilder(self)
        self.frame.configure(fg_color=self.main_color,  width=490, height=590)
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
        self.song_artist_entry = ctk.CTkEntry(
            self.frame, font=("Segoe UI", 15), border_color="black", width=250,
            bg_color=self.main_color, text_color=self.text_color, height=5, border_width=1, fg_color=self.main_color)
        self.album_title = ctk.CTkLabel(
            self.frame, text="Album title", font=("Segoe UI", 15, "bold"))
        self.album_title_entry = ctk.CTkEntry(
            self.frame, font=("Segoe UI", 15), border_color="black", width=250,
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
                                         border_color="Black", border_width=1)

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

        self.song_title.grid(column=0, row=0, padx=(10, 550), pady=(10, 450))
        self.song_title_entry.grid(
            column=0, row=0, padx=(10, 370), pady=(10, 400))
        self.song_title_entry.insert(0, self.song_name)

    def song_artist_elements(self):

        self.song_artist.grid(column=0, row=0, pady=(10, 450), padx=(200, 10))
        self.song_artist_entry.grid(
            column=0, row=0, padx=(370, 10), pady=(10, 400))
        self.song_artist_entry.insert(0, "Song artist here")

    def album_title_elements(self):

        self.album_title.grid(column=0, row=0, padx=(10, 535), pady=(10, 250))
        self.album_title_entry.grid(
            column=0, row=0, padx=(10, 370), pady=(10, 200))
        self.album_title_entry.insert(0, "Album title here")

    def album_artist_elements(self):

        self.album_artist.grid(column=0, row=0, pady=(10, 250), padx=(210, 10))
        self.album_artist_entry.grid(
            column=0, row=0, padx=(370, 10), pady=(10, 200))
        self.album_artist_entry.insert(0, "Album artist here")

    def genre_elements(self):

        self.genre.grid(column=0, row=0, padx=(10, 575), pady=(0, 40))
        self.genre_entry.grid(
            column=0, row=0, padx=(10, 370), pady=(10, 0))
        self.genre_entry.insert(0, "Song genre here")

    def year_elements(self):

        self.year.grid(column=0, row=0, pady=(0, 40), padx=(155, 10))
        self.year_entry.grid(
            column=0, row=0, padx=(370, 10), pady=(10, 0))
        self.year_entry.insert(0, "Song year here")

    def file_location_elements(self):
        self.file_location_label.grid(
            column=0, row=0, padx=(10, 525), pady=(130, 0))
        self.file_location.grid(
            column=0, row=0, padx=(10, 400), pady=(180, 0))

    def save_button_method(self):
        self.save_button.grid(column=0, row=0, padx=(400, 10), pady=(500, 0))

    def cancel_button_method(self):
        self.cancel_button.grid(column=0, row=0, padx=(550, 10), pady=(500, 0))

    def close(self):
        self.destroy()
