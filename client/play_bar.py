import customtkinter as ctk
from PIL import Image
from classes.music import Music
from model.playing_back_next_db import play_back, play_next


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
