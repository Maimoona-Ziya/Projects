# Projects

Beginner projects by Maimoona Ziya, B.Tech CS (AI & ML) student at QUAD AI School of Technology & Management, Bangalore.

## Offer Analyser (Python)

**File:** `Offer_analyser.py`

### Problem
Fake job and internship offers are common, and students often cannot tell whether an offer is genuine. Scammers also keep changing their wording, so checking for keywords in a message is not reliable. This program looks at the situation instead: it asks the user questions about the offer and the hiring process.

### What it does
- Asks 9 yes/no questions about the offer (payment asked, interview process, email type, pressure to decide, documents requested, company verification and more).
- Adds weighted points for each warning sign. Asking for money or sensitive documents scores highest.
- Prints a risk score out of 16 and a verdict: low risk (0-2), suspicious (3-5) or very likely a scam (6 or more).

### How to run
1. Install Python 3.
2. Download `Offer_analyser.py`.
3. Run `python Offer_analyser.py` in a terminal and answer `y` or `n`.

### Sample outputs
These are real runs. Answers are listed in question order (y = yes, n = no).

Scam-style answers (y y y n y y n y y):
```
Risk score: 11 out of 16
Verdict: Very likely a scam. Do not pay or share documents.
```

Borderline answers (n n y n n n n n y: asked for money and company could not be found):
```
Risk score: 5 out of 16
Verdict: Suspicious. Verify carefully before going further.
```

Genuine-style answers (all n):
```
Risk score: 0 out of 16
Verdict: Low risk. Still verify the company before you accept.
```

### Limits
- The score is an estimate, not proof. A low score does not guarantee an offer is genuine.
- One serious warning sign on its own, such as being asked for money, scores 3 and is not enough to reach the "very likely a scam" verdict.
- Any answer other than `y` is counted as "no", including typos.
- The weights are my own judgement, not taken from research.
- It does not read the actual offer message.
- Always check the company on its official website and LinkedIn page before paying or sharing documents.

### Ideas to improve
- Check that answers are valid before counting them.
- Add a keyword check for pasted offer messages.
- Test the weights on more real examples.

## ATM Machine (Python)

**File:** `ATM_Machine.py`

A mini ATM program written with basic Python concepts only, without any for or while loops. The challenge was to stick to fundamentals and use as few built-in functions as possible.

### What it does
- Asks for a 4-digit PIN and checks that it has exactly 4 digits and that all of them are numbers.
- Offers four options: cash withdrawal, balance enquiry, cash deposit and exit.
- Withdrawal accepts amounts of at least Rs 500 in multiples of 100, and rejects amounts higher than the balance.
- Asks whether the user wants a receipt after each transaction.

### How to run
Run `python ATM_Machine.py` and follow the prompts.

### Limits
- The PIN is only checked for format. It is not compared with a stored PIN, so any 4-digit PIN works.
- The starting balance is a fixed demo value.
- It handles one transaction per run, because it uses no loops.

## Login Security (Python)

**File:** `login_security.py`

A practice program that simulates a login with multiple checks.

### What it does
- Asks for a username and password and gives the user 3 attempts.
- If they are correct, checks the account status and then asks for an OTP.
- Counts every failed step (wrong login, inactive account, wrong OTP) and locks the account after 3 failed attempts.

### How to run
Run `python login_security.py` and follow the prompts.

### Limits
- The username, password and OTP are fixed demo values written in the code. This is for practice and is not real security.
- The OTP is not generated or sent anywhere.
- Entering letters instead of numbers for the OTP will crash the program.

## Basic School Webpage (HTML and CSS)

**File:** `School_webpage.html`

A webpage for a kids' preschool with a banner image, heading and tagline, a quote, a list of the school's values and a section on its programs (Playgroup, Nursery, LKG and UKG). Styled with div elements and a separate stylesheet, `basic_webpage.css`.
