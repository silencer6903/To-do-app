

def get_todo():
    with open("save_data.txt", 'r', encoding='utf-8') as save:
        return save.readlines()

def do_todo(lst):
    with open("save_data.txt", 'w', encoding='utf-8') as write:
        write.writelines(lst)


if __name__ == "__main__":
    print("hello")