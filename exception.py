def check_age(age):
    if age<0:
        raise ValueError("age cannot be negative")
    print("valid age")

check_age(-5)