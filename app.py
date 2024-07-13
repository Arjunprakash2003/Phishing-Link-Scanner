from flask import Flask, request, jsonify, render_template
import re
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def check_blacklist(url, blacklist):
    return url in blacklist

def analyze_url_patterns(url):
    suspicious_patterns = [
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',  # IP addresses
        r'login',  # "login" in URL
        r'verify',  # "verify" in URL
        r'update',  # "update" in URL
        r'secure',  # "secure" in URL
        r'\.zip',  # ".zip" files
    ]
    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            return True
    return False

def analyze_page_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        page_text = soup.get_text().lower()
        
        suspicious_keywords = ['password', 'credit card', 'social security', 'ssn', 'account']
        for keyword in suspicious_keywords:
            if keyword in page_text:
                return True
        return False
    except Exception as e:
        print(f"Error fetching URL content: {e}")
        return False

def check_phishing(url):
    blacklist = [
        'http://malicious.com',
        'http://phishing.com',
    ]
    if check_blacklist(url, blacklist):
        return True
    
    if analyze_url_patterns(url):
        return True
    
    if analyze_page_content(url):
        return True
    
    return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    url = request.form['url']
    is_phishing = check_phishing(url)
    result = "phishing" if is_phishing else "safe"
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
