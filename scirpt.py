from selenium import webdriver

server = 'http://localhost:4444'  # Usar host.docker.internal se localhost não funcionar
url = 'https://www.selenium.dev/documentation/webdriver/drivers/remote_webdriver/'

options = webdriver.ChromeOptions()
driver = webdriver.Remote(command_executor=server, options=options)

driver.get(url)

