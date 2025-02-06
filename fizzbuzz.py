def fizzbuzz(n):
    result = []
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
            #print("FizzBuzz")
        elif i % 3 == 0:
            #print("Fizz")
            result.append("Fizz")
        elif i % 5 == 0:
            #print("Buzz")
            result.append("Buzz")
        else:
            #print(i)
            result.append(str(i))
    return result

a = fizzbuzz(4)
print(a)