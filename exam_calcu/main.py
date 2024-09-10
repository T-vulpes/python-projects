print("*** Exam Calculation ***")

try:
    name = input("Enter your name and surname: ")
    midterm = float(input("Enter your midterm grade: "))
    final = float(input("Enter your final grade: "))
    
    if midterm < 0 or midterm > 100 or final < 0 or final > 100:
        raise ValueError("Grades should be between 0 and 100.")
    
    success_score = (midterm * 40 / 100) + (final * 60 / 100)
    
    print("\n")

    if success_score > 85:
        grade = "AA"
    elif 85 >= success_score > 70:
        grade = "BA"
    elif 70 >= success_score > 60:
        grade = "BB"
    elif 60 >= success_score > 50:
        grade = "CB"
    elif 50 >= success_score > 40:
        grade = "CC"
    else:
        grade = "FF"

    print("Student Name-Surname:", name)
    print("Midterm grade:", midterm)
    print("Final grade:", final)
    print("Success score:", success_score)
    print("Your grade is", grade)

    with open("student.txt", "a") as file:
        file.writelines("{} has obtained a success score of {}\n".format(name, success_score))

except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)

input("Press Enter to exit...") 
