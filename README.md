# HUDL QA Project
This is a basic suite of tests that uses the Page Object Model for a login page. It is built to be scalable.
From here we could add more intensive tests, such as verifying the password reset function works, etc.
But for the purposes of this project, the automation tests are kept simple.

## Getting started

### Requirements (Windows)
- Python 3.8+ (download from https://www.python.org/downloads/release/python-3812/)
- Chrome and Firefox browsers
- chromedriver for your version of Chrome (install from https://chromedriver.chromium.org/downloads)
- geckodriver (install from https://github.com/mozilla/geckodriver/releases)
- Add both of these drivers to the Windows PATH environment variable


### Setup
1. Install the requirements above.
2. Clone the project repo into a folder of your choice.
3. From the terminal, cd into where you cloned the 'hudl' folder.
4. Run `python -m venv venv` to create a virtual environment.
5. Activate your virtual environment:
    - MacOS: Run `source venv/bin/activate` to enable the virtual environment.
    - Windows: Run `<path to your venv>\Scripts\activate.bat` to enable the virtual environment.
    - When activated, your terminal prompt should be prefixed with `(venv)`.
    - To deactivate once done, simply run `deactivate`
6. Run `pip install -r requirements.txt` to install the project dependencies.
7. Create a .env file in the root folder of the project (i.e. 'hudl') with 3 variables:
    - TEST_USERNAME=<your-test-username-here>
    - TEST_PASSWORD=<your-test-password-here>
    - BASE_URL=https://www.hudl.com


### Usage
When the virtual environment is activated (see setup #5), pytest can be run from the 
terminal in the 'hudl' folder. The project currently supports 2 optional parameters:
- `--browser`
    - default is 'Chrome' but accepts `Chrome` or `Firefox` as an argument
- `--headless` 
    - takes no arguments; runs the tests without a visible UI


#### Examples
- Run a single login test in Chrome
    - Enter in the commandline:
        pytest tests/login_test.py::test_valid_credentials_login

- Run all login tests in Firefox
    - Enter in the commandline:
        pytest tests/login_test.py --browser Firefox

- Run all tests in headless Chrome
    - Enter in the commandline:
        pytest tests --headless
