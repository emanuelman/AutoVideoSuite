from selenium import webdriver

server = "http://192.168.100.95:4444"

options = webdriver.ChromeOptions()

driver = webdriver.Remote(options=options, command_executor=server)
driver.get("https://www.selenium.dev/documentation/webdriver/getting_started/")

