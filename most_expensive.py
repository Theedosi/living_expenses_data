import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    max = 0
    y = json.loads(file_path)
    u = y.values()
    for i in u:

        if max<i:
            max = i

    return max

f = open('data.json','r')
x = f.read()
print(most_expensive(x))