import time
import subprocess
import platform
import socket
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import os
import random

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def check_domain_availability(domain, processed_domains):
    if domain in processed_domains:
        return False

    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

def submit_report(driver, domain, processed_domains):
    if not check_domain_availability(domain, processed_domains):
        if domain not in processed_domains:
            logging.warning(f'Домен {domain} недоступен. Пропускаем и записываем в файл canceled.txt.')
            with open('canceled.txt', 'a') as canceled_domains_file:
                canceled_domains_file.write(f'{domain}\n')
                processed_domains.add(domain)
        return False

    # Открываем страницу для отправки отчета
    driver.get('https://safebrowsing.google.com/safebrowsing/report_error/?hl=en')

    # Вводим домен в поле "URL"
    url_field = driver.find_element(By.ID, 'url')
    url_field.clear()
    url_field.send_keys(domain)

    # Вводим текст в поле "Additional details: (Optional)"
    additional_details_field = driver.find_element(By.ID, 'dq')
    
    additional_details_texts = [
        '''
        text1
        ''',
        '''
        text2
        '''
          ,
        '''
        text3
        '''
    ]
    
    additional_details_text = random.choice(additional_details_texts)
    additional_details_field.clear()
    additional_details_field.send_keys(additional_details_text)

    # Ждем, пока пользователь перенаправит нас на страницу успешной отправки отчета
    try:
        WebDriverWait(driver, 100).until(EC.url_contains('submit_success'))
        logging.info(f'Отчет для: {domain} успешно отправлен!')
        return True
    except TimeoutException:
        logging.warning(f'Не удалось перейти на страницу успешной отправки отчета для {domain}.')
        return False

# Открываем файл с доменами
with open('domains.txt', 'r') as f:
    domains = f.read().splitlines()

# Множество для отслеживания обработанных доменов
processed_domains = set()

# Опции для ChromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

# Автоматическая установка последней версии ChromeDriver
service = webdriver.chrome.service.Service(ChromeDriverManager().install())

# Открываем браузер
driver = webdriver.Chrome(service=service, options=chrome_options)

# Максимальное количество попыток отправки отчета
max_attempts = 3

index = 0  # Индекс текущего домена

try:
    # Открываем файл successful.txt для записи
    with open('successful.txt', 'a') as successful_domains_file:
        while index < len(domains):
            domain = domains[index]
            attempts = 0  # Счетчик попыток отправки отчета

            while attempts < max_attempts:
                success = submit_report(driver, domain, processed_domains)

                if success:
                    # Записываем успешный отчет в файл successful.txt
                    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                    successful_domains_file.write(f'Домен: {domain} - репорт успешно отправлен! Дата: {current_time}\n')
                    successful_domains_file.flush()
                    break  # Успешно отправлено, переходим к следующему домену
                else:
                    attempts += 1
                    logging.warning(f'Повторяем попытку отправки для {domain} (попытка {attempts})...')

            if attempts >= max_attempts:
                logging.error(f'Зафейлилась отправка для домена {domain} после {max_attempts} попыток.')

            time.sleep(2)

            index += 1  # Переходим к следующему домену

except TimeoutException as e:
    logging.error(f'Произошла ошибка TimeoutException: {str(e)}')
except Exception as e:
    logging.error(f'Произошла ошибка: {str(e)}')

# Закрываем браузер после работы скрипта
driver.quit()

# Открываем файл successful.txt после выполнения скрипта
try:
    if platform.system() == 'Windows':
        os.startfile('successful.txt')  # Винда
    elif platform.system() == 'Darwin':
        subprocess.call(['open', 'successful.txt'])  # Яблоко
    else:
        subprocess.call(['xdg-open', 'successful.txt'])  # Линуха
except Exception:
    logging.warning('Невозможно автоматически открыть файл successful.txt на данной операционной системе.')
