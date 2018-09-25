# Requires:
	* Python3
	* pytest
	* pytest-selenium
	* chromedriver or any other drivers for your browser
	* pytest-html
	
# Use pip3 to install packages
$ pip3 install pytest

# Run single test script
pytest <script_name> --driver chrome --driver-path ./chromedriver 

# Run entire test suite
pytest --driver chrome --driver-path ./chromedriver

# To run in other browsers, replace chrome and with browser name
eg. pytest --driver safari --driver-path ./safaridriver

# To generate summary report
pytest --html=report.html --driver chrome --driver-path ./chromedriver

# Bonus
The shortest sleeptime that can be allowed is 3.5 seconds.	
