# returning simple value.

def get_formatted_name(first_name, last_name):
    """return a fumll name, neatly  formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("Rohit", "Patil")
print(musician)
