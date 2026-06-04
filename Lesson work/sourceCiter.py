import datetime
from datetime import date
import pyperclip
def createCitation_archived(author, title, organisation, date_written, url, archive_url, archive_date):
    citation = str(f"{author} ({get_year_written(date_written)}) '{title}' {organisation} ({date_written}) [Online] Originally Available at: {url}, archived at: {archive_url} on {archive_date} (Accessed: {today})")
    return citation

def createCitation_unarchived(author, title, organisation, date_written, url):
    citation = str(f"{author} ({get_year_written(date_written)}) '{title}' {organisation} ({date_written}) [Online] Originally Available at: {url} (Accessed: {today})")
    return citation

def createCitation_journal(author, title, journal, journal_year, journal_volume, journal_section, pages, link):
    no_of_pages = abs(eval(pages))
    citation = str(f"{author} '{title}' {journal}, ({journal_year}) {journal_volume}, Section {journal_section}, pp: {pages} ({no_of_pages} available at {link}")
    return citation
author = input('Who wrote the article: ')
title = input('What is the article called: ')
url = input('What is the url: ')

publication_type = input('Is this a (J)ournal or a (N)ews article?').upper()
if publication_type.lower() == 'j':
    journal = input('What is the journal called: ')
    journal_year = input('What is the journal year: ')
    journal_volume = input('What is the journal volume: ')
    journal_section = input('What is the journal section: ')
    pages = input('What are the journal pages: ')
    citation = createCitation_journal(author, title, journal, journal_year, journal_volume, journal_section, pages, url)
    print(citation)
    pyperclip.copy(str(citation))
    print('Citation copied!')
    quit()
else:
    is_current_input = str(input('Is the article current? (Yes/No): '))
    if is_current_input.upper() == 'YES':
        (is_current) = bool(True)
    elif is_current_input.upper() == 'NO':
        (is_current) = bool(False)

    today = datetime.datetime.now().strftime('%d/%m/%Y')


    def get_year_written(date):
        arr = []
        for i in date:
            arr.append(i)
        year_written = ''.join(arr[-4:])
        return year_written

    if not is_current:
        organisation = input('What is the organisation: ')
        date_written = input('What is the date written: ')
        archive_url = input('What is the archive url: ')
        archive_date = input('What is the archive date: ')
        result = createCitation_archived(author, title, organisation, date_written, url, archive_url)
        print(result)
        pyperclip.copy(result)
        print('Citation copied!')

    else:
        organisation = input('What is the organisation: ')
        date_written = input('What is the date written: ')
        result = createCitation_unarchived(author, title, organisation, date_written, url)
        print(result)
        pyperclip.copy(result)
        print('Citation copied!')