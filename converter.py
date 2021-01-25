from data import MORSE_CODE_DICT, Data


class Converter:
    def __init__(self):
        self.text = ""
        self.converted_text = ""
        self.history = []

    def get_user_input(self):
        self.text = input('Please input your text: ')

    def convert(self):
        for char in self.text:
            try:
                self.converted_text += f'{MORSE_CODE_DICT[char.upper()]} '
            except KeyError:
                self.converted_text += '<OOV> '

        self.history.append(Data(text=self.text, converted_text=self.converted_text))

    def display_converted_text(self):
        print(self.converted_text)

    def display_history(self):
        if len(self.history) == 0:
            print("No history available.")
            return

        for data in self.history:
            print('===== [History] =====')
            print(f'Original text: {data.text}')
            print(f'Converted text: {data.converted_text}')
            print('---')
