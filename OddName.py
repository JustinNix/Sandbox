"""Justin Nix"""
valid_input = False
while not valid_input:
    try:
        name = input("what is your name: ")
        valid_input = True
        if not name:
            raise ValueError("Empty String")
    except ValueError:
        print("invalid - blank")
print(name)