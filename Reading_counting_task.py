#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     25/05/2022
# Copyright:   (c) USER 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def read_file_content(filename):
    filename = 'story.txt'
    with open (filename, 'r') as f_obj:
        show_text = f_obj.read()
        return show_text

text = read_file_content('story.txt')
print(text)

print('\n')

def count_words():
    text = read_file_content("story.txt")
    counts = dict()
    words = text.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

words_num = count_words()
print(words_num)