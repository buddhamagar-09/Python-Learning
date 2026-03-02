# match_case statement and alternate way to use elif statements

def day_week(day):
    match day:
        case 1:
            return "sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid Day"

print(day_week(9))