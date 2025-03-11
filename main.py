def display_menu():
    print(f'\n Personal Diary application')
    print('1 New diary')
    print('2 My diaries')
    print('3 Search by keyword')
    print('4 Delete diary')
    print('5 Exit')

def add_entry(entries):
    date=input('Enter the date in the following format(YYYY-MM-DD)')
    content=input('Enter the entry of your journal')
    entry={'date':date, 'content':content}
    entries.append(entry)
    print('your journal has been created succesfully')

def view_entries(entries):
    if not entries:
        print('There is on entry found')
    else:
        for i, entry in enumerate(entries, start=1):
            print(f'\n Entry {i}:')
            print(f'date:{entry['date']}')
            print(f'content:{entry['content']}')

def search_entries(entries):
    keyword=input('Enter the keyword of the entry')
    found=False
    for i, entry in enumerate(entries, start=1):
        if keyword.lower() in entry['content'].lower():
            print(f'\ Entry{i}')
            print(f'date:{entry['date']}')
            print(f'content:{entry['content']}')
        else:
            print('There is no entry found')