import re

# Email Validator
def extract_emails(text: str) -> list:
    # Grab all emails in the text. Handles things like alice.smith+work@example.com
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)


# URL Validator
def extract_urls(text: str) -> list:
    # Pull out URLs that start with http or https, with optional www and paths
    pattern = r'https?://(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?'
    return re.findall(pattern, text)


# Phone Number Validator
def extract_phones(text: str) -> list:
    # Catch US phone numbers: (123) 456-7890, 123-456-7890, 123.456.7890
    # Non-capturing group (?: ) so findall doesn't return just the first part
    pattern = r'(?:\(\d{3}\)\s|\d{3}[-.])\d{3}[-.]\d{4}'
    return re.findall(pattern, text)


# Credit Card Validator
def extract_credit_cards(text: str) -> list:
    # Grab credit cards like 1234-5678-9012-3456 or 1234 5678 9012 3456
    # Using finditer so we can get the full match (otherwise findall returns only the separator
    pattern = r'\d{4}([- ])\d{4}\1\d{4}\1\d{4}'
    return [m.group(0) for m in re.finditer(pattern, text)]


# Time Validator (12hr & 24hr)
def extract_times(text: str) -> list:
    # Find times like 14:30, 2:30 PM, or 08:05 am
    # Optional AM/PM included
    pattern = r'([01]?\d|2[0-3]):[0-5]\d\s?(?:AM|PM|am|pm)?'
    return re.findall(pattern, text)


# HTML Tag Validator
def extract_html_tags(text: str) -> list:
    # Grab any HTML tags. Works for <p>, <div class="example">, <img ...>
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)


# Hashtag Validator
def extract_hashtags(text: str) -> list:
    # Pull hashtags like #Python or #AI2025
    # Won't match stuff with invalid characters like #Invalid-Hashtag
    pattern = r'#\w+'
    return re.findall(pattern, text)


# Currency Validator
def extract_currency(text: str) -> list:
    # Grab $ amounts like $19.99, $1,234.56, or $100
    # Handles commas in thousands and optional decimals
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)
