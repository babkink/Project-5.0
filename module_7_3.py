import string

class Words_finder:
    file_names = []
    def __init__(self, *args):
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            low_line = ''
            with open(i) as file:
                for line in file:
                    ll = line.lower().translate(str.maketrans('', '', string.punctuation))
                    low_line = low_line + ll
                low_line_final = low_line.split()
                all_words[file.name] = low_line_final
        return all_words

    def find_word(self, word):
        find_word_dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                find_word_dict[(name)] = words.index(word.lower())
        return find_word_dict

    def count_word(self, word):
        count_word_dict = {}
        for name, words in self.get_all_words().items():
            i = 0
            if word.lower() in words:
                count_word_dict[(name)] = words.count(word.lower())
                i += 1
                return count_word_dict
        if i == 0:
            return f'There is no word "{word}" in the file'


str_ = "It's a text for task,, Найти везде, Используйте его // для самопроверки. Успехов в решении задачи! text text text"
finder1 = Words_finder('Test 7.3.txt', 'Test 7.3.1.txt')
print(finder1.file_names)
print(finder1.get_all_words())
print(finder1.find_word('text'))
print(finder1.count_word('рак'))