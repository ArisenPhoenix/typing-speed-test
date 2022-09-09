from gui_pieces import  *
import time


class Gui(Window):
    def __init__(self, title: str, geox: str = "1400", geoy: str = "900", resize_x: bool = True, resize_y: bool = True):
        super().__init__(title, geox, geox, resize_x, resize_y)
        self.frame_master = 0
        self.title = title
        self.geox = geox
        self.geoy = geoy
        self.resize_x = resize_x
        self.resize_y = resize_y
        self.frame_list = List()
        self.type_list = List()
        self.display_list = List()
        self.master_list = List()
        self.button_list = List()
        self.all_lists = List()
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        
    def make_display(self, text, abg: str = MAIN_BACK, bg: str = MAIN_BACK,
                 height: int = 1, width: int = FULL_SCREEN_WIDTH, fg: str = "white"):
        new_display = Display(self, text, abg=abg, bg=bg,
                 height=height, width=width, fg=fg)
        new_display.configure(anchor="w")
        self.display_list.append(new_display)
        self.master_list.append(new_display)
        return new_display
    
        
    def make_typer(self, font, fg: str = MAIN_BACK, bg: str = SECONDARY_BACK, width: int = FULL_SCREEN_WIDTH ):
        new_typer = Type(self, font, fg, bg, width)
        self.type_list.append(new_typer)
        self.master_list.append(new_typer)
        new_typer.font.update(size=40)
        return new_typer

        
    def make_frame(self, **kwargs):
        new_frame = Frame(self, **kwargs)
        self.frame_list.append(new_frame)
        self.master_list.append(new_frame)
        self.frame_master = new_frame
        return new_frame
    
    
    def make_button(self, text, cmd):
        new_button = Press(master=self.frame_master, text=text, cmd=cmd)
        self.button_list.append(new_button)
        self.master_list.append(new_button)
        return new_button
    
    def create_typer_list(self, number):
        variable_list = List()
        print("variable_list: ", variable_list)
        for i in range(number):
            variable = StringVar()
            typer_widget = Type(self.frame_master, variable, fg=SECONDARY_BACK, bg=MAIN_BACK)
            variable_list.append(variable)
            typer_widget.configure( justify="left", width=FULL_SCREEN_WIDTH)
            # if i == 0:
            #     typer_widget.focus()
            self.type_list.append(typer_widget)
            self.master_list.append(typer_widget)
        return self.type_list, variable_list
    
    def create_display_list(self, list_of_individual_phrases):
        for phrase in list_of_individual_phrases:
            display_widget = Display(self.frame_master, text=phrase, fg="white")
            display_widget.configure(anchor="nw", justify="left")
            self.display_list.append(display_widget)
            self.master_list.append(display_widget)
        return self.display_list
        
    def make_group(self, this_list = None, number=None, type=None):
        """ list_of_types = ["frame", "typer",  "display"]"""
        data_type = this_list
        if not this_list:
            data_type = number
        if type == "frame":
            create = self.make_frame
        elif type == "typer":
            return self.create_typer_list(data_type)
        elif type == "display":
            return self.create_display_list(this_list)
        else:
            return TypeError("That is not a valid Gui Type")
        self.loop(cb=create,  this_list=data_type)
        if type == "frame":
            return self.frame_list
        
        
    def make_object_group(self, object):
        keys = object.keys()
        for key in keys:
            text = f"{key}:      {object[key]}"
            display_widget = Display(self.frame_master, text=text, fg="white")
            display_widget.configure(anchor="nw", justify="left")
            self.display_list.append(display_widget)
            self.master_list.append(display_widget)
        return self.display_list
        
    def loop(self,cb, number=None, this_list=None):
        items = this_list
        if number:
            items = number
            for _ in range(items):
                    cb()
        else:
            for item in items:
                cb(item)
                
    def get_start_time(self):
        self.start_time = time.time()
        return self.start_time
        
    def get_end_time(self):
        self.end_time = time.time()
        return self.end_time
        
    def get_total_time(self):
        self.total_time = self.end_time - self.start_time
        return self.total_time
    
    
    def destroy_all_lists(self):
        self.all_lists.append(self.frame_list)
        self.all_lists.append(self.display_list)
        self.all_lists.append(self.type_list )
        self.all_lists.append(self.master_list)
        self.all_lists.append(self.button_list)
        for a_list in self.all_lists:
            for item in a_list:
                item.destroy()
        self.frame_list = List()
        self.type_list = List()
        self.master_list = List()
        self.display_list = List()
        self.button_list = List()
        self.all_lists = List()
        
        # TODO: FIX THIS PUSH ENTER PROBLEM It Likes To Automatically Go To The Last Enter
    def bind_typers(self, continue_to_results_handler):
        print("self.type_list.num(): ", self.type_list.num())
        for item in range(len(self.type_list)):
            typer = self.type_list[item]

            def focus_handler(event):
                event.widget.tk_focusNext().focus()
                return ("break")
                
            if item <self.type_list.num() - 1:
                if item == 0:
                    typer.focus()
                    typer.bind("<Return>", focus_handler)
                else:
                    typer.bind("<Return>", focus_handler)
            else:
                print("item === len(list)", self.type_list.num()-1)
                typer.bind("<Return>", continue_to_results_handler)
                self.get_start_time()
                
            