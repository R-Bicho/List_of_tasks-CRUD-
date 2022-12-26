tasks: list[str] = []
deleted_itens: list[str] = []


def view():
    '''Show for user the tasks'''

    if len(tasks) == 0:
        return print("Don't have any values yet")

    for index, value in enumerate(tasks):
        print(f'{index}) {value}')


def add(item: str):
    '''adds values to the list'''

    if item.strip() == '':
        print('Need write some value')
    else:
        tasks.append(item)


def remove():
    '''Remove last item to the tasks'''
    if len(tasks) == 0:
        print("Don't have any values for remove")
    else:
        deleted_itens.append(tasks[-1])
        tasks.pop()


def undo():
    if len(deleted_itens) == 0:
        print("Don't have any values for undo")
    else:
        tasks.append(deleted_itens[-1])
        deleted_itens.pop()


def update(value: int):
    '''Update one value in the task list'''

    new_value = input('Write new task: ')

    if new_value.strip == '':
        print('You need write one value')
    else:
        try:
            tasks[value] = new_value
        except IndexError:
            print("This index don't exist")
