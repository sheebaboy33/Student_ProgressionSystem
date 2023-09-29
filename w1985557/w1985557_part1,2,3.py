
# Initializing marks and status lists.
marks = list()
status = list()


def get_marks():
    """The get_marks function will continue to iterate the program until the user quits."""  

    while True:
        # The loop will iterate until the main() returns False.
        repeat = main()

        if repeat:
            continue
        
        # The loop will break if the main() returns False and the program will stop and display the results.
        break


def main():
    """main function will validate marks entered by the user and will continue to iterate until the user quits."""
    
    while True:
        
        # Getting input from the user using the get_input function.
        pass_credits = get_input("Enter your total PASS credits: ")
        defer_credits = get_input("Enter your total DEFER credits: ")
        fail_credits = get_input("Enter your total FAIL credits: ")

        # Assigning the input received after validation into a list.
        marks_list = [pass_credits, defer_credits, fail_credits]

        # Validating if the sum is not equal to 120. If it is not, the user will be prompted again.
        if sum(marks_list) != 120:
            print("Total incorrect\n")
            continue

        # Calling the progression funtion.
        result = progression(marks_list)
        print(result, "\n")

        # Appending the lists after all input validations are completed.
        status.append(result)
        marks.append(marks_list)

        while True:
            # Prompting the user if they wish to continue and the return values will be passed on to the get_marks()
            
            print("Would you like to enter another set of data? ")
            choice = input("Enter 'y' for yes or 'q' to quit and view results: ").lower()
            print()

            if choice == "y":
                return True

            elif choice == "q":
                
                # Calling the histogram and the lists_part2 functions.
                histogram(status)
                lists_part2(status, marks)
                return False
            
            else:
                # Will reprompt the user until 'y' or 'q' is entered.
                print("Invalid input") 


def range_check(mark_input):
    """The range_check function  takes an integer as input and checks if it is out of range. If it is, returns False, else returns True"""

    # Validating if the marks are in the expected range.
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


def histogram(status_list):
    """The histogram function takes a list of status and will display a star infront of each level of progression and the total number of entries included once the user decides to quit the program"""

    # Using the count() to get the number in each module level.
    progress = status_list.count("Progress")
    trailer = status_list.count("Progress (module trailer)")
    retriever = status_list.count("Module retriever")
    exclude = status_list.count("Exclude")

    # Displaying the histogram
    print("\n--------------------------------------------------------------------------------------------------------\nHistogram\n")

    print(f"Progress {progress} : {progress * '*'}")
    print(f"Trailer {trailer} : {trailer * '*'}")
    print(f"Retriever {retriever} : {retriever * '*'}")
    print(f"Excluded {exclude} : {exclude * '*'}\n")

    # Getting the total number of items in the status list using the len()
    print(f"{len(status_list)} outcomes in total.")

    print("--------------------------------------------------------------------------------------------------------\n")

    
def lists_part2(status_list, marks_list):
    """The lists_part2() takes the status and marks lists as parameters, and displays the respective combination."""

    print("Part 2: \n")
    
    for i in range(len(status_list)):

        # Using the updated version of status_list and using the marks_list to display marks at each level seperated by a comma.
        print(f"{status_list[i]} - {marks_list[i][0]}, {marks_list[i][1]}, {marks_list[i][2]}")
    print()

           

def text_file_part3(status_list, marks_list):
    """The text_file_part3() takes the status and marks lists as parameters, firsts creates and writes  the output on the file and then diaplys using read"""

    # Opening the file in the write mode to create and write on the file.
    file = open("assignment.txt", "w")

    file.write("Part 3: \n\n")
    
    for i in range(len(status_list)):

        # Using the updated version of status_list and using the marks_list to display each mark seperated by a comma.
        file.writelines(f"{status_list[i]} - {marks_list[i][0]}, {marks_list[i][1]}, {marks_list[i][2]}\n")

    # Opening the file in the read mode
    file = open("assignment.txt", "r")

    #Assigning the content in the file to the content variable and printing it.
    content = file.read()
    print(content)

    # Closing the file once both reading and writing from the file is completed.
    file.close()



# Calling the get_marks function to start the program.
get_marks()


# Calling the text_file function to display the written file.
text_file_part3(status, marks)


