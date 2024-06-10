from numpy import array


with open('ignfiles/words.txt', encoding="utf-8") as f:
    ram_eater = [i.strip() for i in f.readlines()]
    words_list = array(ram_eater)
    del ram_eater

