import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    sum = 0
    y = 0
    k = json.loads(file_path)
    for i in k.values() :
        y = y + 1
        sum = sum + i


        

    return sum/y
    

f = open('data.json', 'r')
x = f.read()
print(average_expenses(x))

