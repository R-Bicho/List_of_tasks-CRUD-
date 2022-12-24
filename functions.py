tasks: list[str] = []
deleted_itens: list[str] = []


def view():
    '''Show for user the tasks'''

    if len(tasks) == 0:
        print("Don't have any values yet")
    else:
        print(tasks)


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
