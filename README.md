# TO-DO
| Status  | Task                      | Notes                                           |
|---------|---------------------------|-------------------------------------------------|
|   [x]   | 1. Scrape Website         | Scrape PrixWorkshop for now                     |
|   [x]   | 2. Write Excel/CSV        |                                                 |
|   [x]   | 3. Python VENV            |                                                 |
|   [x]   | 4. Airflow Scheduler      |                                                 |
|   [x]   | 5. Update Date/Time       |                                                 |
|   [ ]   | 6. Email Notifications    |                                                 |

# STUDY NOTES
## Web Scraping
-  2 Types of Websites:
1. Static
    - Requires only Beautiful Soup and ds4
2. Dynamic
    - Requires selenium and web driver (ex. chrome driver)
    - Chrome driver is now build into chrome (download not required)

## Python Virtual Environments
- Good for handling python package versioning and dependencies
1. Create a venv in project directory
    - python3 -m venv <venv_name>
2. Activate venv
    - source <venv_name>/bin/activate
3. Install Dependencies
    - pip install -r requirements.txt
4. Deactivate venv
    - deactivate
- To see version of python package
    - pip show <package name>
    - pip list

## WebDriver
- Automates web browsing to simulate user actions (ex. clicking buttons, scrolling, web scraping)

## Apache AirFlow
1. Export airflow to your project directory and set where intialization will happen. This reduces conflicts between multiple projects (isolation and portability)
    - export AIRFLOW_HOME=$(pwd)/airflow_home
2. Make directory for airflow
    - mkdir -p $AIRFLOW_HOME
3. Initialize airflow - creates log files, etc.
    - airflow db init
4. Set airflow.cfg files to not load example dags into project.
    - load_examples = False
    - set frequency to re-load/re-check dags
5. Check dag folder location in airflow.cfg file
    - create dag folder if necessary
    - add dag py file
6. Create airflow user/password
    - airflow users create --username vivi --firstname vivian --lastname dang --role Admin --email bowbian.dang@hotmail.com
    - then enter pw
7. Start airflow web server. This command is used to see UI and purpose
    - airflow webserver -p 8080
8. This command is the engine used to schedule tasks.
    - airflow scheduler
9. Run airflow webserver and scheduler at the same time (should only be used in dev)
    - airflow standalone
10. Shut down airflow
    - <ctrl c>
    - pkill -f airflow
- Other commands
    - airflow dags list - Shows all of the dags