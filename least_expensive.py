import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    k = json.loads(file_path)
    x = k.values()
    x = list(x)
    print(x)
    y = x[0]

    for i in k.values():
        if i<y :
            y=i

    
    return y




f = open('data.json','r')
x = f.read()
print(least_expensive(x))