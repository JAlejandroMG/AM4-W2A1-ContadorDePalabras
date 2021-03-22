class Text:
    def __init__(self, unwanted_signs):
        self.unwanted_signs = unwanted_signs
        self.file_name = ''
        self.file_content = ''

    def find_file(self):
        is_found = False
        while not is_found:
            self.file_name = input("\nProporcine el nombre del archivo que quiere procesar: ")
            try:
                self.file_name = self.file_name.lower() + ".txt"
                self.file_content = open(f'files/{self.file_name}')
                is_found = True
            except FileNotFoundError:
                print(f"\nLo sentimos, no encontramos el archivo {self.file_name}")
                self.file_content = ""
                another_try = input("¿Gusta volver a proporcionar el nombre del archivo?  S=si / N=no: ")
                another_try = another_try.lower()
                if another_try == "s":
                    continue
                else:
                    print("\nMuchas gracias por haber usado esta aplicación, esperamos que vuelva pronto.")
                    exit()
        print(f'El archivo {self.file_name} fue encontrado.')

    def get_words_in_text(self):
        words_in_text = []
        for line in self.file_content:
            line = line.strip()
            empty_line = ''
            line = empty_line.join([ch for ch in line if ch not in self.unwanted_signs])
            words_in_line = line.split(' ')
            words_in_text = words_in_text + words_in_line
        return words_in_text
