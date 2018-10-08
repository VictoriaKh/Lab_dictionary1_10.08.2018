# put your code here.
# open file with separated words 

punctuation = [',', '.', ':']

def list_iter(): 

	with open("twain.txt") as file:
		item_dict = {}
		for line in file:
			line = line.rstrip()
			words = line.split(' ')
			for word in words:
				word = word.lower()
#				print(word, len(word))
				if word:
					if word[-1] in punctuation:
						word = word[0:-1]

				if word in item_dict:
					item_dict[word] = item_dict[word] + 1
				else:
					item_dict[word] = 1

			# print(word, item_dict[word])

		for word in item_dict:
			print('{}: {}'.format(word, item_dict[word]))


	return item_dict

# for i in list_iter():
# 	i = '{}: {}'.format(i[0], i[1])
list_iter()


