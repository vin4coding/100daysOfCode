def iqtest(numbers):
    num = list(map(int,numbers.split(' ')))
    val = [int(i)%2 for i in numbers.split(' ')]
    if val.count(0)>1:
        return val.index(1)+1
    else:
        return val.index(0)+1
    
print(iqtest("1 3 4 5 7 9"))

