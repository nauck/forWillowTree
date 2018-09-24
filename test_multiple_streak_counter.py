from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep

# ----------------------------------------------------------------------
# Verify​the​a​multiple​"streak"​counter resets after​getting​an​
# incorrect​answer.
# ----------------------------------------------------------------------
def test_multiple_streak_counter(driver):

    # count the "correct" and "streak" before clicking on the photo     
    streak = int(driver.find_element_by_class_name('streak').text)
    correct = int(driver.find_element_by_class_name('correct').text)

    # click on a photo and check "correct" and "streak"
    for i in [0, 1, 2, 3, 4]:
        photos = driver.find_element_by_id('gallery').find_elements_by_class_name(
            'photo')
        photos[i].click(); sleep(6)

        newStreak = int(driver.find_element_by_class_name('streak').text)
        newCorrect = int(driver.find_element_by_class_name('correct').text)

        # "streak" should increment  if a "correct" photo is selected
        if newCorrect > correct:
            assert newStreak == streak + 1
            correct = newCorrect
            streak = newStreak
            break

    # click on a photo until photos streak resets
    for i in [0, 1, 2, 3, 4]:
        photos = driver.find_element_by_id(
            'gallery').find_elements_by_class_name('photo')
        photos[i].click(); sleep(6)

        newCorrect = int(driver.find_element_by_class_name('correct').text)
        if newCorrect == correct:
            assert int(driver.find_element_by_class_name('streak').text) == 0
            break
    
