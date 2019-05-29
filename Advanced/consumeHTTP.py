# Your challenge is to consume a streaming HTTP feed and assemble a password. The feed is located at SOURCE_URL (hidden for privacy) and accessible via GET requests.

# This endpoint will return chunks of content that you need to decode. Below is an example:

# 4
# [5, 6]
# RXIBDRBF
# DVMPXTBG
# BMWAERXR
# UPEIJGMZ
# YTALDXDH
# JNPMOUEJ
# XDRHCHWG

# Each chunk reveals a character in the password and can be decoded as follows:

# The first line in the chunk corresponds to the index of character in the password (0 indexed).
# The second line is the [X, Y] coordinates of the password character in the matrix ([0, 0] is the bottom left character).
# The remaining lines contain a matrix of random characters, with a password character located at the coordinates from line 2.
# So, in the example above, we're looking for a character at the coordinates [5, 6]. Moving right 5 spaces, and up 6, we find the character R. So, R is the character at index 4 (again, 0 indexed) in the password.

# Continue processing chunks until you've found all the characters in the password.

# Additional details:
# Passwords are of arbitrary length and may contain letters or numbers.
# Once all characters from the password have been exhausted and returned in a chunk, new chunks will be generated for each character and returned in a random order.

import requests

r = requests.get('SOURCE_URL', stream=True)

# Choosing a reasonable size for the password
# Try to improve this code by removing this limitation
password = [None] * 50
max_index = 49


def processChunk(chunk):
    # Sample chunk
    # chunk = b'8\n[7, 16]\nYKJMXGXJBZVDVPVNY\nUAFUEETDYORRFCCWE\nQMRTMWFMXLSNOBXXC\nKCUCSXEOPTBRCXEDX\nVTNCEGEYNSKHVAOFZ\nRKRNRYWJVXIUWLQUX\nVMCKWWCCHKSTVDQIX\nZYOSIQXAKMVHUKZDL\nKPXKLGGMKWOKUWNUR\nBSQUWCPWIOWGYFTCP\nEQUBYKZFFOZHPSUTH\nQCLDUROXRPSEXDKWI\nFKKBZXJHOJZUKMUMI\nWPWWATJUJPXWFRWKC\nTKXPHQLNVPSJEAJOL\nBKIBMYPDJSBDEYFOW\nQEYOZYZKHULGAWWRO\nSKTZVQJLYWJYDOFQI\n\n'
    # b'15\n[0, 0]\nLPQXGZOYVJHWVZHEGIWXF\n\n'

    # convert to ASCII
    str_chunk = chunk.decode('ASCII')

    lines = str_chunk.splitlines()

    # Remove the last empty line
    lines = lines[:-1]
    len_lines = len(lines)

    list_index = int(lines[0])
    coordinates = lines[1]
    coordinates = coordinates.replace("[", "")
    coordinates = coordinates.replace("]", "")

    x = int(coordinates.split(",")[0])
    y = int(coordinates.split(",")[1])

    y_from_top = len_lines - 2 - y + 1
    # print(x)
    # print(y_from_top)

    character = lines[y_from_top][x]

    if list_index > max_index:
        raise IndexError("Maximum password length is 50")
    elif password[list_index] == None:
        password[list_index] = character
        return True
    else:
        # An element already exists at index: Password has been formed
        return False


for chunk in r.raw.read_chunked():
    try:
        if (processChunk(chunk) == False):
            # Remove all None
            password = list(filter(lambda x: x != None, password))
            str_password = "".join(password)
            print(str_password)
            break
        else
        pass  # Keep processing
    except Exception as error:
        print(error)
        quit()
