#From the provided name list create the dict comp where the name should be key and
# value should be the score and score will be the random number from 1 to 100
#create the new conditional dictionary using the above dictionary where score should be above 60

import random

names = ["savithri", "gayathri", "rudr", "vasu", "munna", "lalitha"]
student_score = {student: random.randint(1, 100) for student in names}
print(f"Student's score are {student_score}")

student_passed = {student: score for (student, score) in student_score.items() if score >= 60}
print(f"Student who had passed in exam are {student_passed}")
#==================================
#You are going to use Dictionary Comprehension to create a dictionary called result
# that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
word_list = sentence.split(" ")
print(word_list)

result = {word: len(word) for word in word_list}
print(result)


