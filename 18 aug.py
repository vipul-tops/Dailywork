# prime Number

start_range = 1
end_range = 100

prime_numbers = []

for num in range(start_range, end_range + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Prime numbers between", start_range, "and", end_range, "are:", prime_numbers)

#number limit

limit = int(input("Enter the upper limit: "))

prime_numbers = []

for num in range(2, limit + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print("Prime numbers up to", limit, "are:", prime_numbers)

#given number is prime or not prime

n = int(input("Enter Number: "))

if n == 2:
    print(n, "is prime")
elif n <= 1 or n % 2 == 0:
    print(n, "is not prime")
else:
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            print(n, "is not prime")
            break
    else:
        print(n, "is prime")



re=sum([1,2,3])
print(re)

a = ['mn', 'op']

print(len(list(map(list, a))))


# Example list
my_list = [5, 3, 9, 1, 7, 2]

# Find the smallest and largest values
min_val = my_list[0]
max_val = my_list[0]

for num in my_list:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

# Print the results
print("Smallest value:", min_val)
print("Largest value:", max_val)

#pattern square
num=int(input("Enter N : "))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")

