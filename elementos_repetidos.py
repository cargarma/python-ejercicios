 #Dada una lista, devolver los elementos repetidos

 dictionary =  {}

    for number in data:
        if number in dictionary:
            dictionary[number] += 1
        else:
		    dictionary[number] = 1
    
    result = []
    for number in data:
        if dictionary[number]>1:
            result.append(number)

