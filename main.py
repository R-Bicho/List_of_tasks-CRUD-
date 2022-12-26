from functions import add, remove, undo, update, view

while True:
    value = input('Write view, add, remove, update, undo or leave: ').lower()

    if value != 'view' and value != 'add' and value != 'update'\
            and value != 'remove' and value != 'undo' and value != 'leave':
        print('You need write "view", "add", "remove", "undo" or "leave"')

    if value == 'add':
        task = input('Write one task: ')
        add(task)

    if value == 'update':
        update_index = input('Write index what you like change: ')

        if not update_index.isnumeric():
            raise ValueError('Invalid value, you need write int value')

        update(int(update_index))

    if value == 'view':
        view()
    elif value == 'remove':
        remove()
    elif value == 'undo':
        undo()
    elif value == 'leave':
        print('End of the program')
        break
