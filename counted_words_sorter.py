from word_counter import WordCounter

class CountedWordsSorter(WordCounter):
    def __init__(self, words_to_count, words_to_ignore=[]):
        self.words_to_ignore = words_to_ignore
        super().__init__(words_to_count)

    def sort_counted_words(self, counted_words):
        sorted_counted_words = []
        for key, value in counted_words.items():
            if key in self.words_to_ignore or len(key) == 1:
                continue
            else:
                sorted_counted_words.append((value, key))
        sorted_counted_words = sorted(sorted_counted_words, reverse=True)
        return sorted_counted_words
