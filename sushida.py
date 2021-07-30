import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(executable_path="./chromedriver")

driver.get('http://typingx0.net/sushida/play.html')
print(driver.current_url)

canvas = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.TAG_NAME, "canvas"))
)
print(canvas)

time.sleep(10)


actions = ActionChains(driver)
actions.move_to_element_with_offset(canvas, 250, 260)
actions.click()
actions.perform()
time.sleep(5)
actions.perform()
time.sleep(5)

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()

actions = ActionChains(driver)
actions.send_keys("a")
actions.send_keys("b")
actions.send_keys("c")
actions.send_keys("d")
actions.send_keys("e")
actions.send_keys("f")
actions.send_keys("g")
actions.send_keys("h")
actions.send_keys("i")
actions.send_keys("j")
actions.send_keys("k")
actions.send_keys("l")
actions.send_keys("m")
actions.send_keys("n")
actions.send_keys("o")
actions.send_keys("p")
actions.send_keys("q")
actions.send_keys("r")
actions.send_keys("s")
actions.send_keys("t")
actions.send_keys("u")
actions.send_keys("v")
actions.send_keys("w")
actions.send_keys("x")
actions.send_keys("y")
actions.send_keys("z")
actions.send_keys("-")
actions.send_keys("!")
actions.send_keys("?")

t_end = time.time() + 60 * 1.6
while time.time() < t_end:
    actions.perform()
