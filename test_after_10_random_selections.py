from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep
import random

# ----------------------------------------------------------------------
# Verify that after 10 random selections the correct counters are being
# incremented for tries and correct counters.
# ----------------------------------------------------------------------
def test_after_10_random_selections(driver):

    # generate 10 random selection of list
    selection = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    random.shuffle(selection)

    # click on a photo randomly and append "attempts" and "correct" to the lists below
    attempts = []
    correct = []
    for i in selection:
        photos = driver.find_element_by_id('gallery').find_elements_by_class_name(
            'photo')
        photos[i].click(); sleep(5)
        attempts.append(int(driver.find_element_by_class_name('attempts').text)); sleep(1)
        correct.append(int(driver.find_element_by_class_name('correct').text)); sleep(1)

    # check that the list are incremented correctly
    assert attempts == sorted(attempts)
    assert correct == sorted(correct)

    
