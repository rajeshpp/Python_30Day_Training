def display(name, city="Hyderabad", *args, **kwargs):
    print(f"Name: {name}")
    print(f"City: {city}")
    
    if args:
        print("Additional positional arguments:")
        for arg in args:
            print(arg)
    
    if kwargs:
        print("Additional keyword arguments:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")

display("Venkat",
        "Bangalore",

        "Engineer", "Male", "Married", "Hobbies: Reading, Traveling", "Country: India",

        age=25, company="XYZ"
)