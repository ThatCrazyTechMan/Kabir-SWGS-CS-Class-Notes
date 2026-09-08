import datetime
import pyperclip


def get_year_written(date_written):
    """Extract the last 4 characters of a date string as the year."""
    return date_written[-4:]


def createCitation_archived(author, title, organisation, date_written, url,
                             archive_url, archive_date, today):
    return (f"{author} ({get_year_written(date_written)}) '{title}' {organisation} "
            f"({date_written}) [Online] Originally Available at: {url}, "
            f"archived at: {archive_url} on {archive_date} (Accessed: {today})")


def createCitation_unarchived(author, title, organisation, date_written, url, today):
    return (f"{author} ({get_year_written(date_written)}) '{title}' {organisation} "
            f"({date_written}) [Online] Originally Available at: {url} (Accessed: {today})")


def createCitation_journal(author, title, journal, journal_year, journal_volume,
                            journal_section, pages, link, today):
    no_of_pages = abs(eval(pages))
    return (f"{author} '{title}' {journal}, ({journal_year}) Vol. {journal_volume}, "
            f"Section {journal_section}, pp: {pages} ({no_of_pages} pages) available at {link} (Accessed: {today})")


def ask_yes_no(prompt):
    """Keep asking until the user gives a recognisable yes/no answer."""
    while True:
        answer = input(prompt).strip().upper()
        if answer in ('Y', 'YES'):
            return True
        if answer in ('N', 'NO'):
            return False
        print("Please answer Yes or No (y/n).")


def main():
    author = input('Who wrote the article: ')
    title = input('What is the article called: ')
    url = input('What is the url: ')

    publication_type = input('Is this a (J)ournal or a (N)ews article? ').strip().upper()

    if publication_type == 'J':
        today = datetime.datetime.now().strftime('%d/%m/%Y')
        journal = input('What is the journal called: ')
        journal_year = input('What is the journal year: ')
        journal_volume = input('What is the journal volume: ')
        journal_section = input('What is the journal section: ')
        pages = input('What are the journal pages: ')
        citation = createCitation_journal(author, title, journal, journal_year,
                                           journal_volume, journal_section, pages, url, today)
    else:
        is_current = ask_yes_no('Is the article current? (Yes/No): ')
        today = datetime.datetime.now().strftime('%d/%m/%Y')

        organisation = input('What is the organisation: ')
        date_written = input('What is the date written: ')

        if not is_current:
            archive_url = input('What is the archive url: ')
            archive_date = input('What is the archive date: ')
            citation = createCitation_archived(author, title, organisation, date_written,
                                                url, archive_url, archive_date, today)
        else:
            citation = createCitation_unarchived(author, title, organisation,
                                                  date_written, url, today)

    print(citation)
    pyperclip.copy(citation)
    print('Citation copied!')


if __name__ == '__main__':
    main()
