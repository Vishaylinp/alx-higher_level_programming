#!/usr/bin/python3

"""Write a string"""


def write_file(filename="", text=""):
    """Writes a string to a text fil

    Args:
        filename: filename
        text: content
    """
    with open(filename, 'w', encoding="UTF-8") as wr_f:
        return (wr_f.write(text))
