def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)
    
c = average(12, 12, 24, 34, 12, 9)
print(f"Average of numbers are {c}")