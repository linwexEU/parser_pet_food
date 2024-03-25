import csv
import random 


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'referer': 'https://royalcaninshop.com.ua/ua/g93477381-korm-dlya-sobak',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}


class UserAgentAndProxy: 

    @classmethod 
    def get_random_ua(cls): 
        with open("user_agent.txt") as file: 
            ua = file.readlines()
            return random.choice(ua).strip()
        
    @classmethod 
    def get_random_proxy(cls): 
        with open("Webshare 10 proxies.txt") as file: 
            proxy = random.choice(file.readlines()).strip() 
            return proxy.split(":")
        

class FileWork: 

    @classmethod 
    def create_file(cls): 
        with open("petfood.csv", "w", encoding="utf-8-sig", newline="") as file: 
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                ("Назва", "Артикул", "Зображення", "Опис (html)")
            )

    @classmethod 
    def add_to_file(cls, name, article, image, description): 
        with open("petfood.csv", "a", encoding="utf-8-sig", newline="") as file: 
            writer = csv.writer(file, delimiter=";")
            writer.writerow(
                (name, article, image, description)
            )