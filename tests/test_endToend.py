import time

from pageObject.CheckoutPage import CheckOutPage
from pageObject.HomePage import HomePage
from utility.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_end2end(self):

        print(self.driver.title)
        print(self.driver.current_url)
        time.sleep(5)

        homePage = HomePage(self.driver)
        homePage.shopItems().click()   # Click shop button:

        checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.productsTitles()   # Identify all 4 products on the page:

        # Scroll to top of the page:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # scroll from 0 to highest
        time.sleep(3)

        # Perform for loop to add product to basket:
        for product in products:
            print(product.find_element_by_xpath("div/h4/a").text)
            productName = product.find_element_by_xpath("div/h4/a").text
            productName = productName
            if productName == "Blackberry":
                product.find_element_by_xpath("div/button").click()   # This Clicks add button of item with name Blackberry
        time.sleep(3)

        # Scroll to top of the page
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")  # scroll from highest to 0
        time.sleep(3)

        # Click first CheckOut button:
        checkOutPage.clickCheckOutA().click()
        time.sleep(3)

        # Assert that product on page 1 is present in page 2 -> Check Out page:
        assert productName == productName
        print(productName)

        # Click final CheckOut button:
        checkOutPage.finalProductCheckOut().click()
        time.sleep(2)

        # Insert country of destination:
        checkOutPage.enterCountryName().send_keys("Nigeria")
        time.sleep(5)

        # select checkbox:
        checkOutPage.selectCheckBox().click()

        # Click Purchase button:
        checkOutPage.clickPurchaseButton().click()

        # Get transaction success text and print to console:
        successText = checkOutPage.displayMessage().text
        print(successText)

        # Assertion true:
        assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in successText

        # Capture screenshot of success page:
        self.driver.get_screenshot_as_file("EndToEnd_screenshot.png")






