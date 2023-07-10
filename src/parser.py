"""
"""
import json

def walk(node):
    for key, item in node.items():
        if isinstance(item, dict):
            walk(item)
        else:
            print(key, item)

if __name__ == '__main__':
    with open('result.json') as file:
        node = json.load(file)
    walk(node)
