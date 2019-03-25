def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Exception: Age cannot be 0 or less")
    return 10/age


try:
    calculate_xfactor(0)
except Exception as err:
    print(err)
