from funcs import *
from gui import *
import time
entry_list = []

# ---------------------- GUI ----------------------------
root = Window(title="Hello")
FONT = Font(family="Calibri", size=30)
frame = Frame(root)
frame.configure(width=300)
frame.grid(row=0, column=0, sticky=(N, S, W, E))
frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1, minsize=30)
frame.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, minsize=30)

# --------------------------------- GLOBALS -------------------------------------
s = 0
e = 0
time_ended = False

def start_time():
    global s
    s = time.time()
    time_ended = False
    return s, time_ended


def end_time():
    global time_ended, e
    e = time.time()
    time_ended = True
    return e, time_ended


p1 = "Sally sells seashells by the sea shore."
p2 = "You will face many defeats in life, but never let yourself be defeated."
p_list = [p1, p2]
# ----------------------------- Functions -----------------------------

def start():
    global p_list, frame, begin, FONT
    for p in range(len(p_list)):
        practice = p_list[p]
        def begin_practice(widget_master, starting_button, original_sentence, font):
            def display_lines_handler():
                display_lines(typed_list)
                
            def continue_to_results_handler(event):
                global s
                continue_to_results(s, end_time, string_var_list, original_sentence)
        
            def display_lines(list_of_lines):
                for item in range(len(list_of_lines)):
                    index = widget_indexes[item] + 1
                    def focus_next_handler(bla):
                        def focus_next():
                            typed_list[item].focus()
                        focus_next()
                    typer = list_of_lines[item]
                    if item != len(list_of_lines) - 1:
                        typer.bind("<Return>", focus_next_handler)
                        typer.grid(row=index, column=0, columnspan=4, sticky="w", pady=(20))
                    else:
                        typer.bind("<Return>", continue_to_results_handler)
                        start_time()
                        typer.grid(row=index, column=0, columnspan=4, sticky="w", pady=(20))
        
            all_words, list_of_words = fix_sentence(practice)
            full, original_sentence_list = format_sentences(list_of_words, widget_master, font)
            starting_button.destroy()
            number = len(original_sentence_list)
            typed_list, string_var_list = create_typing_widgets(number, widget_master, font)
            sentence_widgets, widget_indexes = list_sentences(original_sentence_list)
            sentence_widgets[-1].after(3000, display_lines_handler)
            
        begin_practice(frame, begin, practice, FONT)
begin = Press(frame, text="Begin", cmd=start)
begin.grid(row=0, column=0)

root.mainloop()
print(entry_list)
