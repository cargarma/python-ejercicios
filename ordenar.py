numbers =(-20, -5, 10, 15)
list_numbers = list(numbers)
list_numbers.sort()
negative_numbers = [number for number in numbers if number<0]


sorted_numbers = [abs(number) for number in numbers]
sorted_numbers.sort()

for item in negative_numbers:
    index = sorted_numbers.index(abs(item))
    sorted_numbers[index] *=-1

	    
print(sorted_numbers)

