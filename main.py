import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time

"""

Resolver Techinical Assessment for Automation Test Engineering Coop Position - Dipen Kumar Maheshwari.

The chromedriver and QE-index.html must be in the same folder as this file in order to run.

To Run:
pip install selenium
python main.py or python3 main.pyf

"""


class ResolverTestAssessment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url = "file:///Users/dipenkumar/Documents/Developing-Codes/OA/Resolver/QE-index.html"

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test1(self):
        try:
            driver = self.driver
            driver.get(self.base_url)

            email_input = driver.find_element(By.ID, "inputEmail")
            password_input = driver.find_element(By.ID, "inputPassword")
            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

            self.assertIsNotNone(email_input, "Email input is missing")
            self.assertIsNotNone(password_input, "Password input is missing")
            self.assertIsNotNone(login_button, "Login button is missing")

            email_input.send_keys("test1@example.com")
            password_input.send_keys("abc123456")

        except (TimeoutException, NoSuchElementException) as e:
            self.fail(f"Test 1 failed: {str(e)}")

    def test2(self):
        try:
            driver = self.driver
            driver.get(self.base_url)

            list_group = driver.find_element(By.ID, "test-2-div")
            list_items = list_group.find_elements(By.TAG_NAME, "li")

            self.assertEqual(len(list_items), 3, "Expected 3 list items")

            second_item = list_items[1]
            second_item_text = str(" ".join(second_item.text.split(" ")[0:3]))
            badge_text = second_item.find_element(By.TAG_NAME, "span").text

            self.assertEqual(
                second_item_text, "List Item 2", "Second item text mismatch"
            )
            self.assertEqual(badge_text, "6", "Badge value mismatch")

        except (TimeoutException, NoSuchElementException) as e:
            self.fail(f"Test 2 failed: {str(e)}")

    def test3(self):
        try:
            driver = self.driver
            driver.get(self.base_url)

            dropdown_element = driver.find_element(By.ID, "dropdownMenuButton")

            self.assertEqual(
                dropdown_element.text, "Option 1", "Default value is not 'Option 1'"
            )

            dropdown_element.click()
            select_option = driver.find_element(By.XPATH, "//a[text()='Option 3']")
            select_option.click()

        except (TimeoutException, NoSuchElementException) as e:
            self.fail(f"Test 3 failed: {str(e)}")

    def test4(self):
        try:
            driver = self.driver
            driver.get(self.base_url)

            buttons = self.driver.find_elements(
                By.XPATH, "//div[@id='test-4-div']//button"
            )
            button1 = buttons[0]
            button2 = buttons[1]

            self.assertTrue(button1.is_enabled(), "Button 1 in test-4 is not enabled")
            self.assertFalse(button2.is_enabled(), "Button 2 in test-4 is not disabled")

        except (TimeoutException, NoSuchElementException) as e:
            self.fail(f"Test 4 failed: {str(e)}")

    def test5(self):
        try:
            driver = self.driver
            driver.get(self.base_url)

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "test5-button"))
            )
            button5 = driver.find_element(By.ID, "test5-button")

            button5.click()

            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.ID, "test5-alert"))
            )

            alert = driver.find_element(By.ID, "test5-alert")

            self.assertTrue(alert.is_displayed(), "Success message not displayed")
            self.assertFalse(button5.is_enabled(), "Button for test-5 is not disabled")

        except TimeoutException as e:
            self.fail(f"Test 5 failed: Dynamic element timeout - {str(e)}")
        except Exception as e:
            self.fail(f"Test 5 failed: {str(e)}")

    def test6(self):
        try:
            driver = self.driver
            driver.get(self.base_url)

            # method to find the value of the cell at coordinates
            def find_cell_by_coordinates(row, col):
                rows = self.driver.find_elements(
                    By.XPATH, "//div[@id='test-6-div']//tbody/tr"
                )

                if 0 <= row < len(rows):
                    cells = rows[row].find_elements(By.TAG_NAME, "td")
                    if 0 <= col < len(cells):
                        return cells[col].text
                return None

            cell_value = find_cell_by_coordinates(2, 2)
            element_to_verify = self.assertEqual(
                cell_value, "Ventosanzap", "Cell value mismatch"
            )

        except Exception as e:
            self.fail(f"Test 6 failed: {str(e)}")


if __name__ == "__main__":
    unittest.main()
