# read a line from STDIN
# my_string = input()
# print(my_string)


def read_lines_from_stdin(number_of_lines_to_read):
    """
    Function for reading lines in a standard input and returning the input as a list.
    Note: If `number_of_lines_to_read` = 0, then use the first line as the number of lines to read
    """
    input_list = []

    # Read from the terminal, the number of lines to read
    # This assumes that it can always be casted to an integer
    if number_of_lines_to_read == 0:
        number_of_lines_to_read = int(input())

    # For every line, remove the extra spaces and append it to the list
    for _ in range(number_of_lines_to_read):
        line_input = input()
        input_list.append(line_input)
    return input_list


# Example
# print(read_lines_from_stdin(2))
# print(read_lines_from_stdin(0))
