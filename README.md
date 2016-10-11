# gTranslator
Translate a wording json file.

In the process of the translation of your project, you can use this tool to automatically translate the wordings you list in a structured json file (example in input.json). It uses Google translate.

## Installation
1. Clone repository
    `git clone https://github.com/scorring/gTranslator.git`
    `cd gTranslator`
2. Create a python virtualenv
If it is not already installed, install the package python-virtualenv.
Then create a new virtualenv in the projec folder:
`virtualenv venv`
`source venv/bin/activate`
3. Install requirements
pip install -r requirements.txt
4. Install Chromedriver
For now, we use chrome in this project. To install chrome driver for selenium, visit https://sites.google.com/a/chromium.org/chromedriver/, download the driver and move it to gTranslator/chromedriver or modify the chromedriver_path in the config.py file.

## Configuration
Open the config.py file and set your own settings:
* _chromedriver_path_: Path for chromedriver file
* _in_path_: Path for input json file
* _out_path_: Path for output json file
* _in_language_code_: Language for the input json file (default: en)
* _out_language_code_: Language for the output json file (default: fr)

## Run
`python translator.py`
The result is saved into out.json by default
