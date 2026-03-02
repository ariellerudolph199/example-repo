end = False
# while loop that runs the program until the user decides to stop
while end == False:
    # while loop and try statement that only breaks
    #  if a valid input is given
    while True:
        try:
            # requests calculation
            value = input("Enter your calculation: ")
            # Calculates the length of the input for the loop
            length = len(value)
            # list that contains the seperate numbers in the equation
            numbers = []
            # list that contains all the functions in the equation
            functions = []
            # value that tracks the starting position of a number
            start_pos = 0
            # assigned type to awnser value
            answer = float
            # used to track the positions of values in the equation
            skip = 0
            # number that keeps track of 
            # numbers removed from previous calculations
            gone = 0
            # loop that goes through each character
            # , identifying both numbers and functions
            position = []
            for loop in range(0, length):
                currentchar = value[loop]
                # if statement that activates if the current 
                # character is a function
                if (currentchar == "+" or currentchar == "-" or 
                currentchar == "*" or currentchar == "/"):
                    # adds the function to the list
                    functions.append(currentchar)
                    # identifies the end position of the number
                    end_pos = loop
                    # converts the read number into a string
                    current_string = value[start_pos:end_pos]
                    # converts the string into an integer
                    current_number = int(current_string)
                    # adds the integer to the list of numbers
                    numbers.append(current_number)
                    # calculates the starting position 
                    # of the next number
                    start_pos = loop+1
                # elif statement to add the final value, 
                # where there is no function involved
                elif loop == length-1:
                    # calculates the ending position of 
                    # the final number
                    end_pos = loop+1
                    # adds final number to the list
                    current_string = value[start_pos:end_pos]
                    current_number = int(current_string)
                    numbers.append(current_number)

            # loop for division goes first to ensure 
            # order of operations
            for division_loop in functions:
                # goes through all functions to identify
                #  all divide functions
                if division_loop == "/":
                    # calculates the awnser of the division
                    answer = numbers[skip]/numbers[skip+1]
                    # replaces first & second number to be 
                    # processed further
                    numbers[skip] = answer
                    numbers[skip+1] = answer
                skip += 1
            skip = 0
            for multiplication_loop in functions:
                if multiplication_loop == "*":
                        # calculates the awnser of the multiplication
                        answer = numbers[skip]*numbers[skip+1]
                        # replaces first & second number 
                        # to be processed further
                        numbers[skip] = answer
                        numbers[skip+1] = answer
                # Calculates the position of the numbers 
                # being processed
                skip += 1
            skip = 0
            for as_loop in functions:
                if as_loop == "+":
                    # calculates the awnser of the addition
                    answer = numbers[skip]+numbers[skip+1]
                    # replaces first & second number to be 
                    # processed further
                    numbers[skip] = answer
                    numbers[skip+1] = answer
                elif as_loop == "-":
                    # calculates awnser of subtraction
                    answer = numbers[skip]-numbers[skip+1]
                    # replaces first & second number to be 
                    # processed further
                    numbers[skip] = answer
                    numbers[skip+1] = answer
                skip += 1
            # breaks if no value error is given
            break
        except ZeroDivisionError:
            print("awnser is undefined. Please refrain from"
                   "dividing by zero.")
        except ValueError:
            # error message
            print("Refrain from typing any letters please.")
    # writes to file if no error occurs
    while True:
        # Checks if the file exists
        try:
            with open("equations.txt", "a") as file:
                # writes the equation and the answer to file
                file.write(f"{value} = {answer} \n")
            # asks the user if they want to print the file contents
            print("Type \"print\" to print previous equations")
            print("Type \"continue\" to enter another equation")
            print("Type \"stop\" to close the program")
            print_file = input("Type here: ")
            print_file = print_file.lower()
            # prints the contents of the file if the user
            #  gives the appropriate input
            if print_file == "print":
                with open("equations.txt", "r")as f:
                    for line in f:
                        print(line)
            # asks the user if they want to end the program
            if print_file == "stop":
                # ends the program if the user gives the
                #  appropriate input
                end = True
                break
            if print_file == "continue":
                break
        except FileNotFoundError:
            # error message if the file does not exist
            print("The file \"equations.txt\" does not exist"
                   " and cannot be written to.")
            # informs the user that the program will now end
            print("The program will now end.")
            # automatically ends the program
            end = True
            break
# note the program struggles to track values a bit, 
# however the error handling and writing work perfectly
# I would add the abilty to track numbers but it's a bit 
# too complex and I have spent too long on this.
# simple equations without multiple parts will also work perfectly