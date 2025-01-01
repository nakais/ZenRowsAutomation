# ZenRows Automation Project

## Overview
This project automates the process of accessing the ZenRows website, clicking on the "Start Free Trial" button, and solving the CAPTCHA using Anti-Captcha's API service.

## Features
- Automates website navigation with Selenium.
- Integrates Anti-Captcha API for CAPTCHA solving.
- Handles CAPTCHA bypass for websites using Cloudflare Turnstile.

## Requirements
- Python 3.8 or higher
- Selenium
- Anti-Captcha Official Python SDK
- Google Chrome and ChromeDriver

## Installation
1. Clone the repository:
```bash
git clone https://github.com/nakais/ZenRowsAutomation.git
```
2. Navigate to the project directory:
```bash
cd ZenRowsAutomation
```
3. Create a virtual environment:
```bash
python -m venv venv
```
4. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
5. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
1. Replace `YOUR_API_KEY_HERE` in the code with your Anti-Captcha API key.
2. Replace `YOUR_SITE_KEY_HERE` with the CAPTCHA site key obtained from the target website.

**Note:**
Anti-Captcha does not provide free credits for solving CAPTCHAs. It is a paid service, and you need to add funds to your account before using their API. Ensure you have sufficient credits in your Anti-Captcha account.

## Usage
Run the script:
```bash
python zenrows_test.py
```
## Recorded Video
A complete project walkthrough can be found in the video recorded on Loom:
https://www.loom.com/share/d103ef31a8344e739bba18d63280d91e?sid=7ef76639-93e7-4b47-b395-4150ea600b23

## Troubleshooting
- Check ChromeDriver compatibility with your Chrome version.
- Ensure your Anti-Captcha account has sufficient credits.
- Verify site key and API key configurations.


