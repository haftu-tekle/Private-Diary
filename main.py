def display_menu():
    print('\n Personal Diary application')
    print('1 New diary')
    print('2 My diaries')
    print('3 Search by keyword')
    print('4 Delete diary')
    print('5 Exit')

def add_entry(entries):
    date=input('Enter the date YYYY-MM-DD:')
    content=input('Enter what you want to write about:')
    entry={'date':date, 'content':content}
    entries.append(entry)
    print('Your entry has been sucessfully added')