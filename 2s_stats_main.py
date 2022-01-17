from functions import add_to_dict, add_word_to_dict, dict_to_file, double_char
import numpy as np 
import pandas as pd

# Files 
pathIn = "/home/modo/TEFL_asr/"
nameIn = "harvardPhones_v4.txt"
transIn = "harvardCleanNoPunc.txt"

fileIn = open(pathIn + nameIn, 'r')
fileTransIn = open(pathIn + transIn, 'r')
#fileOut = open(pathIn + 'results.txt', 'w+')

utterances = fileIn.readlines()
sentences = fileTransIn.readlines()

# Variables
sents_count = 0
words_count = 0
chars_count = 0
graphs_count = 0

n_words_per_sent_list = []
n_chars_per_sent_list = []
n_graphs_per_sent_list = []
n_diff_words_per_sent = []
n_diff_chars_per_sent = []
phone_set_per_sent =[]

word_freq = {}
char_freq = {}
char_in_words = {}
words2graphies = {}

# Main body
for idx_s, utterance in enumerate(utterances):
	if utterance:
		sents_count += 1
		#print("Processing utterance...", sents_count)
		words = utterance.split()
		graphies = sentences[idx_s].split()
		words_per_sent_count = len(words)
		n_words_per_sent_list.append(words_per_sent_count)
		words_count += words_per_sent_count
		n_chars_per_word_list = []
		n_graphs_per_word_list = []
		chars_per_sent_count = 0
		graphs_per_sent_count = 0
		word_dict = {}
		char_dict = {}

		for idx_w, word in enumerate(words):
			single_char_word = double_char(word)

			chars_per_word_count = len(single_char_word)
			n_chars_per_word_list.append(chars_per_word_count)
			chars_per_sent_count += chars_per_word_count

			graphie = graphies[idx_w].lower().strip()
			graphs_per_word_count = len(graphie)
			n_graphs_per_word_list.append(graphs_per_word_count)
			graphs_per_sent_count += graphs_per_word_count			

			# Word Frequency
			#print('adding ' + graphie + ' => ' + word)
			add_word_to_dict(word, graphie, words2graphies)
			add_to_dict(graphie, word_dict)
			add_to_dict(graphie, word_freq)

			for char in single_char_word:
				chars_count += 1
				ok_char = double_char(char, original= False)

				add_to_dict(ok_char, char_dict)
				add_to_dict(ok_char, char_freq)
				#print('Phoneme  ' + char + ' in ' + word + ' => ' + graphie)
				add_word_to_dict(char, graphie, char_in_words)

		n_chars_per_sent_list.append(chars_per_sent_count)
		n_graphs_per_sent_list.append(graphs_per_sent_count)
		n_diff_words_per_sent.append(len(word_dict))
		n_diff_chars_per_sent.append(len(char_dict))
		phone_set_per_sent.append(list(c for c in char_dict.keys()))
		graphs_count += graphs_per_sent_count

fileIn.close()		

print('\n------------------')
print('Totals')
print('------------------')
print('Sentence', sents_count)
print('Word count', words_count)
print('Phoneme count', chars_count)
print('Grapheme count', graphs_count)
print('------------------\n')
'''
print('Lengths in unique')
print('------------------')
print('words', len(word_freq))
print('phonemes', len(char_freq))
'''
print('\n---Phone Set---', len(char_freq))
print(char_freq.keys())

# Print out Files
df = pd.DataFrame(list(zip(n_words_per_sent_list,\
							n_graphs_per_sent_list, \
							n_chars_per_sent_list, \
							n_diff_words_per_sent, \
							n_diff_chars_per_sent, \
							phone_set_per_sent)), \
					index = [x for x in range(1, sents_count+1)], \
					columns = ['n_words', \
							'n_graphs', \
							'n_phones', \
							'n_unique_words', \
							'n_unique_phones', \
							'phones'])

print('\n------------------')
print(df.info())
print('------------------')
print(df.head())

df.to_csv(pathIn + 'harvard_data.csv')

# Frequency . Sort dictionaries by value and save them as csv files

dict_to_file(word_freq, pathIn, 'word_freq.csv', sort=True)
dict_to_file(char_freq, pathIn, 'phone_freq.csv', sort=True)

# Save dict as txt files
dict_to_file(char_in_words, pathIn, 'phone_in_words.txt')
dict_to_file(words2graphies, pathIn, 'ipa2graphies.txt')


print('\n----------End of Script\n--------\n')