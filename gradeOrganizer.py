from os import system

students = [
    ("Maxwell", [5, 4, 2, 3, 4]),
    ("Jane", [3,2,1,3,4])
]

sorted_students = sorted(students, key=lambda item: sum(item[1]) / len(item[1]), reverse=True) # Sort students by average of grades
running=True

def showByGrades(): # Display students list by descending average grades
    print("\n--- Descending Grades Order ---")

    for i in sorted_students:
        avg = sum(i[1]) / len(i[1])
        print(f"{i[0]}, Average: {avg}")

def showBest(): # Display only three students with highest average grades
    counter = 0
    print("\n--- Three Best Students ---")
    for i in sorted_students:
        if not counter == 3:
            avg = sum(i[1]) / len(i[1])
            print(f"{i[0]}, Average: {avg}")
            counter+=1
        else:
            break

def showByName():
    print("\n--- Alphabetical Order ---") # Display list of students in alphabetical order

    name_sorted = sorted(sorted_students, key=lambda item: item[0])
    for i in name_sorted:
        avg = sum(i[1]) / len(i[1])
        print(f"{i[0]}, Average: {avg}")


def main(): # Entry function
    system('cls')

    while running:
        user_input = int(input("Option (1, 2, 3): "))

        if user_input == 1: # Call showByGrades function
            showByGrades()
            print('')
        elif user_input == 2: # Call showBest function 
            showBest()
            print('')
        else: # Call showByName function, program doesent except anything else so just call the function so it wont raise an error
            showByName()
            print('')

if __name__ == "__main__":
    main()
