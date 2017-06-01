# def list_to_dict(list):
# 	d_words = {}
# 	for i in words:
# 		ws = d_words.get(len(i), [])
# 		ws.append(i)
# 		d_words[len(i)] = ws
# 	return d_words
#
#
# def search_loop_words(words):
# 	d_words = list_to_dict(words)
# 	for count, words in d_words.items():
# 		for i in range(count):
# 			head = words[0][:i+1]
# 			tail = words[0][i+1:]
# 			for w in words[1:]:
# 				if head == w[-(i+1):] and tail == w[:count-(i+1)]:
# 					print(words[0], w)
#
# if __name__ == '__main__':
# 	words = ['picture', 'turepic', 'icturep', 'word', 'ordw']
# 	search_loop_words(words)
#

def read_data():
    words = []
    n = 1
    words_count = input()
    while n <= int(words_count):
        word = input()
        words.append(word)
        n += 1
    return words


def list_to_dict(list):
    d_words = {}
    for i in words:
        ws = d_words.get(len(i), [])
        ws.append(i)
        d_words[len(i)] = ws
    return d_words


def search_loop_words(words):
    loop_count = 0
    loop_set = set()
    d_words = list_to_dict(words)
    for count, words in d_words.items():
        for i in range(count):
            head = words[0][:i + 1]
            tail = words[0][i + 1:]
            for w in words[1:]:
                if head == w[-(i + 1):] and tail == w[:count - (i + 1)]:
                    print(words[0], w)
                    loop_count += 1
                    loop_set.add(words[0])
    return loop_set


if __name__ == '__main__':
    words = read_data()
    count = search_loop_words(words)
    print(len(count))
