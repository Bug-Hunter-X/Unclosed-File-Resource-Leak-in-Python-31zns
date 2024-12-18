def function_with_unclosed_file(filename):
    f = open(filename, 'w')
    # ... some code that might raise an exception ...
    f.close() #This line is important

# Example call
function_with_unclosed_file('my_file.txt')