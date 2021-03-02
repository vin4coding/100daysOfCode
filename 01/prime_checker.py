def prime_checker(number):
    isPrime= True
    for i in range(2, number-1):
        if number%i==0:
            isPrime = False
    if isPrime:
        print('its prime')

    else:
        print('Its not prime')

print(prime_checker(2100000))

