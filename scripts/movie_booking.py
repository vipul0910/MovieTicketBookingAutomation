# scripts/movie_booking.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils import wait_for_element
from config.settings import *

def book_movie_ticket():
    driver = webdriver.Chrome(executable_path=BROWSER_DRIVER_PATH)

    try:
        driver.get(BASE_URL)

        # Select city
        city_selection = wait_for_element(driver, By.XPATH, "//span[text()='Your City']")
        city_selection.click()
        city_input = driver.find_element(By.XPATH, "//input[@placeholder='Search for your city']")
        city_input.send_keys(CITY)
        city_input.send_keys(Keys.RETURN)

        # Search for the movie
        search_box = wait_for_element(driver, By.XPATH, "//input[@placeholder='Search for Movies, Events, Plays, Sports and Activities']")
        search_box.send_keys(MOVIE_NAME)
        search_box.send_keys(Keys.RETURN)

        # Select the movie
        movie_link = wait_for_element(driver, By.XPATH, "//a[contains(@href, 'movies')]")
        movie_link.click()

        # Choose a date (example logic)
        date_picker = wait_for_element(driver, By.XPATH, "//li[@data-date='desired-date']")
        date_picker.click()

        # Choose a time and theater
        show_time = wait_for_element(driver, By.XPATH, "//a[contains(@href, 'show')]")
        show_time.click()

        # Seat selection
        seats = driver.find_elements(By.CLASS_NAME, "available-seat")
        for seat in seats[:SEAT_COUNT]:
            seat.click()

        # Proceed to payment
        proceed_button = driver.find_element(By.ID, "proceed-button")
        proceed_button.click()

        print("Complete the payment manually.")
    finally:
        driver.quit()
