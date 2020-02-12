# 垃圾文本生成器，利用马尔科夫模型来生成一段垃圾文本

import random

class MarkovTextGenerator:
    def __init__(self):
        pass

    def word_dict_create(self, text):
        text = text.replace('\n', ' ')
        text = text.replace('\"', '')
        punctuations = [',', '.', ';', ':']
        for punctuation in punctuations:
            text = text.replace(punctuation, ' '+punctuation+' ')
        words = text.split()
        words = [word for word in words if word != '']
        word_dict = {}
        for i in range(1, len(words)):
            if words[i-1] not in word_dict:
                word_dict[words[i-1]] = {}
            if words[i] not in word_dict[words[i-1]]:
                word_dict[words[i-1]][words[i]] = 0
            word_dict[words[i-1]][words[i]] += 1

        '''for i in range(1, len(words)):
            if words[i-1] not in word_dict:
                word_dict[words[i-1]] = []
            word_dict[words[i-1]].append(words[i])'''
        return word_dict

    def random_word_get(self, word_list):
        # current_word = random.choice(word_list)
        # return current_word
        sum = 0
        for value in word_list.values():
            sum += value
        rand_index = random.randint(1, sum)
        for word, value in word_list.items():
            rand_index -= value
            if rand_index <= 0:
                return word



    def text_get(self):
        with open('The Customs of Old England.txt', 'r') as f:
            text = f.read()
        return text

    def start(self):
        text = self.text_get()
        word_dict = self.word_dict_create(text)
        current_word = 'I'
        essay = ''
        word_count = 0
        print(word_dict['I'])
        while word_count < 1000:
            essay += current_word+' '
            word_list = word_dict.get(current_word)
            if word_list:
                current_word = self.random_word_get(word_list)
                word_count += 1
        print(essay)
        return essay

if __name__ == '__main__':
    m = MarkovTextGenerator()
    m.start()