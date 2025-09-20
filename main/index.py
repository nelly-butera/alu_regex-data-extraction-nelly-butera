from regex_validators import *

sample_text = """
Alice Smith, an AI researcher, sent an email to her colleague at alice.smith+work@example.co.uk yesterday, 
while her assistant's address bob_jones@sub.domain.com bounced due to a typo. She also updated the project 
website at https://www.test-site.org/path/to/page, though an old URL http://example.com still redirected visitors. 
In case of urgent matters, the team can call her office at (555) 123-4567 or her mobile 555-987-6543. 

During the last meeting, Alice presented credit card transactions: 1111-2222-3333-4444, and noted that 
another card 5555 6666 7777 8888 had expired. She reminded the finance team that unusual amounts like $12,345.67 
or $0.99 needed verification. The next meeting was scheduled at 23:15, but someone mistakenly suggested 25:00, 
which obviously was incorrect. 

The web development team also discussed HTML changes. They added <h1>Project Launch</h1> to the homepage, 
<a href="http://example.com">linking to resources</a>, and embedded <img src="logo.png" alt="Logo"> for branding. 
On social media, hashtags #DataScience, #AI2025, and #python_rocks were trending, though someone accidentally 
used #Invalid-Hashtag which broke the campaign analytics.

Overall, the day was productive: emails sent, URLs updated, phones answered, credit cards checked, 
times scheduled, HTML verified, hashtags tracked, and currency transactions reviewed — all in one complex, 
real-world scenario that ensures regex patterns extract relevant data correctly.
"""

# Helper function to print results neatly
def pretty_print(label, items):
    print(f"\n{label} ({len(items)} found):")
    for i, item in enumerate(items, 1):
        print(f"  {i}. {item}")

# Extract all data
emails = extract_emails(sample_text)
urls = extract_urls(sample_text)
phones = extract_phones(sample_text)
credit_cards = extract_credit_cards(sample_text)
times = extract_times(sample_text)
html_tags = extract_html_tags(sample_text)
hashtags = extract_hashtags(sample_text)
currency = extract_currency(sample_text)

# Print nicely
pretty_print("Emails", emails)
pretty_print("URLs", urls)
pretty_print("Phones", phones)
pretty_print("Credit Cards", credit_cards)
pretty_print("Times", times)
pretty_print("HTML Tags", html_tags)
pretty_print("Hashtags", hashtags)
pretty_print("Currency Amounts", currency)
