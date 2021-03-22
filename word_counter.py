class WordCounter:
    def __init__(self, words_to_count):
        self.words_to_count = words_to_count

    def count_words(self):
        counted_words = {}
        for word in self.words_to_count:
            word = word.lower()
            counted_words[word] = counted_words.get(word, 0) + 1
        return counted_words
