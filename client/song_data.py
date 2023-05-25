import customtkinter as ctk


class SongData(ctk.CTkToplevel):
    def __init__(self, song_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.title('Edit song info')

        self.label = ctk.CTkLabel(self, text=song_name)
        self.label.grid(column=2, row=0)
