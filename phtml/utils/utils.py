import os

def etc_path():
    current_path = os.getcwd().split('/')
    for i in range(len(current_path)):
        if not i:
            path = '/'.join(current_path)
        else:
            path = '/'.join(current_path[:-i])
        # if phtml

