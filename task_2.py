# Write a program that takes a file name as command line argument,
# count how many times each word appears in the file and prints the word that appears the most
import sys
if __name__ == "__main__":

    f_name = sys.argv[1]

    file1 = open(f_name, 'r')
    text1 = file1.read()
    text_list = text1.split()
    text_list.sort()
    words_counter=0
    main_word = ''

    for i in text_list:
        mx = text_list.count(i)
        if mx > words_counter:
            words_counter = mx
            main_word = i

    print (main_word, words_counter)

