import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    sum = 0
    y = json.loads(file_path)
    for i in y.values():
        sum = sum + i
    return sum

    
f = open('data.json','r')
x = f.read()
print(total_expenses(x))


