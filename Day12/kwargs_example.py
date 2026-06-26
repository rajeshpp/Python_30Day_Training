def show_details(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("User Details:")
show_details(name="Alice", age=30, city="New York", profession="Engineer")
print("*" * 20)
show_details(name="Bob", age=25, city="Los Angeles", profession="Designer", hobby="Photography")
print("*" * 20)
show_details(name="Charlie", age=35, city="Chicago", profession="Teacher", hobby="Reading", language="English")
print("*" * 20)
show_details(name="David", age=28, city="San Francisco", profession="Developer", hobby="Gaming", language="Spanish", country="USA")