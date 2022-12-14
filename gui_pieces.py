from tkinter import *
from tkinter import font
from lister import List

MAIN_BACK = "black"
SECONDARY_BACK = "white"
TERTIARY_BACK = "red"
FULL_SCREEN_WIDTH = 100
FULL_SCREEN_HEIGHT = 20


class Theme:
    def __init__(self):
        self.BG_Primary = MAIN_BACK
        self.BG_Secondary = SECONDARY_BACK
        self.BG_Tertiary = TERTIARY_BACK
        self.FG_Primary = MAIN_BACK
        self.FG_Secondary = SECONDARY_BACK
        self.FG_Tertiary = TERTIARY_BACK
        self.GEO_X = 1400
        self.GEO_Y = 900
        self.Width = 1400 / 10
        self.Height = 900 / 10
    
    def update(self, bgp: str = None, bgs: str = None, bgt: str = None, fgp: str = None,
               fgs: str = None, fgt: str = None, geox: str = None, geoy: str = None, x: int = None, y: int = None):
        if bgp:
            self.BG_Primary = bgp
        if bgs:
            self.BG_Secondary = bgs
        if bgt:
            self.BG_Tertiary = bgt
        if fgp:
            self.FG_Primary = fgp
        if fgs:
            self.FG_Secondary = fgs
        if fgt:
            self.FG_Tertiary = fgt
        if geox:
            self.GEO_X = geox
        if geoy:
            self.GEO_Y = geoy
        if x:
            self.Width = x
        if y:
            self.Height = y
        

class Font(font.Font):
    def __init__(self, family="Arial", size=20, slant="roman"):
        super().__init__(family=family, size=size, slant=slant)
        self.family = family
        self.size = size
        self.slant = slant
    
    def update(self, family=None, size=None, slant=None):
        if family is None:
            self.family = family
        if size is None:
            self.size = size
        if slant is None:
            self.slant = slant


class Window(Tk):
    def __init__(self, title: str, geox: str = "1400", geoy: str = "900", resize_x: bool = True, resize_y: bool = True):
        super().__init__()
        self.title(title)
        self.current_x = geox
        self.current_y = geoy
        self.geometry(f"{self.current_x}x{self.current_y}")
        self.resizable(resize_x, resize_y)
        self.configure(background=MAIN_BACK, highlightbackground=MAIN_BACK)
    
    def get_dims(self):
        return self.current_x, self.current_y
        
        
class Frame(Frame):
    def __init__(self, master, fg: str = "green", bg: str = "green"):
        x, y = Window.get_dims(master)
        super().__init__(master)
        self.master = master
        self.fg = fg
        self.bg = bg
        self.configure(width=x, height=y, background=bg, highlightbackground=fg,
                       padx=(10), pady=(10))


class Display(Label):
    def __init__(self, master, text, abg: str = MAIN_BACK, bg: str = MAIN_BACK,
                 height: int = 1, width: int = FULL_SCREEN_WIDTH, fg: str = "Black"):
        super().__init__(master)
        self.list = List()
        self.font = Font()
        self.master = master
        self.text = text
        self.abg = abg
        self.bg = bg
        self.height = height
        self.width = width
        self.fg = fg
        self.configure(text=self.text, activebackground=self.abg,
                       background=self.bg, height=self.height, width=self.width, foreground=self.fg, font=self.font)
        
    def create_widget_list(self, list_of_text, master, font):
        for i in range(len(list_of_text)):
            text = list_of_text[i]
            display = Display(master, text=text, fg="white", bg="black", )
            display.configure(anchor="nw", justify="left", font=font)
            self.list.append(display)
    
    def destroy_all(self):
        for list in self.master:
            for item in list:
                item.destroy()
        self.list = []
    
       
class Type(Entry):
    def __init__(self, master, var, fg: str = MAIN_BACK, bg: str = SECONDARY_BACK, width: int = FULL_SCREEN_WIDTH):
        super().__init__(master, textvariable=var)
        self.master = master
        self.font = Font()
        self.var = var
        self.fg = fg
        self.bg = bg
        self.width = width
        self.configuration = self.configure(font=self.font, foreground=self.fg, width=self.width, background=self.bg)
        self.input = ""
    
    def set_save_key(self, key, func=None):
        def save_input(data):
            return self
        if func is None:
            func = save_input
        self.bind(key, func)
        
        
    def create_widget_list(self, number, master, font):
        variable_list = List()
        if not font:
            font = self.font
        for i in range(number):
            variable = StringVar()
            variable_list.append(variable)
            typer = Type(master, font=font, fg="white", bg="black")
            typer.configure(textvariable=variable, justify="left", font=font)
            if i == 0:
                typer.focus()
            self.append(typer)
        return self, variable_list
        
class Press(Button):
    @staticmethod
    def click_me():
        print("make a new function")
        
    def __init__(self, master,  text, bg=SECONDARY_BACK, fg=SECONDARY_BACK, x=5, y=2, cmd=click_me):
        super().__init__(master, text=text, command=cmd)
        self.text = text
        self.bg = bg
        self.fg = fg
        self.width = x
        self.height = y
        self.cmd = cmd
        self.configure(width=self.width, height=self.height)
        
        
    
