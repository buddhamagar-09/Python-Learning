# write a function called evaluate_grade(grade) that takes a single
#  letter grade(A,B,C,D or F) and return a description using a match-case statement

def evaluate_grade(grade):
    match grade :
        case "A" | "a":
            return "Excellent Work"
        case "B" | "b":
            return "Good Work"
        case "C" | "c":
            return "Satisfactory"
        case "D" | "d":
            return "Needs Improvement"
        case "F" | "f":
            return "Please see me after the class"
        case _:
            return "Invalid Grade"
print(evaluate_grade("a"))
