def get_mistakes(p1, p2):
    p1 = p1.split(" ")
    p2 = p2.split(" ")
    matching_letters = []
    incorrect_letters = []
    matching_words = []
    incorrect_words = []
    words_typed = []
    
    for i in range(len(p1) - 1):
        or_word = p1[i]
        try:
            typed_word = p2[i]
            if or_word == typed_word:
                matching_words.append(or_word)
                words_typed.append(typed_word)
            else:
                incorrect_words.append(typed_word)
                words_typed.append(typed_word)
        
        except IndexError:
            incorrect_words.append(f"'{or_word}'")
        
        for word in range(len(p1[i])):
            p1_word = p1[i][word]
            try:
                p2_word = p2[i][word]
                if p1_word == p2_word:
                    matching_letters.append(p1_word)
                else:
                    incorrect_letters.append(p2_word)
            except IndexError:
                incorrect_letters.append(f"'{p1_word}'")
    response = {
        "matching_words": matching_words,
        "incorrect_words": incorrect_words,
        "matching_letters": matching_letters,
        "incorrect_letters": incorrect_letters,
        "typed words": words_typed
    }
    return response


def num_mistakes(p1, p2):
    """Determines which word is longer and then determines certain stats based on the differences"""
    p1, p2, word_switched = longer_switch(p1, p2)
    p1 = p1.split(" ")
    p2 = p2.split(" ")
    
    correct_letters = []
    correct_words = []
    incorrect_letters = []
    incorrect_words = []
    typed_words = []
    
    for w in range(len(p1)):
        word1 = p1[w]
        word2 = ""
        incorrect_letters.append(word1 + " ---")
        try:
            word2 = p2[w]
            incorrect_letters[w] = (incorrect_letters[w], word2)
            if word1 == word2:
                correct_words.append(word2)
            else:
                if word_switched:
                    incorrect_words.append(word1)
                else:
                    incorrect_words.append(word2)
        
        except IndexError:
            
            incorrect_words.append(f"({word1})")
        finally:
            if word_switched:
                typed_words.append(word1)
            else:
                typed_words.append(word2)
        if word_switched:
            word1, word2 = switch(word1, word2)
        word1, word2, letter_switched = longer_switch(word1, word2)
        for let in range(len(word1)):
            # word1 is always going to be the longer one, so it won't cause an index error
            letter1 = word1[let]
            letter2 = ""
            try:
                letter2 = word2[let]
                if letter1 == letter2:
                    correct_letters.append(letter1)
                else:
                    if letter_switched:
                        # print("incorrect letter was: ", letter1)
                        incorrect_letters.append(letter1)
                    else:
                        # print("incorrect letter was: ", letter2)
                        incorrect_letters.append(letter2)
            
            except IndexError:
                # Always typing error due to not enough characters or too many being typed
                # print("Not enough letters in one string, defaulting to error from: ", letter1)
                if letter_switched:
                    incorrect_letters.append(f"{(letter1, letter2)}")
                else:
                    incorrect_letters.append(f"({(letter1, letter2)})")
    
    response = {
        "correct_words": correct_words,
        "incorrect_words": incorrect_words,
        "correct_letters": correct_letters,
        "incorrect_letters": incorrect_letters,
        "typed words": typed_words
    }
    
    return response



def start_timer():
    global REPS
    REPS += 1
    display_to_do(REPS)
    print(REPS)
    work_min = 2#WORK_MIN * 60
    short_break_min = 2#SHORT_BREAK_MIN * 60
    long_break_min = 2#LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        countdown(long_break_min)
    elif REPS % 2 == 0:
        countdown(short_break_min)
    else:
        countdown(work_min)