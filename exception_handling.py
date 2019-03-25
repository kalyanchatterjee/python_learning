try:
    age = int(input("enter age: "))
    xfactor = age / 0
except (ValueError, ZeroDivisionError) as ex:
    print("Exception:", ex)
else:
    print("no exceptions")
finally:
    print("All good, terminated gracefully")
