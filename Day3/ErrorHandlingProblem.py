def safe_divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Please enter number only!")
    else:
        print(f"Result: {result}")
    finally:
        print("Operation complete!")

safe_divide(10, 2)   # normal
safe_divide(10, 0)   # zero division
safe_divide(10, "a") # type error