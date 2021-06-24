# Square(n) sum
# Create a function that given a list of integers squares each number 
# passed into it and then sums the results together.
# Example Input: [1, 2, 2]
# Example Output: 9 
# Explanation: 1^2 + 2^2 + 2^2 = 9
# Example Input: [3, 4, 5]
# Example Output: 50

def square(n):
    return sum([num**2 for num in n])

print(square([1,2,2]))
        