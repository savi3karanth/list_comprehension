student_dict = {
    "student": ["savithri", "vaijanath", "rudr"],
    "score": [84, 72, 90],
}

#looping through dictionaries
for (key, value) in student_dict.items():
    print(key, value)
print()

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print()

#Loop through a data frame
for key, value in student_data_frame.items():
    print(f"Prints only the value \n{value}")

print("Loop through rows in data frame rather then each of column using the inbuilt method iterrows")
for index, row in student_data_frame.iterrows():
    print(f"prints only the index  ie {index}")
    print(row)
    print(f"prints the row of each students score line by line as this {row.score}")
    print(f"prints the row of each student name line by line as this {row.student}")
    if row.student == "savithri":
        print(f"prints the score of savithri ie {row.score}")

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(index, row)