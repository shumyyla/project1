def func(num):
    fact =1
    for i in range(1,num+1):
        fact = fact * i
    return fact

number = 5
rv = func(number)
print("Factorial of {} is {}".format(number, rv))