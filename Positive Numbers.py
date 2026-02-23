# Program to print all positive numbers in a list

# Example lists
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

# Function to get positive numbers
def positive_numbers(lst):
    result = []
    for num in lst:
        if num > 0:
            result.append(num)
    return result

# Output for list1 (without brackets, like example 1)
print("Input: list1 =", list1)
print("Output:", ", ".join(map(str, positive_numbers(list1))))

# Output for list2 (with brackets, like example 2)
print("Input: list2 =", list2)
print("Output:", positive_numbers(list2))

Output:
Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64
Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]
