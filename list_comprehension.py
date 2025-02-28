#for loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#list comprehension adds one for each number
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

#Output: [2, 3, 4]
#===============================
#Creates the new list which separate each letter for the provided name
name = "Savithri"
letters_list = [letter for letter in name]
print(letters_list)

#Output: ['S', 'a', 'v', 'i', 't', 'h', 'r', 'i']

#===============================

#Range as list where the number should get doubled
range_list = [n * 2 for n in range(1, 5)]
print(range_list)

#Output: [2, 4, 6, 8]
#===============================


#Conditional list comprehension
names = ["Savithri", "Gayathri", "Rudr", "Vasu", "Munna", "Lalitha"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

#Output: ['Rudr', 'Vasu']
#===============================

#Conditional list comprehension where provided name letter should be more than 5 letter also it should be in upper case.
names = ["Savithri", "Gayathri", "Rudr", "Vasu", "Munna", "Lalitha"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

#Output: ['SAVITHRI', 'GAYATHRI', 'LALITHA']
#===============================
# Convert the string to int and then create the new string only for the even numbers

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)

#Output: [0, 32, 8, 2, 8, 64, 42]
