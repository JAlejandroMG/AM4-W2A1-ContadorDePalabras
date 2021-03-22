from text_processor import Text
from word_counter import WordCounter
from counted_words_sorter import CountedWordsSorter
unwanted_signs = [",", ".", ";", ":", "-", "¿", "?", "¡", "!", "(", ")"]
words_to_ignore = ["con", "de", "el", "en", "in", "la", "las", "le", "me", "mi", "no", "pero", "por", "que", "se", "sin", "su", "un", "una"]
words_most_used = 10

print("\nBienvenido a la aplicación procesadora de Textos.")

text = Text(unwanted_signs)
text.find_file()
words_in_text = text.get_words_in_text()

print("\nPuede escoger una de las siguientes opciones:")
print("(1) Relación de las palabras utilizadas en el texto, así como las veces que aparecen.")
print("(2) Las 10 palabras más utilizadas en el texto, asi como las veces que aparecen.")
option = int(input("Escribe el número de una de las opciones: "))

if option == 1:
    word_counter = WordCounter(words_in_text)
    counted_words = word_counter.count_words()
    print(f"\nLa relación de palabras que aprecen {text.file_name}, con la cantidad de veces que aparece cada una de ellas, es la siguiente:")
    for key, value in counted_words.items():
        if value == 1:
            print(f"{key} aparece {value} vez.")
        else:
            print(f"{key} aparece {value} veces.")
    print("\nMuchas gracias por haber usado esta aplicación, esperamos que vuelva pronto.")

if option == 2:
    word_counter_sorter = CountedWordsSorter(words_in_text, words_to_ignore)
    counted_words = word_counter_sorter.count_words()
    sorted_counted_words = word_counter_sorter.sort_counted_words(counted_words)
    counter = 0
    print(f"\nLas 10 palabras más utilizadas en {text.file_name} son las siguientes:")
    for value, key in sorted_counted_words:
        if counter < words_most_used:
            if value == 1:
                print(f"{key} aparece {value} vez.")
            else:
                print(f"{key} aparece {value} veces.")
            counter += 1
        else:
            continue
    print("\nMuchas gracias por haber usado esta aplicación, esperamos que vuelva pronto.")
