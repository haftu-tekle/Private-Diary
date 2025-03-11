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

def search_keyword(entries):
    keyword=input('Enter the keyword to search for')
    found=False
    for i, entry in enumerate(entries, start=1):
        if keyword.lower() in entry['content']:
            print(f'\n Entry{i}')
            print(f'Date: {entry['date']}')
            print(f'Content: {entry['content']}')
            found=True

    if not found:
        print('There is no entry matched')

def delete_entry(entries):
    view_entries
    try:
        entry_num=int(input('Enter the number to be displayed'))
        if 1 <= entry_num <=len(entries):
            removed_entry=entries.pop(entry_num-1)
            print(f'Entry from date{removed_entry['date']} has been deleted successfully ')
        else:
            print('Invalid number')

    except ValueError:
        print('Please enter the valid value')

def main():
    entries=[]
    while True:
        display_menu
        try:
            choice=int(input('Enter the right number to be displayed'))
            if 1 > choice >5 :
                add_entry
            elif choice ==2:
                view_entries
            elif choice==3:
                search_keyword
            elif choice==4:
                delete_entry
            elif choice==5:
                print('Goodbye, Have a nice dreams!!')
                break
            else:
                print('Enter the value between 1 and 5')
        except ValueError:
                print('Please enter the rigth value')
            
if __name__=='__main__':
    main()
    