#exercise4
#Exercise 4: Remove first n characters from a string
#write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_characters(input_string, n):
    # check if n is a number
    if not n.isdigit():
        return "Invalid value of n, please enter a valid positive integer."

    n = int(n)
    
    if n < 0 or n >= len(input_string):
        return "Invalid value of n, out of range."

    # Remove characters 0 up to n
    new_string = input_string[n:]

    return new_string

#user-interface
input_word = input("Type a word: ")
input_number = input("Type a number: ")

# result
result = remove_characters(input_word, input_number)
print(f"Original String: {input_word}")
print(f"New String after removing characters from 0 to {input_number}: {result}")