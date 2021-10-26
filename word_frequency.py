STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        lines = text.readlines()
        print(f"{len(lines)} lines in the file.")
        for line in lines:
            line = line.replace(",", "")
            line = line.replace(".", "")
            line = line.replace("-", "")
            line = line.replace("?", "")
            line = line.replace(":", "")
            line = line.replace("’", "")
            line = line.lower()
            for word in STOP_WORDS:
                line = line.split(word, " ")
            print(line)


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


