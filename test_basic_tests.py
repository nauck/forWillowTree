from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys
import pytest


# ----------------------------------------------------------------------
# A. Verifies​name​game​title​is​shown.
# B. Verifies​“attempts”​counter is​incremented.
# ----------------------------------------------------------------------
def test_title_and_attempts(driver):
    # Verifies​​name​​game​​title​​is​​shown.
    assert driver.title == "name game"

    # Verifies​​“attempts”​​counter​​is​​incremented.
    # "attempts" counter is initially set to 0
    attempts = int(driver.find_element_by_class_name('attempts').text)
    assert attempts == 0
    
    # create a list to keep track of "attempts" on every clicks
    # click photo few times and append to the list on each click
    attemptsList = []
    for i in range(4):
        click_photo(driver, i)
        newAttempts = int(driver.find_element_by_class_name('attempts').text)
        attemptsList.append(newAttempts)
    
    # verify that counter is incremented
    assert attemptsList == [1, 2, 3, 4]


def click_photo(driver, index):
    photos = driver.find_element_by_id(
        'gallery').find_elements_by_class_name('photo')
    photos[index].click(); sleep(6)
