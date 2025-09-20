import re

# Email Validator
def extract_emails(text: str) -> list:
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


# URL Validator
def extract_urls(text: str) -> list:
    pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
    return re.findall(pattern, text)


# Phone Number Validator
def extract_phones(text: str) -> list:
    pattern = r'(?:\(\d{3}\)\s|\d{3}[-.])\d{3}[-.]\d{4}'
    return re.findall(pattern, text)


# Credit Card Validator
def extract_credit_cards(text: str) -> list:
    pattern = r'\d{4}([- ])\d{4}\1\d{4}\1\d{4}'
    return re.findall(pattern, text)


# Time Validator (12hr & 24hr)
def extract_times(text: str) -> list:
    pattern = r'([01]?\d|2[0-3]):[0-5]\d\s?(?:AM|PM|am|pm)?'
    return re.findall(pattern, text)


# HTML Tag Validator
def extract_html_tags(text: str) -> list:
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)


# Hashtag Validator
def extract_hashtags(text: str) -> list:
    pattern = r'#\w+'
    return re.findall(pattern, text)


# Currency Validator
def extract_currency(text: str) -> list:
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)
