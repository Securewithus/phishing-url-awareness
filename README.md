# EWB Phishing URL Awareness Checker

## Overview
[WRITE IN YOUR OWN WORDS, 2-3 sentences: what phishing is, and what your tool does.]

## Features
- Detects an @ symbol in the URL
- Flags unusually long URLs (over 100 characters)
- Flags IP-address hostnames
- Flags many hostname segments (5 or more)
- Flags punycode-style hostnames (xn--)
- Flags the HTTP scheme
- Loop: checks many URLs in one run; type q to quit
- "Review carefully" summary with a count of warnings
- Handles malformed input such as http://[bad without crashing
- Short "Why" explanation under each warning

## Requirements
Python 3.10 or later. No extra packages.

## How to Run
Windows: python phishing_checker.py
Mac/Linux: python3 phishing_checker.py

## Example Output
[PASTE THE OUTPUT OF ONE REAL RUN FROM YOUR COMPUTER HERE.]

## Testing
| # | Input | Expected | Actual | Result |
|---|-------|----------|--------|--------|
| 1 | https://www.example.com/login | No warning signs | [fill] | [PASS/FAIL] |
[Add rows 2 to 5. Full table is in tests/test_samples.md]

## Screenshots
![Sample run](screenshots/sample_run.png)
![Test results](screenshots/test_results.png)

## Improvements
1. Loop with quit - [why you chose it, how you tested it]
2. Review carefully summary - [why, how tested]
3. Malformed input handling - [why, how tested: typed http://[bad before and after]
4. Explanations for warnings - [why, how tested]

## Limitations
This is an educational tool. It only reads URL text. It does not visit
URLs, scan for malware or prove that a URL is safe. No warning signs
found does NOT mean a URL is safe.

## Ethical Use
Use sample strings only. Do not collect credentials. Do not use this
project to deceive anyone or to test websites without permission.

## Author
Akash Tiwari, AI-POWERED CYBERSECURITY INTERNSHIP, EWB Courses
