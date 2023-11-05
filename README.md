![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Google Chrome](https://img.shields.io/badge/Google%20Chrome-4285F4?style=for-the-badge&logo=GoogleChrome&logoColor=white) ![Selenium](https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white)

## What the script does:

1. Opens the Safe Browsing service (https://safebrowsing.google.com/safebrowsing/repor...).
2. Specifies the domain from the domains.txt file and enters it in the "URL" field.
3. Specifies the text in the "Additional details" field.
4.Waits for the user to manually complete the reCAPTCHA verification and click the "Submit report" button.
5. If redirected to "https://www.google.com/safebrowsing/static/submit_...", it means the report has been successfully submitted.
5. The script repeats the actions with another domain from the domains.txt file.
7. Additionally, the script searches for non-working domains in the list. If a non-working domain is found, the script writes it to the "canceled.txt" file.

## Requirements for the script to work correctly:

1. The "ReportSender2.0" folder must contain a domains.txt file for scanning domains, and it should contain the domains.
2. The latest version of Chrome is required, as the script relies on the latest Chrome driver (The script includes the function ChromeDriverManager().install() to download the latest driver).
3. Use the script without a VPN (Google detects decrypted traffic and makes the CAPTCHA more complex).

## Important:

1. The script does not interact with CAPTCHA or automate its bypass.

# Russian :sparkles:

## Что делает скрипт:
1. Открывает сервис безопасного просмотра (https://safebrowsing.google.com/safebrowsing/repor...);
2. Указывает домен из файла domains.txt и вписывает его в поле “URL“;
3. Указывает текст в поле “Additional details“;
4. Ожидает, пока пользователь вручную пройдет проверку reCAPTCHA и нажмет кнопку “Отправить отчет“;
5. Если происходит перенаправление на "https://www.google.com/safebrowsing/static/submit_...", это означает, что отчет был успешно отправлен;
6. Скрипт повторяет действия только уже с другим доменом из списк в файле "domains.txt“;
7. Также, скрипт ищет неработающие домены в списке. Если найден неработающий домен - скрипт записывает его в файл “canceled.txt“.

## Требования для правильной работы скрипта:
1. В папке со скриптом должен находиться файл domains.txt для сканирования доменов, ну и конечно в нем должны быть домены :)
2. Необходима последняя версия Chrome, так как для работы скрипта требуется последняя версия драйвера Chrome (В скрипте есть функци ChromeDriverManager().install() которая качет последний драйвер);
3. Использовать без VPN (гугл определяет что трафик дешифруется и усложняет капчу в несколько раз).

## Важно:
1. Скрипт не взаимодействует с капчей и не автоматизирует ее обход.
