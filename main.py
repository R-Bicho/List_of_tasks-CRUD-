from functions import add, remove, undo, view

while True:
    value = input('digite view, add, remove or undo: ')

    if value == 'add':
        task = input('digite o valor: ')
        add(task)

    if value == 'view':
        view()
    elif value == 'remove':
        remove()
    elif value == 'undo':
        undo()
