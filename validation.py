"""
Author:     -_-
File:       proj5_validation.py
Date:       5/3/2023
Description:A program to grade your project has the same output as the starting file.
"""
import os.path

# Enter the baseline FileName to be compared against:
FILE_1 = ""

# Enter the FileName you want to be compared to FILE_1:
FILE_2 = ""

""" 
Function Name: menu 
Pre-Condition:  The function is passed a string.
Post-Condition: Return true if a file exist in the directory
"""
def menu():
    print("Welcome to the Project 5 Validation Program!!")

""" 
Function Name:  validate_file
Pre-Condition:  The function is passed a string.
Post-Condition: Return true if a file exist in the directory
"""
def validate_file(path = ""):
    return os.path.isfile("./" + path)

    
""" 
Function Name:  compare_files
Pre-Condition:  The function is passed a string.
Post-Condition: Return true if a file exist in the directory
"""
def compare_files(based_file = "", comparison_file = ""):
    based_file_list = []
    compare_files_list = []
    
    with open(based_file) as file:
        for line in file:
            based_file_list.append(line.strip())
            
    with open(comparison_file) as file:
        for line in file:
            compare_files_list.append(line.strip())
    
    if True if based_file_list == compare_files_list else False:
        return True
    else:
        if len(based_file_list) != len(compare_files_list):
            print(f"ERROR: {FILE_1} and {FILE_2} are two different lengths.")
            print()
        else:
            for i in range(len(based_file_list)):
                if based_file_list[i] != compare_files_list[i]:
                    print(f"Error at Line: {i}")
                    print(f"Line {i} in {FILE_1}:\n{based_file_list[i]}")
                    print(f"Line {i} in {FILE_2}:\n{compare_files_list[i]}")
                    print()
                
        return False


if __name__ == "__main__":
    tries = 0
    user_input = ""
    
    # Print the Menu:
    menu()
    
    # Verifying FILE_1:
    while (user_input.lower() != 'q' and user_input.lower() != 'quit'):
        # Ensure FILE_1 is a valid file in the directory:
        while(not validate_file(FILE_1) and user_input.lower() != 'q' and user_input.lower() != 'quit'):
            # Error Msg:
            if (tries >= 1):
                print("Invalid Filename. Please try Again".center(50, "-"))
                print()
            
            # User user_Input:
            FILE_1 = input("Enter a Filename to act as the BASE file (Q/Quit to Exit Program):\n>> ").strip()
            user_input = FILE_1
            tries += 1
        else:
            # Prints out the msg if the file is valid:
            if (user_input.lower() != 'q' and user_input.lower() != 'quit'):
                print(f"{FILE_1} is a Valid File".center(50, "-"))
                
                # Printing out the File:
                with open(FILE_1) as file:
                    for line in file:
                        print(line.strip())
                print()
            break
    
    # Verifying FILE_2:
    tries = 0
    while (user_input.lower() != 'q' and user_input.lower() != 'quit'):
        # Ensure FILE_2 is a valid file in the directory:
        while(not validate_file(FILE_2) and (user_input.lower() != 'q' and user_input.lower() != 'quit')):
            # Error Msg:
            if (tries >= 1):
                print("Invalid Filename. Please try Again".center(50, "-"))
                print()
                
            # User user_Input:
            FILE_2 = input("Enter a Filename to be compared against {FILE_1} (Q/Quit to Exit Program):\n>> ").strip()
            user_input = FILE_2
            tries += 1
        else:
            # Prints out the msg if the file is valid:
            if (user_input.lower() != 'q' and user_input.lower() != 'quit'):
                print(f"{FILE_2} is a Valid File".center(50, "-"))
                
                # Printing out the File:
                with open(FILE_1) as file:
                    for line in file:
                        print(line.strip())
                print()
            break
    
    # Compares the files:
    if (user_input.lower() != 'q' and user_input.lower() != 'quit'):
        if (compare_files(FILE_1, FILE_2)):
            print(f"'{FILE_1}' and '{FILE_2}' are the same file.\n")
        else:
            print(f"'{FILE_1}' and '{FILE_2}' are the are different files.\n")
    else:
        print("End of the Program.....")
    
