# Consume data from HTTP stream https://enigmatic-plains-7414.herokuapp.com
import requests

r = requests.get('https://enigmatic-plains-7414.herokuapp.com', stream=True)
# print(r.status_code)
# print(r.raw.__dir__())

password = []


def processChunk(chunk):
    try:
        str_chunk = chunk.decode('ASCII')
        # print(str_chunk)

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

        if len(password) == 0:
            password.append(character)
        else if password[list_index] my

        if password[list_index] != None:
            password.insert(list_index, character)
            return True
        else:
            return False
    except Exception as error:
        print(error)
    finally


# chunk = b'8\n[7, 16]\nYKJMXGXJBZVDVPVNY\nUAFUEETDYORRFCCWE\nQMRTMWFMXLSNOBXXC\nKCUCSXEOPTBRCXEDX\nVTNCEGEYNSKHVAOFZ\nRKRNRYWJVXIUWLQUX\nVMCKWWCCHKSTVDQIX\nZYOSIQXAKMVHUKZDL\nKPXKLGGMKWOKUWNUR\nBSQUWCPWIOWGYFTCP\nEQUBYKZFFOZHPSUTH\nQCLDUROXRPSEXDKWI\nFKKBZXJHOJZUKMUMI\nWPWWATJUJPXWFRWKC\nTKXPHQLNVPSJEAJOL\nBKIBMYPDJSBDEYFOW\nQEYOZYZKHULGAWWRO\nSKTZVQJLYWJYDOFQI\n\n'
# b'15\n[0, 0]\nLPQXGZOYVJHWVZHEGIWXF\n\n'


for chunk in r.raw.read_chunked():
    print(chunk)
    if (processChunk(chunk) == False):
        print(password)

# r.encoding = "ISO-8859-1"
# print(dir(r))

# json_text = r.json()

# print(dir(json_text))

# print(json_text.__sizeof__)
# first_chunk = r.raw.read(300)
# first_chunk.decode("utf-8")

# print(first_chunk)
