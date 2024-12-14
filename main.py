from Modules.todo_m import get_todo, do_todo


def todo():
    while True:
        menu = input("Select your option: add, show, edit, complete, exit: ")
        match menu:
            case str() as c if c.startswith('add'):
                todo = get_todo()
                todo.append(c[4:] + '\n')

                do_todo(todo)

            case str() as c if c.startswith('show'):
                with open("save_data.txt", 'r', encoding='utf-8') as show:
                    for index, line in enumerate(show, 1):
                        print(f"{index}) {line}", end='')


            case str() as c if c.startswith('edit'):
                try:
                    complied = int(input("Enter number: "))
                    todo = [*map(str.strip, get_todo())]

                    ch = input("Enter edit: ")
                    if len(todo) >= complied:
                        todo[complied-1] = ch

                    with open("save_data.txt", 'w', encoding='utf-8') as r_change:
                        r_change.write('\n'.join(todo))
                except Exception:
                    print("Enter integer type")

            case str() as c if c.startswith('complete'):
                try:
                    complied = int(input("Enter number: "))
                    todo = get_todo()

                    print(f"You complete this: {todo.pop(complied-1)}")

                    do_todo(todo)

                except IndexError:
                    print("Not valid number")

            case str() as c if c.startswith('exit'):
                print('Bye!')
                break

            case _:
                print("You write wrong type symbols. Use only please a-z chars")
todo()
