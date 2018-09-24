from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep

@pytest.fixture
def driver(selenium):
    # setup
    selenium.implicitly_wait(10)
    selenium.get("http://www.ericrochester.com/name-game/")
    sleep(3)

    # pass control to test method
    yield selenium

    # teardown
    selenium.close()
    
