from gui import *


class Text(List):
    def __init__(self, list_of_paragraphs):
        super().__init__()
        if (list_of_paragraphs):
            self.append(list_of_paragraphs)
        self.counter = 0
        self.item_counter = 0
        try:
            self.current =self[0][self.item_counter]
        except IndexError:
            raise IndexError("Please add a list of sentences when initializing the Text(<list_of_sentences>) class.") from None
            exit()
        self.total_p = len(self)
        self.paragraphs_left = self.total_p - self.counter
        
        
    def next(self):
        self.item_counter += 1
        try:
            self.current = self[0][self.item_counter]
        except IndexError:
            return False
        
        self.total_p = len(self)
        self.paragraphs_left = self.total_p - self.counter
        return True


    def split_sentence(self, p):
        passed_break_point = False
        final_list = List()
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
        for word in words:
            final_list.append(word)
        return all, words


    def switch(self, v1, v2):
        a = v2
        v2 = v1
        v1 = a
        return v1, v2
    
    
    def longer_switch(self, v1, v2):
        if len(v1) < len(v2):
            v1, v2 = self.switch(v1, v2)
            return v1, v2, True
        else:
            return v1, v2, False
    
    
    def calculate_errors(self, p1, p2):
        p1 = p1.split(" ")
        p2 = p2.split(" ")
        starting_errors = abs(len(p1) - len(p2))
        longer, shorter, switched = self.longer_switch(p1, p2)
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
            p1, p2, switched = self.longer_switch(p1, p2)
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
    
    
    def typing_accuracy(self, paragraph, copy, response):
        typed = copy.split(" ")
        response["errors"] = self.calculate_errors(paragraph, copy)
        p1_len = len(paragraph)
        p2_len = len(copy)
        stats = p2_len / p1_len  # defaults to expected situation
        if p2_len > p1_len:
            stats = p1_len / p2_len
        accuracy = stats * 100
        response["accuracy"] = accuracy
        response["typed"] = typed
        return response
    
    
    def get_typing_accuracy(self, paragraph, copy, response):
        original_words_list = self.current.split(" ")
        num_words = len(original_words_list)
        self.typing_accuracy(paragraph, copy, response)
        response["number of words"] = num_words
        response["original"] = original_words_list
        return response
    
    
    def determine_values(self, data, p):
        original_sentence = self.sentence(data, "original")
        typed_sentence = self.sentence(data, "typed")
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
        score = f"{round(data['accuracy'])}%"
        return {
            "original sentence": original_sentence, "typed sentence": typed_sentence, "time in seconds": seconds,
            "original": original, "typed": typed, "errors": total_errors, "accuracy": accuracy, "words per minute": wpm,
            "adjusted words per minute": adjusted_wpm, "overall score": score
        }
        # return [original_sentence, typed_sentence, seconds, original, typed, total_errors, accuracy, wpm, adjusted_wpm,
        #         score]
    
    
    def combine_typed_lines(self, list_of_vars):
        var_list = [var.get() for var in list_of_vars]
        text = " ".join(var_list)
        return text
    
    def get_time(self, start_time, end_time_func, string_var_list, original_sentence):
        end_time = end_time_func()
        duration = end_time - start_time
        response = {}
        response["time"] = duration
        text = self.combine_typed_lines(string_var_list)
        response = self.get_typing_accuracy(original_sentence, text, response)
        return response


    def sentence(self, data_source, location):
        new_sentence = ""
        for word in data_source[location]:
            new_sentence += word
            new_sentence += "     "
        return new_sentence


    def calculate_errors(self, p1, p2):
        p1 = p1.split(" ")
        p2 = p2.split(" ")
        starting_errors = abs(len(p1) - len(p2))
        longer, shorter, switched = self.longer_switch(p1, p2)
        indexes_wrong = []
        for word in range(len(longer)):
            try:
                if longer[word] != shorter[word]:
                    indexes_wrong.append(word)
            except IndexError:
                pass
    
        word_list = List()
        for index in indexes_wrong:
            data = {
                "correct": p1[index],
                "incorrect": p2[index],
            }
            p1, p2, switched = self.longer_switch(p1, p2)
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

    

