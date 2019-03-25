try:
    with open("exercise2_repeat3.py") as file:
        print("File opened:", file.name)
except Exception as e:
    print(e)
finally:
    print("Program terminated gracefully")
    file.close()  # redundant
