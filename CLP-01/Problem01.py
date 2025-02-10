def sum_(numbers):
    sum_odd = 0
    sum_even = 0

    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return sum_odd, sum_even

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_odd, sum_even = sum_(numbers)

print(f"Sum of odd numbers: {sum_odd}")
print(f"Sum of even numbers: {sum_even}")
