from time import sleep
import re
from moduls import choice_item_menu



def visit_link_serf_time(driver, list_vis, serf_links, By):
    for serf_link in serf_links:
        id_td = re.findall(r'=\d+', serf_link.get_attribute('onclick'))[0][1:]
        if id_td not in list_vis:
            list_vis.append(id_td)
            item_time = driver.find_element(By.CLASS_NAME, 'de_' + id_td)\
                .find_element(By.CLASS_NAME, 'serf-text')
            times_visibel = int(re.findall(r'\d+', item_time.text)[0])
            return [serf_link, times_visibel]


def serfing_links(driver, action, By, login):
    pass

    scroll = step_bad = 0
    steps = 5
    link_visit = []

    choice_item_menu.select_item_menu(driver, action, By, 1)
    sleep(2)

    driver.execute_script(f'window.scrollTo(0, 750)')
    sleep(1.5)

    wrapper_links = driver.find_element(By.ID, 'contentwrapper')
    serfing_links = list(wrapper_links.find_elements(By.CLASS_NAME, 'work-serf'))
    steps_to_end = len(serfing_links)

    if steps_to_end < 15:
        return f'Small serfing links {steps_to_end}'
# srart while!
    for links in serfing_links:
        driver.switch_to.window(driver.window_handles[0])
        print('start', steps_to_end)
# blok if start
        if not steps:
            scroll += 200
            if steps_to_end > 70:
                steps = 5
            else:
                steps = 4
            driver.execute_script(f'window.scrollTo(0, {750 + scroll})')
        if step_bad == 10:
            return 'Much bads in Serfing!'
        steps_to_end -= 1
        steps -= 1
        if steps_to_end == 0:
            return 'The end serfing'

# blok if end
# получаем id ссылки
        td_id = re.findall(r'\d+', links.get_attribute('id'))[0]
        try:
            link_to = links.find_element(By.CSS_SELECTOR, f'#start-serf-{td_id} > a')
            action.click(link_to).perform()
        except:
            step_bad += 1
            print('problem id')
            continue
        sleep(2.5)

        try:
            serf_links = driver.find_elements(By.CLASS_NAME, 'start-yes-serf')
#  f
            serfing_link, times_vis = visit_link_serf_time(driver, link_visit, serf_links, By)
            action.click(serfing_link).perform()
        except:
            step_bad += 1
            print('no serfing link')
            driver.get_screenshot_as_file(f'no serfing link {login}.png')
            continue
        driver.switch_to.window(driver.window_handles[1])
        sleep(times_vis + 2)
        #  Полный цсс селектор как есть без каких либо изменений.
        html = driver.find_element(By.CSS_SELECTOR, 'html > frameset > frame:nth-child(1)')
        # переходим во фрейм
        driver.switch_to.frame(html)
        # элементы во фрейме периодически обновляются так что все действия делаем быстро
        try:
            body = driver.find_element(By.TAG_NAME, 'body')
            btn = body.find_element(By.CLASS_NAME, 'btn_capt')
            action.click(btn).perform()
        except:
            print('capch problem')
            continue
        sleep(1)
        driver.close()
        sleep(1)

