from time import time
from gui import *
# """Always incorrect, if there's an index error there's no way that the character at this index matches.
# It will definitely be caused by word2"""
# Wrapping the non missing value with () to show that it wasn't in the typed version.


def switch(v1, v2):
    a = v2
    v2 = v1
    v1 = a
    return v1, v2


def longer_switch(v1, v2):
    if len(v1) < len(v2):
        v1, v2 = switch(v1, v2)
        return v1, v2, True
    else:
        return v1, v2, False


def calculate_errors(p1, p2):
    p1 = p1.split(" ")
    p2 = p2.split(" ")
    starting_errors = abs(len(p1) - len(p2))
    longer, shorter, switched = longer_switch(p1, p2)
    
    indexes_wrong = []
    for word in range(len(longer)):
        try:
            if longer[word] != shorter[word]:
                indexes_wrong.append(word)
        except IndexError:
            pass
    
    word_list = []
    for index in indexes_wrong:
        data = {
            "correct": p1[index],
            "incorrect": p2[index],
        }
        p1, p2, switched = longer_switch(p1, p2)
        try:
            data["errors"] = abs(len(p1[index]) - len(p2[index]))
        except IndexError:
            data["errors"] = abs(len(p1) - len(p2))
        
        for letter in range(len(p1[index])):
            orig = p1[index][letter]
            try:
                bad = p2[index][letter]
                if orig == bad:
                    data[letter] = orig
                else:
                    data["errors"] = data["errors"] + 1
            except IndexError:
                data[letter] = f"({orig})"
        word_list.append(data)
    total_errors = 0
    for word in word_list:
        total_errors += word["errors"]
    return total_errors + starting_errors


def typing_accuracy(paragraph, copy, response):
    typed = copy.split(" ")
    response["errors"] = calculate_errors(paragraph, copy)
    p1_len = len(paragraph)
    p2_len = len(copy)
    
    stats = p2_len / p1_len  # defaults to expected situation
    if p2_len > p1_len:
        stats = p1_len / p2_len
        
    accuracy = stats * 100
    response["accuracy"] = accuracy
    response["typed"] = typed
    return response


def start(paragraph, copy, response):
    words = paragraph.split(" ")
    num_words = len(words)
    typing_accuracy(paragraph, copy, response)
    response["number of words"] = num_words
    response["original"] = words
    return response


def commence(p, p2, response):
    data = start(p, p2, response)
    return data

def sentence(data_source, location):
    new_sentence = ""
    for word in data_source[location]:
        new_sentence += word
        new_sentence += "     "
    return new_sentence


def determine_values(data, p):
    original_sentence = sentence(data, "original")
    typed_sentence = sentence(data, "typed")
    seconds = data["time"]
    original = data["original"]
    typed = data["typed"]
    total_errors = data["errors"]
    accuracy = 100
    if total_errors != 0:
        accuracy = total_errors / len(p)
    wpm = round((len(typed) / seconds) * 60)
    adjusted_wpm = wpm - total_errors
    if total_errors > wpm:
        adjusted_wpm = 0
    # score = f"{round(data['accuracy'])}%"
    print(original_sentence)
    print(typed_sentence)
    print("time", str(data["time"]) + " seconds")
    print("number of errors: ", data["errors"])
    print(original)
    print(typed)
    print("total_errors: ", total_errors)
    print("num characters in sentence: ", len(p))
    print("accuracy: ", accuracy)
    print("wpm: ", wpm)
    print("adjusted_wpm: ", adjusted_wpm)
    
    
    
def fix_sentence(p):
    passed_break_point = False
    new = ""
    for i in range(len(p)):
        char = p[i]
        new += char
        if i == 0:
            pass
        elif i % 40 == 0:
            passed_break_point = True
            if new == " ":
                new += "\n"
        elif passed_break_point and char == " ":
            new += "\n"
            passed_break_point = False
    all = new
    words = new.split("\n")
    return all, words


def create_typing_widgets(number, widget_master, font):
    typed_list = []
    variable_list = []
    for i in range(number):
        variable = StringVar()
        variable_list.append(variable)
        typer = Type(widget_master, font=font, fg="white", bg="black")
        typer.configure(textvariable=variable, justify="left", font=font)
        if i == 0:
            typer.focus()
        typed_list.append(typer)
    return typed_list, variable_list


def format_sentences(words, label_master, font):
    listed = []
    full = ""
    for phrase in words:
        full += phrase
        display_widget = Display(label_master, text=phrase, fg="white")
        display_widget.configure(anchor="nw", justify="left", font=font)
        listed.append(display_widget)
    return full, listed


def list_sentences(original_list):
    list_of_sentences = []
    lists_of_indexes = []
    for item in range(len(original_list)):
        row_index = item + item
        label_widget = original_list[item]
        label_widget.grid(row=row_index, column=0, pady=20)
        list_of_sentences.append(label_widget)
        lists_of_indexes.append(row_index)
    return list_of_sentences, lists_of_indexes
    
    
def continue_to_results(start_time, end_time_func, string_var_list, original_sentence):
    end_time, time_ended = end_time_func()
    duration = end_time - start_time
    response = {}
    response["time"] = duration
    var_list = [var.get() for var in string_var_list]
    text = " ".join(var_list)
    response = commence(original_sentence, text, response)
    return determine_values(response, original_sentence)


