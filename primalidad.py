number = int(input('introduce tu número: '))
def its_prime(number):
    counter = 0 
    result = True
    for i in range(1, number + 1):
        if (number % i == 0):
            counter += 1 
        if (counter > 2):
            result = False
        break
    return(result)   

if (its_prime(number) == True):
    print('El número es primo')
else:
    print('El número no es primo')



