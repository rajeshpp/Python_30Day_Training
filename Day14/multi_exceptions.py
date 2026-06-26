def sample():
    try:
        num = int(input("Enter a number: "))
        result = 100/num
        return result
    except ValueError:
        print("That was not a valid number!")
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    except:
        print("At last")
    finally:
        print("This always executes")

sample()