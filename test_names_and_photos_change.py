from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from time import sleep
import random
import pdb

# ----------------------------------------------------------------------
# Verify name and displayed​fotos​change​after​selecting​the​correct​
# answer.
# ----------------------------------------------------------------------
def test_names_and_photos_change(driver):

    # selections
    selection = list(range(5))
    
    # capture name and image before clicking
    fotos = capture_image_src(driver)
    name = driver.find_element_by_id('name').text
    correct = int(driver.find_element_by_class_name(
            'correct').text)

    for i in selection:
        photos = driver.find_element_by_id('gallery').find_elements_by_class_name(
            'photo')
        photos[i].click(); sleep(6)
        newCorrect = int(driver.find_element_by_class_name('correct').text)
        # pdb.set_trace()

        # if 'correct' value changes capture the name and image again
        if newCorrect > correct:
            newFotos = capture_image_src(driver)
            newName = driver.find_element_by_id('name').text
            # assert to make sure that the images are new and name has changed
            assert newName != name
            assert newFotos != fotos
            break

def capture_image_src(driver):
    gallery = driver.find_element_by_id('gallery')
    photos = gallery.find_elements_by_class_name('photo')
    images = [photo.find_element_by_tag_name('img') for photo in photos]
    image_sources = [image.get_attribute("src") for image in images]
    return image_sources
