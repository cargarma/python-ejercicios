 #Dada una lista, devolver los elementos repetidos

 data_copy = data[:] #create a copy that won't mutate
    for num in data_copy: #iterate thru the list copy
        if data.count(num) == 1:
            data.remove(num) #delete from original list
    return data
