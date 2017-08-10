dictionary =  {}
text = "One"
for letter in text:
		if(letter.isalpha):
			lower_letter = letter.lower()
			if lower_letter in dictionary:
				dictionary[lower_letter] += 1 
			else:
				dictionary[lower_letter] = 1
	#replace this for solution
print(dictionary)

maxval = max(dictionary.values())
letter = dictionary


items = []
for letter, count in dictionary.items():
    if count == maxval:
        items.append(letter)

print(sorted(items)[0])