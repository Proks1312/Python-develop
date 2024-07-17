class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(punct, ' ')
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f" {file_name} нет такого")
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        found_positions = {}
        for file_name, words in all_words.items():
            try:
                position = words.index(word)
                found_positions[file_name] = position
            except ValueError:
                found_positions[file_name] = None
        return found_positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        word_count = {}
        for file_name, words in all_words.items():
            word_count[file_name] = words.count(word)
        return word_count

# Пример использования
# wf = WordsFinder('file1.txt')
# print(wf.get_all_words())
# print(wf.find('намнек'))
# print(wf.count('намнек'))
