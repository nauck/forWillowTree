# forWillowTreeRequires:
	* Python3
	* pytest
	* pytest-selenium
	* chromedriver or any other drivers for your browser
	* pytest-html
	
Both pytest and pytest-selenium packages can be obtained using pip3
$ pip3 install pytest
$ pip3 install pytest-selenium

Running Tests:
To run individual script:
pytest <script_name> --driver chrome --driver-path ./chromedriver 

To run entire suite:
pytest --driver chrome --driver-path ./chromedriver

You can also replace chrome and the correspoding path with the browser you are testing against.
eg. pytest --driver safari --driver-path ./safaridriver

For generating the report:
pytest --html=report.html --driver chrome --driver-path ./chromedriver

Bonus Question:
The shortest sleeptime that can be allowed is 3.5 seconds.	