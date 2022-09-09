# def switch(v1, v2):
#     a = v2
#     v2 = v1
#     v1 = a
#     return v1, v2
#
#
# def longer_switch(v1, v2):
#     if len(v1) < len(v2):
#         v1, v2 = switch(v1, v2)
#         return v1, v2, True
#     else:
#         return v1, v2, False


# def calculate_errors(p1, p2):
#     p1 = p1.split(" ")
#     p2 = p2.split(" ")
#     starting_errors = abs(len(p1) - len(p2))
#     longer, shorter, switched = longer_switch(p1, p2)
#
#     indexes_wrong = []
#     for word in range(len(longer)):
#         try:
#             if longer[word] != shorter[word]:
#                 indexes_wrong.append(word)
#         except IndexError:
#             pass
#
#     word_list = []
#     for index in indexes_wrong:
#         data = {
#             "correct": p1[index],
#             "incorrect": p2[index],
#         }
#         p1, p2, switched = longer_switch(p1, p2)
#         try:
#             data["errors"] = abs(len(p1[index]) - len(p2[index]))
#         except IndexError:
#             data["errors"] = abs(len(p1) - len(p2))
#
#         for letter in range(len(p1[index])):
#             orig = p1[index][letter]
#             try:
#                 bad = p2[index][letter]
#                 if orig == bad:
#                     data[letter] = orig
#                 else:
#                     data["errors"] = data["errors"] + 1
#             except IndexError:
#                 data[letter] = f"({orig})"
#         word_list.append(data)
#     total_errors = 0
#     for word in word_list:
#         total_errors += word["errors"]
#     return total_errors + starting_errors


# def typing_accuracy(paragraph, copy, response):
#     typed = copy.split(" ")
#     response["errors"] = calculate_errors(paragraph, copy)
#     p1_len = len(paragraph)
#     p2_len = len(copy)
#     stats = p2_len / p1_len  # defaults to expected situation
#     if p2_len > p1_len:
#         stats = p1_len / p2_len
#
#     accuracy = stats * 100
#     response["accuracy"] = accuracy
#     response["typed"] = typed
#     return response


# def start(paragraph, copy, response):
#     words = paragraph.split(" ")
#     num_words = len(words)
#     typing_accuracy(paragraph, copy, response)
#     response["number of words"] = num_words
#     response["original"] = words
#     return response


# def commence(p, p2, response):
#     return start(p, p2, response)
    

# def sentence(data_source, location):
#     new_sentence = ""
#     for word in data_source[location]:
#         new_sentence += word
#         new_sentence += "     "
#     return new_sentence


# def determine_values(data, p):
#     original_sentence = sentence(data, "original")
#     typed_sentence = sentence(data, "typed")
#     seconds = data["time"]
#     original = data["original"]
#     typed = data["typed"]
#     total_errors = data["errors"]
#     accuracy = 100
#     if total_errors != 0:
#         accuracy = total_errors / len(p)
#     wpm = round((len(typed) / seconds) * 60)
#     adjusted_wpm = wpm - total_errors
#     if total_errors > wpm:
#         adjusted_wpm = 0
#     score = f"{round(data['accuracy'])}%"
#     return [original_sentence, typed_sentence, seconds, original, typed, total_errors, accuracy, wpm, adjusted_wpm, score]


