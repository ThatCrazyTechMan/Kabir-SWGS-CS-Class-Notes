from datetime import date
import pyperclip

is_current = input('Is the article current? ')
publication_type = input('Is this a (J)ournal or a (N)ews article?')
date_known = input('Is the full date known? ')


def get_year_written(date):
    arr = []
    for i in date:
        arr.append(i)
    year_written = ''.join(arr[-4:])
    return year_written



def createCitation(author, date, url, archive, archive_url, organisation):
    today = date.today().strftime("%d/%m/%Y")
    if archive:
        citation = str(f"{author} ({get_year_written(date)}) '{title}' \x1B[3m{organisation}\x1B[0m ({date_written}) [Online] Originally Available at: {url}, archived at: {archive_url} (Accessed: {today})")
    else:
        citation = str(f"{author} ({get_year_written(date)}) '{title}' \x1B[3m{organisation}\x1B[0m ({date_written}) [Online] Originally Available at: {url} (Accessed: {today})")

    return citation


if is_current:
    author = input('Who wrote the article? ')
    date_written = input('What date was the article written? (DD/MM/YYYY) ')
    title = input('What is the title of the article? ')
    organisation = input('What is the organisation of the author? ')
    url = input('What is the url of the article? ')
else:
    author = input('Who wrote the article? ')
    date_written = input('What date was the article written? (DD/MM/YYYY) ')
    title = input('What is the title of the article? ')
    organisation = input('What is the organisation of the author? ')
    url = input('What is the url of the article? ')




