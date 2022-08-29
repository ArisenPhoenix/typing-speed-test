from funcs import *
from gui import *
import time

p1 = "Sally sells seashells by the sea shore."
p2 = "You will face many defeats in life, but never let yourself be defeated."
p_list = [p1, p2]
widget_list = []


        
root = Window(title="Hello")
FONT = Font(family="Calibri", size=30)

frame = Frame(root)
frame.configure(width=300)
frame.grid(row=0, column=0, sticky=(N, S, W, E))
frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1, minsize=30)
frame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, minsize=30)
widget_list.append(frame)
timer = None
time_elapsed = 0
s = 0
e = 0
time_ended = False


def destroy_widgets(w_list: list):
    for w in w_list:
        w.destroy()
        

def start_time():
    global s
    s = time.time()


def end_time():
    global time_ended, e
    e = time.time()
    time_ended = True


def create_rows(rows):
    global begin
    begin.destroy()
    listed = []
    for i in range(len(rows) - 1):
        typed_text = rows[i]
        text = Display(frame, text=typed_text, fg="white")
        text.configure(anchor="nw", justify="left", font=FONT)
        text.grid(row=i, column=0)
        listed.append(text)
    return listed


def fix_sentence(sentence):
    new = ""
    for char in range(len(sentence)):
        new += sentence[char]
        if char % 40 == 0:
            new += "\n"
    rows = new
    words = new.split("\n")
    return rows, words, len(words)


def begin_practice():
    full, listed, number = fix_sentence(p)
    rows = create_rows(listed)
    print("num rows: ", len(rows))
    for item in range(len(rows)):
        listed[item].grid(row=len(rows) + 1 + item, column=0, pady=20)
    entry = StringVar()
    
    def continue_to_results(event):
        global e, s
        some = [event]
        del some[0]
        end_time()
        duration = e - s
        response = {"time": duration}
        text = entry.get()
        # entry_list.append(text)
        response = commence(p, text, response)
        determine_values(response)
    
    def display_typer():
        typer.focus()
        typer.grid(row=number + 3, column=0, columnspan=4, sticky="w", pady=20)
        typer.focus()
        start_time()
    
    typer = Type(frame, font=FONT, fg="white", bg="black")
    typer.configure(textvariable=entry, justify="left", font=FONT)
    typer.bind("<Return>", continue_to_results)
    typer.after(3000, display_typer)


begin = Press(frame, text="Begin", cmd=begin_practice)
begin.grid(row=0, column=0)

root.mainloop()
