import os
import codecs

def handle_file(dir_name, target_file):
    target_words = set()
    files = os.listdir(dir_name)
    print(files)
    files = [file for file in files if os.path.splitext(file)[-1] == '.txt']
    for fi in files:
        fi = os.path.join(dir_name, fi)
        with codecs.open(fi, 'r') as f:
            lines = f.readlines()
            target_words = target_words.union(set(lines))
    with codecs.open(target_file, 'a+') as f:
        for line in target_words:
            f.writelines(line)
    return target_words



if __name__ == '__main__':
    dir_name = 'txt'
    target = 'agri_voca_unique2.txt'

    handle_file(dir_name, target)
