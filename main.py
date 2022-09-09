import json
from json import JSONDecodeError
from gui import *
from sentences import Text
from quotes_api import *
from decouple import config
from random import shuffle



# --------------------------------- GLOBALS -------------------------------------

time_to_wait = 100
p1 = "Sally sells seashells by the sea shore."
p2 = "You will face many defeats in life, but never let yourself be defeated."
p_list = [p1, p2]

endpoint = "https://famous-quotes4.p.rapidapi.com/random"
headers = {
	"X-RapidAPI-Key": config("X-RapidAPI-Key"),
	"X-RapidAPI-Host": config("X-RapidAPI-Host")
}


params =  {
    'category': 'all',
    'count': '200'
}


root = Gui("Test Your Typing")
FONT = Font(family="Calibri", size=30)

current_quotes = List()
def get_quotes():
    api = Api(headers, endpoint, params)
    api.call()
    api.save_to_file("quotes", True, True)


def filter_quotes(unfiltered_quotes):
    quote_list = List()
    for quote in unfiltered_quotes:
        quote_list.append(quote["text"])
    return quote_list


def read_quotes_from_file():
    try:
        with open("quotes.json", "r") as file:
            quotes = json.load(file)
        return filter_quotes(quotes)
    except JSONDecodeError:
        get_quotes()


current_quotes = read_quotes_from_file()

if current_quotes.empty() or not current_quotes:
    get_quotes()
    current_quotes = read_quotes_from_file()

shuffle(current_quotes)
text = Text((current_quotes))

# ----------------------------- Functions -----------------------------
def next_handler():
    root.destroy_all_lists()
    can = text.next()
    kwargs = {"bg": "blue"}
    if can:
        root.make_frame(**kwargs)
        root.frame_list.grid()
        start()
    else:
        kwargs = {"bg": "green"}
        root.make_frame(**kwargs)
        root.frame_list.grid()
def create_results_lines(results):
    determined_results = text.determine_values(results, text.current)
    list_of_results = root.make_object_group(object=determined_results)
    print("list of results: ", list_of_results)
    list_of_results.grid()
    begin = root.make_button("Next", cmd=next_handler)
    begin.grid()


def start():
    def play():
        
        def continue_to_results_handler(event):
            response = text.get_time(root.start_time, root.get_end_time, string_var_list, text.current)
            root.destroy_all_lists()
            results_frame = root.make_frame(**{"bg": "red"})
            results_frame.grid(**{})
            create_results_lines(response)
        def show_typing_spaces():
            kwargs = {"row": 2, "padx": (10, 10), "pady": (10, 10)}
            root.type_list.grid(**kwargs)
            
            
        all_words, lines_of_sentences = text.split_sentence(text.current)
        sentence_widgets = root.make_group(this_list=lines_of_sentences, type="display")
        kwargs = {"row": 1, "padx": (10, 10), "pady": (10, 10)}
        sentence_widgets.grid(**kwargs)
        type_list, string_var_list = root.make_group(number=sentence_widgets.num(), type="typer")
        sentence_widgets[-1].after(time_to_wait, show_typing_spaces)
        root.bind_typers(continue_to_results_handler)
    return play()

# frame = None

def start_handler():
    begin.destroy()
    start()
    
    
# TODO: Get The Program to be able to run multiple different strings in a loop or by some other means.
kwargs = {"bg": "green"}
root.make_frame(**kwargs)
root.frame_list.pack()
begin = root.make_button("Begin", cmd=start_handler)
begin.pack()
root.mainloop()

