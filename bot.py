from config import users_dict
from time import sleep
from moduls import login_in, look_youtub, mail_click, serfing


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options



# puppeteer  learn
# https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html, https://bot.sannysoft.com/
url = 'https://aviso.bz/login'
# url = 'https://trafbig.fun/r/58014'


# https://trafbig.fun/r/58014
def bot_drive(urls):
    # agent = ua.google
    count = input("Кто? ")
    agent, login, password = users_dict[count].values()
    optins = Options()
    optins.headless = True
    optins.set_preference('dom.webdriver.enabled', False)
    optins.set_preference('media.volume_scale', '0.0')
    optins.set_preference('dom.ipc.processCount', '3')
    optins.set_preference('toolkit.cosmeticAnimations.enabled', False)
    optins.set_preference('general.useragent.override', agent)
    optins.set_preference('browser.sessionstore.max_tabs_undo', 4)
    optins.set_preference('browser.sessionhistory.max_entries', 10)
    optins.set_preference('browser.sessionhistory.max_total_viewers', 2)
    optins.set_preference('geo.enabled', False)
    optins.set_preference('network.prefetch-next', False)
    optins.set_preference('media.cache_size', 128000)

    serves = Service(executable_path='Draiver/geckodriver.exe')
    driver = webdriver.Firefox(service=serves, options=optins)
    action = ActionChains(driver)
    driver.get(url=urls)
    driver.set_window_size(1276, 1024)

    try:
    # mail_click.mail_click(driver, action, By)
        login_in.log_in(driver, action, Keys, By, login, password)

        print(look_youtub.look_video_youtub(driver, action, By, login))

        driver.refresh()
        sleep(2)

        print(serfing.serfing_links(driver, action, By, login))
        driver.quit()

        print('The BOT is tired')

    except KeyError as er:
        print(er)
    finally:
        driver.quit()


def main():
    bot_drive(url)


if __name__ == '__main__':
    main()
