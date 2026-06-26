x = "Global"

def outer():
    print(x)
    x = "In Outer Function"
    print(x)

    def inner():
        print(x)
        x = "In Inner Function"
        print(x)

    inner()

outer()
