# Read text from a given file, return the text to a list.

def text_read(filename):
    text = []
    with open(filename, 'r') as f:
        temp = f.readline()
        while temp != '':
            text.append(temp)
            temp = f.readline()
    return text

# Write the text in a list to a file. If the file under the given filename doesn't exist, create it.

def text_write(filename, text):
    with open(filename, 'w+') as f:
        for temp in text:
            f.write(temp)
    if f.closed is True:
        return True
    return False
