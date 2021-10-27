# - remove punctuation
# - normalize all words to lowercase
# - remove "stop words" -- words used so frequently they are ignored
# - go through the file word by word and keep a count of how often each word is used

# When your program is complete, you should be able to run 
# ```
# python3 word_frequency.py praise_song_for_the_day.txt
# ``` 
# and get a printed report like this:

# ```
#      we | 7 *******
#    each | 5 *****
#      or | 5 *****
#    need | 5 *****
#    love | 5 *****
#   about | 4 ****
#  praise | 4 ****
#    song | 4 ****
#     day | 3 ***
#     our | 3 ***

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]



def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        text_string = str(text.readlines())
        print(f"{len(text_string)} lines in the file.")
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
        text_string = text_string.lower()
        words_list = text_string.split()
        no_stop_words = []
        for word in words_list:
            if word in STOP_WORDS:
                pass
            else: no_stop_words.append(word)
        no_stop_words = sorted(no_stop_words, key=no_stop_words.count, reverse=True)
        clean_list = {}
        for word in no_stop_words:
            clean_list[word] = no_stop_words.count(word)
        print(clean_list)


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


