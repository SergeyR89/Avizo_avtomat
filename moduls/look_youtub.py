import re
from time import sleep
from moduls import dots_click, choice_item_menu
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ESi


def visit_link_youtub_time(driver, list_vis, youtub_links, By):
    for youtub_link in youtub_links:
        id_td = re.findall(r'\d+', youtub_link.get_attribute('onclick'))[0]
        if id_td not in list_vis:
            list_vis.append(id_td)
            item_time = driver.find_element(By.CLASS_NAME, 'ads_' + id_td)\
                .find_element(By.CLASS_NAME, 'serf-text')
            times_visibel = int(re.findall(r'\d+', item_time.text)[0])
            return [youtub_link, times_visibel]


def start_taimer():
    pass


def look_video_youtub(driver, action, By, login):
    scroll = step_bad = 0
    steps = 5
    link_visit = []
    wait = WebDriverWait(driver, 600)

    choice_item_menu.select_item_menu(driver, action, By, 4)
    sleep(2)

    # wrapper_links = driver.find_element(By.ID, 'contentwrapper')
    wrapper_links = wait.until(ESi.visibility_of_element_located((By.ID, 'contentwrapper')))
    serfing_links = list(wrapper_links.find_elements(By.CLASS_NAME, 'work-serf'))[2:]
    steps_to_end = len(serfing_links)

    if steps_to_end == 0:
        return 'no links watching'
    driver.get_screenshot_as_file('start.png')

# srart while!
    for links in serfing_links:
        driver.switch_to.window(driver.window_handles[0])
        print('start', steps_to_end)
# blok if start
        if not steps:
            scroll += 300
            if steps_to_end > 70:
                steps = 5
            else:
                steps = 4
            driver.execute_script(f'window.scrollTo(0, {scroll})')

        if step_bad == 9:
            return 'Much Bads in Youtub'
            break
        steps_to_end -= 1
        steps -= 1
        if steps_to_end == 0:
            return 'Finish look youtub'
            break
# blok if end
# получаем id ссылки
        td_id = re.findall(r'\d+', links.get_attribute('id'))[0]
        try:
            link_to = links.find_element(By.CSS_SELECTOR, f'#start-ads-{td_id} > span:nth-child(1)')
            action.click(link_to).perform()
        except:
            step_bad += 1
            print('id no', td_id)
            continue
        sleep(2.5)
# нажимаем на ссылку
        try:
            # wait.until(ESi.visibility_of_element_located(By.CLASS_NAME, 'go-link-youtube'))
            youtub_links = driver.find_elements(By.CLASS_NAME, 'go-link-youtube')

            youtub_link, times_vis = visit_link_youtub_time(driver, link_visit, youtub_links, By)
            action.click(youtub_link).perform()
            sleep(2)
            driver.switch_to.window(driver.window_handles[1])
        except:
            step_bad += 1
            print('no youtub link')
            continue
# переходим на другую вкладку и запускаем видео
#         try:
#
#             frame = driver.find_element(By.XPATH, ' html / body / table / tbody / tr[2] / td / iframe')
#             driver.switch_to.frame(frame)
#             play_btn = driver.find_element(By.CLASS_NAME, 'ytp-large-play-button')
#             action.click(play_btn).perform()
#             driver.switch_to.default_content()
#         except:
#             print('Problem in play')
#             driver.close()
#             continue
#  f
        dots_click.dot_click(action, {'x': (300, 650), 'y': (250, 600)})
        sleep(times_vis + 3)
        # capcha_blok = driver.find_element(By.ID, 'capcha-tr-block')
        # wait.until(ECi.visibility_of(capcha_blok))
#
        sleep(1)
        driver.close()
