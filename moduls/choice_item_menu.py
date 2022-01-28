from time import sleep


def select_item_menu(driver, action, By, count):
    sleep(2)
    try:
        blok_link = driver.find_element(By.ID, 'mnu_tblock1')
        links = blok_link.find_elements(By.TAG_NAME, 'a')
        action.click(list(links)[count])
        action.perform()
    except:
        action.click(driver.find_element(By.ID, 'mnu_title1'))
        blok_link = driver.find_element(By.ID, 'mnu_tblock1')
        links = blok_link.find_elements(By.TAG_NAME, 'a')
        action.click(list(links)[count])
        action.perform()

