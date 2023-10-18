#!/usr/bin/python3
"""append after module"""


# def append_after(filename="", search_string="", new_string=""):
#     """append a text after a substring line"""

#     with open(filename, 'r') as f:
#         content = f.readlines()
#         for (index, line) in enumerate(content):
#             if line.find(search_string) != -1:
#                 content.insert(index+1, new_string)
#         new_content = "".join(content)
#     f = open(filename, 'w')
#     f.write(new_content)
#     f.close()

def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
