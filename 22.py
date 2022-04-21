import string
from tqdm import tqdm

letters = string.ascii_lowercase + " "
def compare(name1, name2):
    """Compares two names to help sorting by alphabetical order

    Args:
        name1 (str): First name
        name2 (str): Second name
    
    Returns:
        inOrder (bool): if the names are already in order
    """
    name1 = name1.lower()
    name2 = name2.lower()
    inOrder = True
    for i in range(min(len(name1), len(name2))):
        
        
    

def sort(liste):
    end = 0
    for i in tqdm(range(len(liste))):
        for j in range(0, len(liste) - end):
            try:
                compare
        end += 1
    return liste
                    

with open('files\p022_names.txt', 'r') as f:
    names = f.read().replace("\"", "").split(",")

namedict = {}
for i in range(len(names)):
    pass

print(names)