import customtkinter as ctk
from client.gui import Gui


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Music Player')
        self.geometry("1350x810")
        self.resizable(0, 0)
        self.configure(fg_color="Black")
        gui = Gui(self)
        gui.search_frame_method()
        gui.library_frame()
        gui.menu_frame_method()
        gui.my_music_frame()
