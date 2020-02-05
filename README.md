# yeti-ecomm
The design pattern being used is a Page Object Model.  POM is used to have reusable WebElements/small helper methods separated from the actual test classes, allowing for cleaner code and easier test maintenance.

### Getting Started
1. Install Python 3.x
https://www.python.org/downloads/  
*Optionally, you can create a virtual env to isolate Python dependencies between projects*

2. In a terminal install the following packages:  
`pip install selenium`  
`pip install pytest`  

3. Add Python 3.x to your PATH environment variable
4. Clone repo to your local machine

### Driver Setup
 A driver is separate executable that WebDriver uses to control Browsers.  Use links below to get started:
   > [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

   > [Firefox Driver]( https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver)
   	
#Note: Check Firefox + Chrome version & Selenium version compatibility before downloading geckodriver.

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
Log files are created with each test and if the test fails a screenshots is taken to  provide further information about what happened if they failed. The screenshots reside in the ./screenshots directory and can be viewed locally in your IDE

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
