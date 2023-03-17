from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
def parse():
    url = 'https://www.omgtu.ru/l/?SHOWALL_1=1' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    #print('Cтатуc страницы',page.status_code) # смотрим ответ

    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4.
    block = soup.findAll('a', class_='news-card__link') # находим  контейнер с нужным классом.

    description = ''
    file = open("file.txt", 'w+', encoding="utf-8") # создание файла для записи.
    # count = 0 # Счетчик для проверки количества новостей.
    # print(block)

    for data in block: # проходим циклом по содержимому контейнера.
        if data.find('h3'): # находим тег <h3>.
            description += data.text.replace('  ','').lstrip('\n').rstrip('\n')+'\n' # Поиск каждого заголовка и запись его в переменную.
            # count += 1
    file.write(description) # запись в файл.

    with open("file.txt", "r", encoding="utf-8") as file1: # вывод результата.
        for line in file1:
            print(line.strip())
    file.close() # Завершение работы с файлом.

    # print('Итоговое количество новосте