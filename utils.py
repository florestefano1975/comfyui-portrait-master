# Utility functions for Portrait Master

def pmReadTxt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]
        return values

def applyWeight(text, weight):
    if weight == 1:
        return text
    else:
        return f"({text}:{round(weight,2)})"
