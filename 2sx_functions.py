def add_to_dict(token, token_dict):
	if token in token_dict:
		token_dict[token] += 1

	else:
		token_dict[token] = 1

def add_word_to_dict(char, word, char_dict):
	if len(char)== 1:
		ok_char = double_char(char)

		if ok_char not in char_dict.keys():
				char_dict[ok_char] = [word]
		else:
			if word not in char_dict[ok_char]:
				char_dict[ok_char].append(word)
	else:
		if char not in char_dict.keys():
			char_dict[char] = word

def dict_to_file(py_dict, path, fileName, sort= False):
	fileOut = open(path + fileName, 'w+')
	if sort == True:
		sort_items  = sorted(py_dict.items(), key=lambda x:x[1], reverse= True)
		#count = 10
		for i in sort_items:
			fileOut.write(str(i[0]) + ',' + str(i[1]) + '\n')
			'''
			if count != 0:
				print(i[0], i[1])
				count -= 1
			print('Dictionary saved as ', fileName)
			'''
	else:
		for key,value in py_dict.items():
			value_out = value
			if isinstance(value, list):
				value_out= ','.join(value)

			fileOut.write(key + ':' + value_out + '\n')

	fileOut.close()

def double_char(word, original = True):
	new_word = word
	if original:
		if 'tʃ' in word:
			new_word = word.replace('tʃ','x')
		if 'dʒ' in word:
			new_word = word.replace('dʒ', 'y')
	else:
		if 'x' in word:
			new_word = word.replace('x', 'tʃ')
		if 'y' in word:
			new_word = word.replace('y', 'dʒ')
	return new_word

