from time import sleep


def log_in(drive, actio, Keys, By, log, passw):
    sleep(1)
    login = drive.find_element(By.NAME, 'username')
    actio.click(login)
    actio.send_keys(log)
    actio.send_keys(Keys.TAB)
    actio.send_keys(passw)
    actio.send_keys(Keys.ENTER)
    actio.perform()
    print('Avtorizovan ' + log)