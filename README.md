# Phishing-Link-Scanner
## **Overview**
The Phishing Link Scanner is a web-based application designed to help users identify potentially malicious URLs that could be used for phishing attacks. This tool uses a combination of blacklist checking, URL pattern analysis, and page content analysis to determine whether a given URL is likely to be safe or a phishing attempt.

## **Features**
- Blacklist Checking: Compares the submitted URL against a list of known malicious URLs.
- URL Pattern Analysis: Detects common phishing patterns in the URL such as the presence of IP addresses, suspicious keywords (e.g., "login", "verify"), and file extensions (e.g., ".zip").
- Page Content Analysis: Scrapes the webpage content to search for sensitive keywords (e.g., "password", "credit card") that are commonly targeted in phishing attacks.

## **Technologies Used**
- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- Web Scraping: BeautifulSoup (Python)
