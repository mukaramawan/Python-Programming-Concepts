# You must manually check types → if type(...) == ....
# You must manually raise errors for invalid inputs.
# Not scalable.
# No automatic type conversion (e.g., "25" won’t become 25).

def insert_patient(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative!")
        else:
            print(name)
            print(age)
    else:
        raise TypeError("Incorrect Datatype!")
    print("Inserted Data into the database!")

insert_patient('Name', 'thirty')

def update_patient(name: str, age: int):
    if type(name) == str and type(age) == int:
        if age < 0:
            raise ValueError("Age can't be negative!")
        else:
            print(name)
            print(age)
    else:
        raise TypeError("Incorrect Datatype!")
    print("Updated!")
