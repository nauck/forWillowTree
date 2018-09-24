# Requires:
	* Python3
	* pytest
	* pytest-selenium
	* chromedriver or any other drivers for your browser
	* pytest-html
	
# Use pip3 to install packages
$ pip3 install pytest
$ pip3 install pytest-selenium

# Run single test
pytest <script_name> --driver chrome --driver-path ./chromedriver 

# Run entire suite
pytest --driver chrome --driver-path ./chromedriver

# Run in other browsers replace chrome and with other browsers
eg. pytest --driver safari --driver-path ./safaridriver

# Generate summary
pytest --html=report.html --driver chrome --driver-path ./chromedriver

# Bonus
The shortest sleeptime that can be allowed is 3.5 seconds.	
