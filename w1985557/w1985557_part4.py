
# Initializing marks, status and uni_id lists.

marks = list()
status = list()
uni_id_list = list()


def get_marks():
    """The get_marks function will continue to iterate the program until the user quits."""  

    while True:
        repeat = main()

        if repeat:
            continue
        
        # The loop will break if the main() returns False and the program will stop.
        break

    
def main():
    """main function will validate marks entered by the user and will continue to iterate until the user quits."""
        
    while True:
        
        # Getting marks input from the user using the get_input function.
        uni_id = input("Enter the student University identification: ")
        pass_credits = get_input("Enter your total PASS credits: ")
        defer_credits = get_input("Enter your total DEFER credits: ")
        fail_credits = get_input("Enter your total FAIL credits: ")

        # Assigning the input received after validation into a list.
        marks_list = [pass_credits, defer_credits, fail_credits]

        # Validating if the sum is not equal to 120. If it is not, the user will be prompted again.
        if sum(marks_list) != 120:
            print("Incorrect total\n")
            continue
        
        # Calling the progression funtion.
        result = progression(marks_list)
        print(result, "\n")
        
    
        # Appending the lists after all input validations are completed.
        status.append(result)
        marks.append(marks_list)
        uni_id_list.append(uni_id)

        while True:
            # Prompting the user if they wish to continue and the return values will be passed on to the get_marks()
            print("Would you like to enter another set of data? ")
            choice = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
            print()

            if choice == "y":
                return True

            elif choice == "q":
                # Calling the dict_part4 function to display the desired output from the dictionary.
                dict_part4(status, marks, uni_id_list)
                return False
            
            else:
                # Will reprompt the user until 'y' or 'q' is entered.
                print("Invalid input") 



def range_check(mark_input):
    """The range_check function  takes an integer as input and checks if it is out of range. If it is, returns False, else returns True"""
    
    # Validating if the marks entered are within the expected range.
    if mark_input % 20 != 0 or mark_input not in range(0,121):
        return False
    
    return True


def get_input(prompt):
    """The get input function takes a prompt as input and checks if it is valid by making sure it is an integer using exception handling and by executing the get_range function"""
    
    while True:
        
        # Exception handling is used to detect if there is a ValueError in the user input.
        try:
            mark_input = int(input(prompt))

            # Calling the range_check function.
            if not range_check(mark_input):
                print("Out of range\n")
                continue
            
            return mark_input
        
        except ValueError:
            print("Integer required\n")


def progression(marks):
    """The progression function will categorize the list of marks into 'Progress', 'Progress (module trailer)' 'Do not progress - module retriver' and 'Exclude'"""

    # Categorizing Progress
    if marks[0] == 120:
        return "Progress"

    # Categorizing module trailer
    elif marks[0] == 100:
        return "Progress (module trailer)"

    # Categorizing module retriever
    elif marks[2] in range(0,61):
        return "Module retriever"

    # Categorizing exclude
    else:
        return "Exclude"


def dict_part4(status_list, marks_list, id_list):
    
    marks_dict = dict()
    
    for i in range(len(status_list)):

        # 
        values = f"{status_list[i]} - {marks_list[i][0]}, {marks_list[i][1]}, {marks_list[i][2]}"

        # Creating a dictionary with student ID as key and values variable as values.
        marks_dict[id_list[i]] = values


    print("Part 4: \n")
    
    # Printing the dictionary with student IDs and progression data.
    for key, value in marks_dict.items():
        print(f"{key} : {value}")


get_marks()

