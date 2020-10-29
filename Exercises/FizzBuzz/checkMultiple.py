def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return 'FizzBuzz'

    elif num % 3 == 0:
        return 'Fizz'

    elif num % 5==0:
        return 'Buzz'
    
    elif num % 7==0:
        return 'Bang'
     
    elif num % 11==0:
        return 'Bong'
    
    elif num % 13==0:
        return 'Fezz'

    elif num%3==0 and num%7==0:
        return 'FizzBang'
    else:
        return num

#for n in range(1,100):
#   print(fizz_buzz(n))
print('value when number is '  + fizz_buzz(11))