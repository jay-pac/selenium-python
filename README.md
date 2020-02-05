# QE-UI
The design pattern being used is a Page Object Model.  POM is used to have reusable WebElements/small helper methods separated from the actual test classes, allowing for cleaner code and easier test maintenance.

### Getting Started
1. Install Python 3.x
https://www.python.org/downloads/  
*Optionally, you can create a virtual env to isolate Python dependencies between projects*

2. In a terminal install the following packages:  
`pip install selenium`  
`pip install pytest`  

3. Add Python 3.x to your PATH environment variable
<details>
<summary>
<b><i><u>How to add python PATH in windows</u></i></b>
</summary>
<p>
	
- Search 'env'
- Edit the System Environment Variables
- Click on 'Environment Variables' button
- Click on 'New' in the System Variable section
- Enter `PYTHONPATH` in the Variable name field
- Enter in the Variable value field `C:\Python[version];C:\Python[version]\DLLs;C:\Python[version]\lib;C:\Python[version]\Scripts;`
- Select and click Edit on 'path' the list of system variables
- add `%PYTHONPATH%` to the end existing Path variable value
- open a terminal /cmd promp and type `python`.  Should be able to run the interpreter and see the python version

</p>
</details>

4. Clone repo to your local machine

### Driver Setup
 A driver is separate executable that WebDriver uses to control Browsers.  Use links below to get started:
   > [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

   > [Firefox Driver](https://github.com/mozilla/geckodriver/releases)
   	
#Note: Check Firefox + Chrome version & Selenium version compatibility before downloading geckodriver.
<details>
<summary>
<b><i><u>How to evoke browsers</u></i></b>
</summary>
<p>
	
- download chromedriver and extract the file
- copy file in desired location > Add path to executable_path variable in your tests
- `driver = webdriver.Chrome(executable_path = 'C:\\chromedriver.exe')`

</p>
</details>

### Running Tests Locally
To execute the tests just browse to the path where the selenium project is located in your terminal and type:
`py.test tests/home/login_tests.py`

### Repository Details
Directory structure - ***NOTE: Base, Config, Utils will be implemented at a later date***
```
|__base: DriverFactory and PageFactory
|__config: For all configurations and credential files
|__page: Put your Page Objects in here
|__tests: Put your tests in here
|__utils: Base Loggers are kept in this folders
```

### Screehshots 
***NOTE:  Will be implemented in later date***
Log files are created with each test and if the test fails a screenshots is taken to  provide further information about what happened if they failed. The screenshots reside in the ./screenshots directory and can be viewed locally in your IDE

### Commands for Running Tests

a)py.test [options]

	-s	used to display the output on the screen	
	-v      increase verbosity
	-h	help for more options 
	-n 	used to run tests in parallel
  example: `py.test -s -v sfcc/tests/login/login_tests.py`

### Documentation
- [Offical Selenium Documentation](https://selenium.dev/documentation/en/)
- [Selenium with Python](https://selenium-python.readthedocs.io/index.html)
- [PyTest](https://docs.pytest.org/en/latest/index.html)
- [WebDriver W3](https://www.w3.org/TR/webdriver1/)
