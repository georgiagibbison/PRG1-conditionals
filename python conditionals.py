def check_temperature(temp):
    """Simple if/else - good for beginners to read and understand"""
    if temp > 25:
        return "It's warm today!"
    else:
        return "It's cool today!"
print(check_temperature(45))