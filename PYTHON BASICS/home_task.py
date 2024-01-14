# Function to generate Fibonacci numbers up to a given limit
def generate_fibonacci(num):
    fibonacci_series = [0, 1]
    while fibonacci_series[-1] + fibonacci_series[-2] <= num:
        next_fib = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_fib)
    return fibonacci_series

# Function to filter and print Fibonacci numbers divisible by 3, 4, or 5
def print_divisible_fibonacci(num):
    fibonacci_series = generate_fibonacci(num)
    divisible_numbers = [num for num in fibonacci_series if num % 3 == 0 or num % 4 == 0 or num % 5 == 0]
    
    for number in divisible_numbers:
        print(number, end=",")

num = 1000 

# Call the function to print Fibonacci numbers
print_divisible_fibonacci(num)
