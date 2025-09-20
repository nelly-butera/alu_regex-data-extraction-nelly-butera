from regex_validators import *

sample_text = """
Contact: john.doe@example.com or jane_doe@company.org
Visit: https://www.example.com or https://sub.example.org/page
Call: (123) 456-7890 or 123-456-7890
Credit: 1234 5678 9012 3456
Time: 14:30 or 2:30 PM
HTML: <p>Hello</p> <div class="example">
Hashtag: #Example #Test123
Currency: $19.99 or $1,234.56
"""

print("Emails:", extract_emails(sample_text))
print("URLs:", extract_urls(sample_text))
print("Phones:", extract_phones(sample_text))
print("Credit Cards:", extract_credit_cards(sample_text))
print("Times:", extract_times(sample_text))
print("HTML Tags:", extract_html_tags(sample_text))
print("Hashtags:", extract_hashtags(sample_text))
print("Currency Amounts:", extract_currency(sample_text))
