import time
import math
from threading import Thread
from PIL import Image
import customtkinter as ctk
import pygame


class FrameBuilder(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)






class App(ctk.CTk):
    n=0

    list_of_songs = ["./music/dispara.mp3"]

    def __init__(self):
        super().__init__()

        self.title("Music Player")
        self.geometry("1350x810")
        pygame.mixer.init()
        self.resizable(0, 0)
        self.configure(fg_color="Black")
        self.play_bar()
        self.search_frame_method()
        self.my_music_frame()
        self.my_music_songs()
        self.menu_frame_method()

    def get_song_name(self, song_name):
        stripped_string = song_name[8:-4]
        self.song_name_label = ctk.CTkLabel(self, text=stripped_string.title(), text_color="#ffffff",  font=("Segoe UI", 20, "bold"))
        self.song_name_label.grid(row=0, column=0, padx=(10, 10), pady=(720, 10))
    
    def threading(self):
        t1 = Thread(target=self.progress)
        t1.start()

    def play_music(self):
        self.threading()
        n = self.n
        current_song = n
        if n > 2:
            n = 0
        song_name = self.list_of_songs[n]
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.set_volume(.5)    
        self.get_song_name(song_name)

    def skip_forward(self):
        self.play_music()

    def skip_backwards(self):
        n = self.n
        n -= 2
        self.play_music()

    def volume(self, value):
        pygame.mixer.music.set_volume(value)

    def progress(self):
        a = pygame.mixer.Sound(f"{self.list_of_songs[self.n]}")
        song_len = a.get_length() * 3
        for i in range(0, math.ceil(song_len)):
            time.sleep(.3)
            self.progress_bar.set(pygame.mixer.music.get_pos() / 1000000)

    def play_bar(self):

        play_icon = ctk.CTkImage(dark_image=Image.open("./img/play.png"),
                                  size=(25, 25))
        self.play_button = ctk.CTkButton(self, command=self.play_music)
        self.play_button.configure(width=1, bg_color="black",image= play_icon,
                                       text="", text_color="black",  font=("Segoe UI", 15, "bold"),  fg_color="black")
        self.play_button.grid(row=0, column=3, padx=(10, 350), pady=(720, 10))
        
        skip_f_icon = ctk.CTkImage(dark_image=Image.open("./img/fast-forward.png"),
                                  size=(25, 25))
        self.skip_f_button = ctk.CTkButton(self, command=self.skip_forward)
        self.skip_f_button.configure(width=1, bg_color="black",
                                       text="", text_color="black", image=skip_f_icon, font=("Segoe UI", 15, "bold"),  fg_color="black")
        self.skip_f_button.grid(row=0, column=3, padx=(10, 260), pady=(720, 10))
        
        skip_b_icon = ctk.CTkImage(dark_image=Image.open("./img/fast-backward.png"),
                                  size=(25, 25))
        self.skip_b_button = ctk.CTkButton(self, command=self.skip_backwards)
        self.skip_b_button.configure(width=1, bg_color="black",
                                       text="", text_color="black", image= skip_b_icon, font=("Segoe UI", 15, "bold"),  fg_color="black")
        self.skip_b_button.grid(row=0, column=3, padx=(10, 440), pady=(720, 10))

        speaker_icon = ctk.CTkImage(dark_image=Image.open("./img/speaker.png"),
                                  size=(25, 25))
        self.speaker_button = ctk.CTkButton(self)
        self.speaker_button.configure(width=1, bg_color="black",
                                       text="", text_color="black", image= speaker_icon, font=("Segoe UI", 15, "bold"),  fg_color="black")
        self.speaker_button.grid(row=0, column=3, padx=(400, 10), pady=(720, 10))

        self.slider = ctk.CTkSlider(self, from_= 0, to=1, command=self.volume)
        self.slider.configure()
        self.slider.grid(row=0, column=3, padx=(650, 10), pady=(720, 10))

        self.progress_bar = ctk.CTkProgressBar(self, progress_color='#32a85a', width=250, height=5)
        self.progress_bar.grid(row=0, column=3, padx=(10, 340), pady=(780, 10))


    def search_frame_method(self):
        self.search_frame = FrameBuilder(self)
        self.search_frame.configure(width=310, height=50, fg_color="#1b1b1b")
        self.search_frame.grid(
            row=0, column=0, padx=10, pady=(10, 700), sticky="nsw")
        
        self.search_entry = ctk.CTkEntry(self)
        self.search_entry.configure(border_color="#ffffff", width= 230, bg_color="#1b1b1b", text_color="#ffffff", placeholder_text="search", placeholder_text_color= "#ffffff",font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.search_entry.grid(row=0, column=0, padx=(
            0, 30), pady=(10, 700))

        search_icon = ctk.CTkImage(dark_image=Image.open("./img/search_icon.png"),
                                  size=(20, 20))
        
        self.search_button = ctk.CTkButton(self)
        self.search_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",text="",
                                       image=search_icon, text_color="#1b1b1b",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.search_button.grid(row=0, column=0, padx=(
            250, 0), pady=(10, 700))

    def menu_frame_method(self):
        self.menu_frame = FrameBuilder(self)
        self.menu_frame.configure(
            width=310, height=590, fg_color="#1b1b1b")
        self.menu_frame.grid(
            row=0, column=0, padx=10, pady=(130, 100), sticky="nsw")

        self.my_music_button = ctk.CTkButton(self, command=self.my_music_frame)
        self.my_music_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                       text="My Music", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.my_music_button.grid(row=0, column=0, padx=(
            10, 200), pady=(10, 500), sticky="ew")

        self.recently_played_button = ctk.CTkButton(
            self, command=self.recently_played_frame)
        self.recently_played_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                              text="Recently Played", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.recently_played_button.grid(row=0, column=0, padx=(
            10, 160), pady=(10, 430), sticky="ew")

        self.playing_now_button = ctk.CTkButton(
            self, command=self.playing_now_frame)
        self.playing_now_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                          text="Playing Now", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.playing_now_button.grid(row=0, column=0, padx=(
            10, 179), pady=(10, 360), sticky="ew")

        self.library_button = ctk.CTkButton(self, command=self.library_frame)
        self.library_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                      text="Library", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.library_button.grid(row=0, column=0, padx=(
            10, 215), pady=(10, 290), sticky="ew")

        self.settings_button = ctk.CTkButton(self, command=self.settings_frame)
        self.settings_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                       text="Settings", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.settings_button.grid(row=0, column=0, padx=(
            10, 215), pady=(550, 10), sticky="ew")

    def my_music_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(width=1010, height=710, fg_color="#1b1b1b")
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")
        
        self.my_music_label = ctk.CTkLabel(self)
        self.my_music_label.configure(
                text="My Music", text_color="#ffffff",  font=("Segoe UI", 30, "bold"),  fg_color="#1b1b1b")
        self.my_music_label.grid(
                row=0, column=3, padx=(10, 807), pady=(10, 720))

        
        self.songs_button = ctk.CTkButton(self, command=self.my_music_songs)
        self.songs_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                        text="Songs", text_color="#ffffff",  font=("Segoe UI", 20, "bold"),  fg_color="#1b1b1b")
        self.songs_button.grid(row=0, column=3, padx=(
            10, 890), pady=(10, 650))

        self.artist_button = ctk.CTkButton(self, command=self.my_music_artist)
        self.artist_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                         text="Artists", text_color="#ffffff",  font=("Segoe UI", 20, "bold"),  fg_color="#1b1b1b")
        self.artist_button.grid(row=0, column=3, padx=(
                10, 700), pady=(10, 650))

        self.albums_button = ctk.CTkButton(self, command=self.my_music_albums)
        self.albums_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                         text="Albums", text_color="#ffffff",  font=("Segoe UI", 20, "bold"),  fg_color="#1b1b1b")
        self.albums_button.grid(row=0, column=3, padx=(
                10, 500), pady=(10, 650))
        self.my_music_songs()
        
    def my_music_songs(self):
        self.music_songs_frame = FrameBuilder(self)
        self.music_songs_frame.configure(width=1010, height=605, fg_color="#1b1b1b")
        self.music_songs_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(105, 100), sticky="nsew")
        
        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                          text="Random Play", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 580))
        
        self.order_by_button = ctk.CTkButton(self)
        self.order_by_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                       text="Order By:", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 660), pady=(10, 580))
        
        self.gender_button = ctk.CTkButton(self)
        self.gender_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                       text="Gender:", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.gender_button.grid(row=0, column=3, padx=(
            10, 500), pady=(10, 580))
        
    def my_music_artist(self):
        self.music_artist_frame = FrameBuilder(self)
        self.music_artist_frame.configure(width=1010, height=605, fg_color="#1b1b1b")
        self.music_artist_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(105, 100), sticky="nsew")
        
        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                          text="Random Play", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 580))
        
        self.order_by_button = ctk.CTkButton(self)
        self.order_by_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                       text="Order By:", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 660), pady=(10, 580))
        
    def my_music_albums(self):
        self.music_albums_frame = FrameBuilder(self)
        self.music_albums_frame.configure(width=1010, height=605, fg_color="#1b1b1b")
        self.music_albums_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(105, 100), sticky="nsew")
        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                          text="Random Play", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 580))
        
        self.order_by_button = ctk.CTkButton(self)
        self.order_by_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                       text="Order By:", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 660), pady=(10, 580))
        
        self.gender_button = ctk.CTkButton(self)
        self.gender_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                       text="Gender:", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.gender_button.grid(row=0, column=3, padx=(
            10, 500), pady=(10, 580))

    def recently_played_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(width=1010, height=710, fg_color="#1b1b1b")
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")
        
        self.recently_played_label = ctk.CTkLabel(self)
        self.recently_played_label.configure(
                text="Recently played", text_color="#ffffff",  font=("Segoe UI", 30, "bold"),  fg_color="#1b1b1b")
        self.recently_played_label.grid(
                row=0, column=3, padx=(10, 720), pady=(10, 720))
        
        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                          text="Random play all music", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 780), pady=(10, 650))
        
    def playing_now_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(width=1010, height=710, fg_color="#1b1b1b")
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")
        
        self.playing_now_label = ctk.CTkLabel(self)
        self.playing_now_label.configure(
                text="Playing now", text_color="#ffffff",  font=("Segoe UI", 30, "bold"),  fg_color="#1b1b1b")
        self.playing_now_label.grid(
                row=0, column=3, padx=(10, 770), pady=(10, 720))

    def library_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(width=1010, height=710, fg_color="#1b1b1b")
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")
        
        self.library_label = ctk.CTkLabel(self)
        self.library_label.configure(
                text="Library", text_color="#ffffff",  font=("Segoe UI", 30, "bold"),  fg_color="#1b1b1b")
        self.library_label.grid(
                row=0, column=3, padx=(10, 845), pady=(10, 720))
        
        self.random_play_button = ctk.CTkButton(self)
        self.random_play_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                          text="New Playlist", text_color="#ffffff",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.random_play_button.grid(row=0, column=3, padx=(
            10, 855), pady=(10, 650))
        
        self.order_by_button = ctk.CTkButton(self)
        self.order_by_button.configure(width=1, bg_color="#1b1b1b", hover_color="#1b1b1b",
                                       text="Order By:", text_color="#4b4b4b",  font=("Segoe UI", 15, "bold"),  fg_color="#1b1b1b")
        self.order_by_button.grid(row=0, column=3, padx=(
            10, 640), pady=(10, 650))

    def settings_frame(self):
        self.main_frame = FrameBuilder(self)
        self.main_frame.configure(width=1010, height=710, fg_color="#1b1b1b")
        self.main_frame.grid(row=0, column=3, padx=(0, 10),
                             pady=(10, 100), sticky="nsew")
        
        self.settings_label = ctk.CTkLabel(self)
        self.settings_label.configure(
                text="Settings", text_color="#ffffff",  font=("Segoe UI", 30, "bold"),  fg_color="#1b1b1b")
        self.settings_label.grid(
                row=0, column=3, padx=(10, 820), pady=(10, 720))


app = App()
app.mainloop()
