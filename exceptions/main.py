def main():
    normal_try_catch_no_raise()
    try:
        try_catch_reraise_exception() # because this actually raises an exception - this will halt the program
    except Exception as e:
        print("Exception happened when calling try_catch_reraise_exception")
        print("continuning to try_catch_exception")
        print(f"error is {e}") # we can wrap the method in a try-catch and print the exception out this way if we want to
        # continue processing
    try_catch_exception() # this halts program exceution
    print(f"THIS WON'T EXECUTE")



def normal_try_catch_no_raise():
    try:
        print(f"within the try block of {normal_try_catch_no_raise.__name__}")
        raise ValueError("raising value error")
    except:
        print(f"Exception hapened")
        print(f"this doesn't stop the program execution though because we're not raising anything")


def try_catch_exception():
    try:
        print(f"within try of {try_catch_exception.__name__}")
        raise ValueError("Raising value error and raising in except block as well")
    except ValueError as e:
        raise # we use bare raise here to keep the stack trace
        # if we did raise ValueError("new error") -> we would lose the stack trace

def try_catch_reraise_exception():
    try:
        raise ValueError("this will get overwritten")
    except Exception:
        raise Exception("Overwriting the origina value error that caused this")



if __name__ == "__main__":
    main()