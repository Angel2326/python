import os
def create_dir():
    for i in range(1,9):
        new_path=os.path.join(os.getcwd(),'dir_{}'.format(i))
        os.mkdir(new_path)

def del_dir():
    for i in range(1,9):
        new_path=os.path.join(os.getcwd(),'dir_{}'.format(i))
        os.rmdir(new_path)
create_dir()
del_dir()