# Requires:
	* Python3
	* pytest
	* pytest-selenium
	* chromedriver or any other drivers for your browser
	* pytest-html
	
# use pip3 to install the packages
$ pip3 install pytest
$ pip3 install pytest-selenium

# run one test
To run individual script:
pytest <script_name> --driver chrome --driver-path ./chromedriver 

# run entire suite
pytest --driver chrome --driver-path ./chromedriver

# To run in other browsers replace chrome and with other browsers
eg. pytest --driver safari --driver-path ./safaridriver

# generate summary
pytest --html=report.html --driver chrome --driver-path ./chromedriver

# Bonus
The shortest sleeptime that can be allowed is 3.5 seconds.	
