from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class= 'card h-100']")
    productCheckOutButtonA = (By.CLASS_NAME, "btn-primary")
    productCheckOutButtonB = (By.CLASS_NAME, "btn-success")
    countryName = (By.ID, "country")
    checkBox = (By.CLASS_NAME, "checkbox-primary")
    purchase = (By.CLASS_NAME, "btn-lg")
    successInfo = (By.CLASS_NAME, "alert-success")

    def productsTitles(self):

        return self.driver.find_elements(*CheckOutPage.products)

    def clickCheckOutA(self):
        return self.driver.find_element(*CheckOutPage.productCheckOutButtonA)

    def finalProductCheckOut(self):
        return self.driver.find_element(*CheckOutPage.productCheckOutButtonB)

    def enterCountryName(self):
        return self.driver.find_element(*CheckOutPage.countryName)

    def selectCheckBox(self):
        return self.driver.find_element(*CheckOutPage.checkBox)

    def clickPurchaseButton(self):
        return self.driver.find_element(*CheckOutPage.purchase)

    def displayMessage(self):
        return self.driver.find_element(*CheckOutPage.successInfo)

