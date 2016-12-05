# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].

def find_second(number_list):
        if type(number_list) is not list:
            raise TypeError('The parameter is not a list')
        else:
            return number_list[1::2]


print(find_second([1, 2, 3, 4, 5, 6, 7]))
