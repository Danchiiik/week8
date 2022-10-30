
#! python3 -m venv venv - устанавливаем виртуальное окружение
#! source venv/bin/activate - активируем вир. акружение
#! deactivate - выйти из вир. акружение
#! pip freeze - показывает список всех библиотек в компе

# pip install beautyfulsoup4 - позволяет нам извлекать информацию HTML 
# pip install lxml - позволяет разбить HTNL код на составляющие
# pip install requests - позволяет сделать запрос

import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='catalog-list')
    try:
        cars = catalog.find_all('a', class_='catalog-list-item')
    except AttributeError:
        print('No more cars bitch')
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
        except AttributeError:
            title = ''
        try:
            price = car.find('span', class_='catalog-item-price').text
        except AttributeError:
            price = ''
        try:
            img = car.find(class_='catalog-item-cover-img')
            print(img)
        except AttributeError:
            img = ''
        
#         data = {
#             'title': title,
#             'price': price,
#             'img':img
#         }
#         write_in_file_csv(data)

#         # write_in_file_txt([title, price, img, '\n', '\n'])


# def write_in_file_csv(data):
#     with open('cars.csv', 'a')as file:
#         names = ['title', 'price', 'img']
#         writer = csv.DictWriter(file, delimiter=',', fieldnames=names)
#         writer.writerow(data)

# def write_in_file_txt(data):
#     with open('cars.txt', 'a') as file:
#         file.writelines(data)
        
def main():
    try:
        for i in range(90, 1000):
            url = f'https://cars.kg/offers/{i}'
            html = get_html(url)
            get_data(html)
            print(f'спарсили {i} страницу')
            print('\n')
    except UnboundLocalError:
        print('Go away bitch')

if __name__ == '__main__':
    main()