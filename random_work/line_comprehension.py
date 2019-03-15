

# Use the code below to answer all of the exercises:

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]


# output = []
# for fruit in fruits:
#     output.append(fruit.upper())

# Rewrite the above example code below using a list comprehension.
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [i.upper() for i in fruits]
# print(uppercased_fruits)


# Create a variable named capitalized_fruits and
# use a list comprehension to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = [i.title() for i in fruits]
# print(capitalized_fruits)

#
# Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# Hint: You'll need a way to check if something is a vowel.

def vowel():
    if word 





#
# Make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi']
#
# Make a list that contains each fruit with more than 5 characters

more_than_5 = [word for word in fruits if len(word) > 5]
# print(more_than_5)


# Make a list that contains each fruit with exactly 5 characters

exactly_5 = [word for word in fruits if len(word) == 5]
# print(exactly_5)


# Make a list that contains fruits that have less than 5 characters

less_than_5 = [word for word in fruits if len(word) < 5]
# print(less_than_5)


# Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

word_count = [len(word) for word in fruits]
# print(word_count)


# Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [word for word in fruits if 'a' in word]
# print(fruits_with_letter_a)


# Make a variable named even_numbers that holds only the even numbers

even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)


# Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = [num for num in numbers if num % 2 ==1]
# print(odd_numbers)


# Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = [num for num in numbers if num > 0]
# print(positive_numbers)


# Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = [num for num in numbers if num < 0]
# print(negative_numbers)


# Use a list comprehension with a conditional in order to produce a list of numbers with 2 or more numerals

two_num = [num for num in numbers if num > 9 or num < -9]
# print(two_num)


# Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = [n**2 for n in numbers]
# print(numbers_squared)


# Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_numbers = [num for num in numbers if num < 0 and num % 2 == 1]
# print(odd_negative_numbers)


# Make a variable named primes that is a list containing the prime numbers in the numbers list.

primes = [num for num in numbers if num % num in range(1,9) != 0]
print(primes)




