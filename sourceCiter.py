from datetime import date
import pyperclip

is_current = input('Is the article current? ')
if is_current.lower() == 'yes':
    author = input('Who wrote the article? ')
    date_written = input('What date was the article written? (DD/MM/YYYY) ')
    title = input('What is the title of the article? ')
    organisation = input('What is the organisation of the author? ')

    #year written
    arr = []
    for i in date_written:
        arr.append(i)

    year_written = ''.join(arr[-4:])
    url = input('What is the url of the article? ')
    date = date.today().strftime("%d/%m/%Y")

    print(f"{author} ({year_written}) '{title}' \x1B[3m{organisation}\x1B[0m ({date_written}) [Online] Available at: {url} (Accessed: {date})")
    pyperclip.copy(f"{author} ({year_written}) '{title}', {organisation}, ({date_written}) [Online] Available at: {url} (Accessed: {date})")




