def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1

    while a <= n:
        fib_series.append(a)
        a, b = b, a + b

    return fib_series

# Input from the user
try:
    n = int(input("Enter a number: "))
    if n < 0:
        print("Please enter a non-negative number.")
    else:
        result = fibonacci_series(n)
        print("Fibonacci series up to", n, "is:", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")

print("-"*30)

count = 0
while(True):
   if count % 3 == 0:
       print(count, end = " ")
   if(count > 15):
       break;
   count += 1

print("*"*30)

def solve(a, b):
   return b if a == 0 else solve(b % a, a)
print(solve(20, 50))

print(50%20)

word = "Python Programming"
n = len(word)
word1 = word.upper()
word2 = word.lower()
converted_word = ""
for i in range(n):
 if i % 2 == 0:
   converted_word += word2[i]
 else:
   converted_word += word1[i]
print(converted_word)

















