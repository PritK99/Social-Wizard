import re

def extract_python_list(string):
    # Define a regular expression pattern to match Python lists
    pattern = r'\[.*?\]'

    # Use re.findall to find all matches of the pattern in the string
    matches = re.findall(pattern, string)

    # If there are matches, return the first one
    if matches:
        return matches[0]
    else:
        return None

if __name__ == '__main__':
    input_string = "This is a string with a Python list: [1, 2, 3, hello , world ]"
    python_list = extract_python_list(input_string)
    if python_list:
        print("Extracted Python list:", python_list)
    else:
        print("No Python list found in the input string.")
