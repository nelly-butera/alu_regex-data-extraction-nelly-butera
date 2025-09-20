from regex_validators import *

sample_text = """
Dr. Evelyn Parker emailed evelyn.parker.research@innovation-lab.org and cc'd john_doe+updates@techhub.io. 
An invalid email jane..smith@badmail..com bounced.

Docs moved to https://docs.innovation-lab.org/releases/v2/index.html, but old http://legacy-site kept redirecting. 
An ftp://backup.server.com link was flagged as unsupported.

Calls came through on (800) 321-6549 and 800-654-3210 (valid), but 800.3216.549 was ignored.

Finance logs showed 1234-5678-9012-3456 and 9876 5432 1098 7654 (valid cards), 
while 1234-5678-9012 was too short. Transactions included $1,500.00, $0.50, $250,000.99, 
and an invalid $3000.5.

Meetings were at 09:00 AM, 14:30, and 11:59 PM. Invalid proposals 26:00 and 12:75 were flagged.

Frontend changes added <header>Welcome</header>, <article class="news">News</article>, 
and <img src="banner.png" alt="Banner">. Even <unknownTag> was spotted.

Hashtags included #InnovationLab, #AI_Future, #123Wins (valid), and #Oops-WrongTag (invalid).
"""

# Helper function to print results neatly
def beautify(label, items):
    print(f"\n{label} ({len(items)} found):")
    for i, item in enumerate(items, 1):
        print(f"  -> {item}")

# Extract all data
emails = extract_emails(sample_text)
urls = extract_urls(sample_text)
phones = extract_phones(sample_text)
credit_cards = extract_credit_cards(sample_text)
times = extract_times(sample_text)
html_tags = extract_html_tags(sample_text)
hashtags = extract_hashtags(sample_text)
currency = extract_currency(sample_text)


# Time extraction with validation for valid/invalid times
# Grabing all HH:MM patterns including optional AM/PM
all_times = re.findall(r'\b\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)?\b', sample_text)

# Separating valid vs invalid times
valid_times = []
invalid_times = []

for t in all_times:
    t_clean = t.upper().replace("AM", "").replace("PM", "").strip()
    hour, minute = map(int, t_clean.split(":"))
    if 0 <= hour <= 23 and 0 <= minute <= 59:
        valid_times.append(t)
    else:
        invalid_times.append(t)


# Validating emails (simple edge cases)
valid_emails = []
invalid_emails = []
for e in emails:
    # checking for double dots in domain or username
    if ".." in e:
        invalid_emails.append(e)
    else:
        valid_emails.append(e)


# my heading
print("\n\n__________________________________________\n")
print("   This Is My Regex Validation System")
print("__________________________________________\n")

# my pretty print functions
beautify("Valid Emails", valid_emails)
beautify("Invalid Emails", invalid_emails)
beautify("URLs", urls)
beautify("Phones", phones)
beautify("Credit Cards", credit_cards)
beautify("Valid Times (12-hour format)", valid_times)
beautify("Invalid Times", invalid_times)
beautify("HTML Tags", html_tags)
beautify("Hashtags", hashtags)
beautify("Currency Amounts", currency)

print("\n")