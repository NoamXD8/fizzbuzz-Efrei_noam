def fizzbuzz(n):
    result = []
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
            result.append("Fizz")
        elif i % 5 == 0:
            print("Buzzzzzz")
            result.append("Buzzzzzz")
        else:
            print(i)
            result.append(str(i))
    return result

#Commit pour test pull request
#a = fizzbuzz(101)
#print(a)
fizzbuzz(101)