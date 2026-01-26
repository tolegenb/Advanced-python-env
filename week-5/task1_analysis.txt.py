import string

def analyze_text(input_file, output_file):
    word_freq = {}
    total_lines = 0
    total_words = 0

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1
            line = line.lower().translate(str.maketrans("", "", string.punctuation))
            words = line.split()
            total_words += len(words)

            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(f"Total lines: {total_lines}\n")
        file.write(f"Total words: {total_words}\n")
        file.write("Word frequency:\n")
        for word, count in word_freq.items():
            file.write(f"{word}: {count}\n")


analyze_text("text.txt", "analysis.txt")
