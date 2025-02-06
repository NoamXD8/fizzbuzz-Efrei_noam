def fizzbuzz(n):
    '''
    Cette fonction génère une suite contenant les résultats de FizzBuzz pour les nombres de 1 à n-1. 
    Voici les règles :
    - Si le nombre est divisible par 3 et 5, on affiche "FizzBuzz".
    - Si le nombre est divisible par 3 mais pas par 5, on affiche "Fizz".
    - Si le nombre est divisible par 5 mais pas par 3, on afffiche "Buzz".
    - Sinon, on affiche juste le nombre en question.
    '''
    result = []
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
            result.append("Fizz")
        elif i % 5 == 0:
            print("Buzz")
            result.append("Buzz")
        else:
            print(i)
            result.append(str(i))
    return result

#Commit pour test pull request

#a = fizzbuzz(101)
#print(a)
fizzbuzz(101)