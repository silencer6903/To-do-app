FILE_PATH = "save_data.txt"

def get_todo(filepath=FILE_PATH):
    with open(filepath, 'r', encoding='utf-8') as save:
        return save.readlines()

def do_todo(lst, filepath=FILE_PATH):
    with open(filepath, 'w', encoding='utf-8') as write:
        write.writelines(lst)

def read_line(filepath=FILE_PATH):
    with open(filepath, 'r', encoding='utf-8') as save:
        return save.read()


if __name__ == "__main__":
    print("hello")