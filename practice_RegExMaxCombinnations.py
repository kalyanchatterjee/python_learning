# https://www.hackerrank.com/challenges/count-strings/problem


def countStrings(r, l):
    # First step is to get the RegEx patterns
    strProvidedPattern = r
    pattern_tuple = tuple(strProvidedPattern)

    parenthesis_stack = []
    patterns = []
    currentPattern = []
    # Push each element to a stack to find '(' and ')' pairs
    for char in pattern_tuple:
        if char == '(':
            if parenthesis_stack:
                if parenthesis_stack[0] == '(':
                    currentPattern = []
                    currentPattern.append(char)
                else:
                    parenthesis_stack.append(char)
            else:
                parenthesis_stack.append(char)
        elif char == ')':
            if currentPattern[0] == '(':
                currentPattern.append(char)
                print(currentPattern)
                patterns.append(str(currentPattern))
            else:
                # Reached end of string
                any
        else:
            currentPattern.append(char)

    for item in patterns:
        print(str(patterns[item]))


if __name__ == "__main__":
    countStrings("((a*)(b(a*)))", 100)
