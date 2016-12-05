# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.
import os.path

def write_text(file_name, get_string):

    if os.path.isfile(file_name) and type(get_string) is str:
        text_file = open(file_name, 'w')
        for i in range(10):
            text_file.write(get_string)
        text_file.close()
        return True
    else:
        return False

print (write_text('text.txt', 'apple'))
