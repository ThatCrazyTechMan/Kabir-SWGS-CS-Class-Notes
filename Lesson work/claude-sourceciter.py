from dataclasses import dataclass, field
from typing import Optional
from datetime import date
from enum import Enum

class SourceType(Enum):
    JOURNAL = "journal"
    NEWS = "news"
    ARCHIVED = "archived"

@dataclass
class CitationSource:
    # Universal fields
    authors: list[str]                        # ["Smith, J.", "Jones, A."]
    title: str
    year: int
    source_type: SourceType

    # Partial/full date support
    month: Optional[int] = None
    day: Optional[int] = None

    # Journal-specific
    journal_name: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    doi: Optional[str] = None

    # News-specific
    publication_name: Optional[str] = None
    url: Optional[str] = None
    accessed: Optional[date] = None           # date object for access date

    # Archive.org-specific
    archive_url: Optional[str] = None
    archive_date: Optional[date] = None       # when it was archived


def _format_authors(authors: list[str]) -> str:
    if len(authors) == 1:
        return authors[0]
    elif len(authors) <= 3:
        return ", ".join(authors[:-1]) + " and " + authors[-1]
    else:
        return authors[0] + " et al."


def _format_date(year: int, month: Optional[int], day: Optional[int]) -> str:
    if day and month:
        return f"{year}, {day} {date(year, month, day).strftime('%B')}"
    elif month:
        return f"{year}, {date(year, month, 1).strftime('%B')}"
    else:
        return str(year)


def createCitation(source: CitationSource) -> str:
    author_str = _format_authors(source.authors)
    date_str = _format_date(source.year, source.month, source.day)

    if source.source_type == SourceType.JOURNAL:
        citation = f"{author_str} ({date_str}) '{source.title}', {source.journal_name}"
        if source.volume:
            citation += f", {source.volume}"
        if source.issue:
            citation += f"({source.issue})"
        if source.pages:
            citation += f", pp. {source.pages}"
        if source.doi:
            citation += f". doi:{source.doi}"

    elif source.source_type == SourceType.NEWS:
        citation = f"{author_str} ({date_str}) '{source.title}', {source.publication_name}"
        if source.url:
            accessed_str = source.accessed.strftime("%-d %B %Y") if source.accessed else "n.d."
            citation += f". Available at: {source.url} (Accessed: {accessed_str})"

    elif source.source_type == SourceType.ARCHIVED:
        citation = f"{author_str} ({date_str}) '{source.title}'"
        if source.publication_name:
            citation += f", {source.publication_name}"
        if source.url:
            citation += f". Originally available at: {source.url}"
        if source.archive_url and source.archive_date:
            archive_str = source.archive_date.strftime("%-d %B %Y")
            citation += f". Archived at: {source.archive_url} (Archived: {archive_str})"

    return citation + "."



author = input('Who wrote the article: ')
title = input('What is the article called: ')
organisation = input('What is the organisation: ')
date_written = input('What is the date written: ')
url = input('What is the url: ')
archive_url = input('What is the archive url: ')

print(createCitation(

))