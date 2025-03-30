# TO-DO
1. Excel/CSV
2. Airflow or Cron Scheduler
3. Email Notifications

# STUDY NOTES
Web Scraping

2 Types of Websites:
1. Static
    - Requires only Beautiful Soup and ds4
2. Dynamic
    - Requires selenium and web driver (ex. chrome driver)
    - Chrome driver is now build into chrome (download not required)


Python Virtual Environments
- Good for handling python package versioning and dependencies
1. Create a venv in project directory
    - python3 -m venv <venv_name>
2. Activate venv
    - source <venv_name>/bin/activate
3. Install Dependencies
    - pip install -r requirements.txt
4. Deactivate venv
    - deactivate

WebDriver
- Automates web browsing to simulate user actions (ex. clicking buttons, scrolling, web scraping)