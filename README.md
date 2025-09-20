### Regex Extractor

```bash
A simple Python project for extracting common patterns (emails, URLs, phone numbers, credit cards, times, HTML tags, hashtags, and currency amounts) using regular expressions.
```

### Project Structure

```bash
regex-extractor/
├─ main/
│ ├─ regex_validators.py
│ └─ index.py
├─ README.md
```

### Features
```bash
- **Email Extraction** → Finds valid email addresses (supports subdomains and `+` addressing).
- **URL Extraction** → Captures HTTP/HTTPS URLs with optional paths.
- **Phone Extraction** → Handles formats like `(123) 456-7890` and `123-456-7890`.
- **Credit Card Extraction** → Captures 16-digit card numbers (both hyphen and space separated).
- **Time Extraction** → Supports 12-hour (`02:30 PM`) and 24-hour (`23:15`) formats.
- **HTML Tag Extraction** → Finds all HTML tags (with or without attributes).
- **Hashtag Extraction** → Captures hashtags containing letters/numbers/underscores.
- **Currency Extraction** → Matches amounts like `$12,345.67`, `$0.99`, `$100`.

```

### Installation

```bash
git clone https://github.com/nelly-butera/regex-extractor.git
cd regex-extractor

```

### Sample Input

```bash
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

```

### Sample Output

```bash
Emails (2 found):
  1. evelyn.parker.research@innovation-lab.org
  2. john_doe+updates@techhub.io

URLs (2 found):
  1. https://docs.innovation-lab.org/releases/v2/index.html
  2. http://legacy-site

Phones (2 found):
  1. (800) 321-6549
  2. 800-654-3210

Credit Cards (2 found):
  1. 1234-5678-9012-3456
  2. 9876 5432 1098 7654

Times (3 found):
  1. 09:00 AM
  2. 14:30 (24-hour)
  3. 11:59 PM

HTML Tags (4 found):
  1. <header>Welcome</header>
  2. <article class="news">News</article>
  3. <img src="banner.png" alt="Banner">
  4. <unknownTag>

Hashtags (3 found):
  1. #InnovationLab
  2. #AI_Future
  3. #123Wins

Currency Amounts (3 found):
  1. $1,500.00
  2. $0.50
  3. $250,000.99

```

### Running the Script

```bash
python src/main.py

```