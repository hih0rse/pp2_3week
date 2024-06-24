def prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while(i*i)<=n:
        if n%i == 0:
            return False
        i+=1
    return True
def filter(numbers):
    return [num for num in numbers if prime(num)]
numbers = [2, 3,4, 5, 7,9, 10, 11, 13, 15, 17, 19, 20,21, 25, 31, 29]
prime_numbers = filter(numbers)
print(prime_numbers)
