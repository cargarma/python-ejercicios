#Conversor de base
import string

def checkio(str_number, radix):
	result = 0;
	cont = 1;
	lenght = len(str_number)
	for digit in str_number:
		if(digit.isalpha()):
			letter = str(digit)			
			value =string.ascii_lowercase.index(letter.lower())+10
		else:
			value = int(digit)
		result +=  value*(radix**(lenght-cont))
		cont+=1   
	
	return result

print(checkio("AF", 16))
print(checkio("101", 2))
print(checkio("AF", 16))
print(checkio("AF", 16))
print(checkio("AF", 16))
