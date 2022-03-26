# @Daniel Ben-Harush
# ID 316152792

def read_line(n, file):
    if type(n) != int or n < 1:
        return "invalid input detected"
    try:
        lines = []
        for line in open(file):
            lines.append(line.strip().split("\n"))
        if n > len(lines):
            return ("line "+ str(n) + " doesn't exist")
        else:
            return str(lines[n-1])

    except:
        return "file not found"


def longest_words(file):
    try:
        words = []
        final_words = []
        for line in open(file):
            line = line.strip().split()
            for word in line:
                word = word.split(".")
                for word_withotpoint in word:
                    word_withotpoint = word_withotpoint.split("-")
                    for final_word in word_withotpoint:
                        final_words.append(final_word)

        sorted_words = sorted(final_words, key=len,reverse= True)
        return sorted_words[:5]
    except:
        print("file not found")
        return []



