from CONSTANTS import *
file_name = 'data/try/try.txt'
os.mkdir('data/try')
some_str = 'hello'
with open(file_name, 'wb') as fileObject:
    pickle.dump(some_str, fileObject)