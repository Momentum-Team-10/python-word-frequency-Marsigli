

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # with open(file, 'r') as text the r as the second arguement means that my intentions are to read the file
    with open(file, 'r') as text:
        # this reads the entire file and puts this into text string
        text_string = text.read()
        # returns the string respresentation of text string without removing special characters so you can see what you need to remove
        # print(repr(text_string))
        # this removes the specified characters from the text string
        text_string = text_string.replace(",", "")
        text_string = text_string.replace(".", "")
        text_string = text_string.replace("—", " ")
        text_string = text_string.replace("-", " ")
        text_string = text_string.replace("?", "")
        text_string = text_string.replace(":", "")
        text_string = text_string.replace("'", "")
        text_string = text_string.replace("\\n", "")
        text_string = text_string.replace("’", "")
        text_string = text_string.replace("]", "")
        text_string = text_string.replace("[", "")
        text_string = text_string.replace("\"", "")
        # takes the text string and makes all the characters lower case
        text_string = text_string.lower()
        # takes the text string and splits all the words into a list this splits from space to space
        words_list = text_string.split()
        # a dictionary is a key and a value
        no_stop_words = {}
        # for loop that will cycle through the words list
        for word in words_list:
            # checking to see if the word is stop words
            if word not in STOP_WORDS:
                # if the word is already in the dictionary no stop words increment the value by 1
                if word in no_stop_words:
                    no_stop_words[word] += 1
                # if the word is not in the dictionary no stop words add this to the dictionary and give it a value of 1
                else:
                    no_stop_words[word] = 1
            
            sorted_dict = {}
            sorted_keys = sorted(no_stop_words, key=no_stop_words.get, reverse=True)
            
        for w in sorted_keys:
            sorted_dict[w] = no_stop_words[w]
                
        for key in sorted_dict:
            print(f"{key:>15} | {sorted_dict[key]:2} {'*' * sorted_dict[key]}")
            
        # good practice to ensure that we are properly closing the file in use at the end of the function
        text.close()
        


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


