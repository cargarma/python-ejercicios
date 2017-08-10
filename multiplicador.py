#Dado un número, múltiplica sus dígitos ignorando los ceros

def checkio(number):
    n = str(number)
    
    result =1
    for digit in n:
        if digit != "0":
            result *= int(digit)        
    
    

    return result

print(checkio(123405))