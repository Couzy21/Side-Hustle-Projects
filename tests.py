from statistics import mean

# Imported statistics module to access mean for my average

# Created a list that accepts input from the user and calculates the average for further analysis
student_input = input("Input student scores separated by commas: ")
new_student_input = student_input.split(",")
new_student_input1 = list(map(int, new_student_input))
average_scores = mean(new_student_input1)
print("The class average is: " + str(average_scores))

# Created a for loop that iterates through the input and created conditions within the loop that meets the required
# scores
for n in range(len(new_student_input1)):
    pass_score = average_scores - 5
    if (new_student_input1[n]) >= 60 and new_student_input1[n] >= pass_score:
        print("The student passed with a score of: " + str(new_student_input1[n]))
    else:
        print("The student failed with a score of: " + str(new_student_input1[n]))
