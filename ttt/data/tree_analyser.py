import json

def load_tree_data():
    with open('./tree_data.json', 'r') as f:
        data = json.load(f)
        data = json.loads(data)

    f.close()

    return(data)
