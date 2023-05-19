import json

def get_data(file_path: str) -> dict:
    """
    get data from json file as dictionary
    
    Args:
        file_path (str): path to json file

    Returns:
        dict: dictionary of data
    """
    y = json.loads(file_path)
    return y



f = open('data.json','r')
x = f.read()
print(get_data(x))