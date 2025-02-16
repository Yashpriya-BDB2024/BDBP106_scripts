def calculate_gradePoint(grade):
#Convert the grade into upper case
    grade = grade.upper()
#Return the grade point based on the grade provided.
    if grade == 'A':
        return 4.0
    elif grade == 'B':
        return 3.0
    elif grade == 'C':
        return 2.0
    elif grade == 'D':
        return 1.0
    elif grade == 'F':
        return 0.0
    else:
        return None
def calculate_gpa():
#Initialize the total grade point to zero.
    total_gp = 0.0
#Loop through all the five subjects to get the grades.
    for i in range(1, 6):
        gr = input(f"Enter the grade for subject {i}: ")
#Check if the input falls in the given category or not
        if not(gr.upper()=='A' or gr.upper()=='B' or gr.upper()=='C' or gr.upper()=='D' or gr.upper()=='F'):
            print("Please enter only A, B, C, D, or F as grades.")
            exit (1)
        gp = calculate_gradePoint(gr)
        total_gp += gp
#Calculate GPA
    grade_point_avg = total_gp / 5
    print('Total GPA is', grade_point_avg)
def main():
    calculate_gpa()
if __name__ == "__main__":
    main()