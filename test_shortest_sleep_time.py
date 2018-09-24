from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time
from selenium.webdriver.support import expected_conditions as EC


# ----------------------------------------------------------------------
# Bonus -​What's​the​shortest​we​can​allow​the​sleeps​in​the​example​
# provided​(B.)​before it​starts​failing?​Can​you​do​this​
# programmatically?
# ----------------------------------------------------------------------
def test_shortest_sleep_time(driver):

    # Note down the "name" and "correct" before clicking on a photo
    correct = int(driver.find_element_by_class_name('correct').text)
    name = driver.find_element_by_id('name').text

    # click on a photo and check "correct"
    for i in range(4):
        photos = driver.find_elements_by_class_name('photo')
        photos[i].click()

        """
        If a "correct" photo is selected, the 'correct' number updates 
        immediately, but the 'name' id takes some time to update. If we can 
        measure the time for the new 'name' to load this will be our
        minimal wait time
        """
        newCorrect = int(driver.find_element_by_css_selector('#stats > span.correct').text)
        if newCorrect > correct:
            start = time.time()
            while driver.find_element_by_id('name').text == name:
                continue
            stop = time.time()
            # This is the shortest sleep time we can allow  before it starts failing
            delta = stop - start 
            print("The shortest sleeptime is: " +  str(delta))
            break
