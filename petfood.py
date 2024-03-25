import aiohttp 
import asyncio
from bs4 import BeautifulSoup 
from work import headers, UserAgentAndProxy, FileWork


class Parser: 
    def __init__(self):
        pass

    async def parse_page(self, session, link): 
        async with session.get(link, headers=headers) as response: 
            res_text = await response.text() 
            soup = BeautifulSoup(res_text, "lxml")

            name = soup.find("h1", class_="b-product__title b-online-edit").text.strip() 
            article = soup.find("li", class_="b-product-data__item b-product-data__item_type_sku").find("span").text.strip() 
            image = soup.find("div", class_="js-product-gallery-overlay b-product-view__image-link").get("href")
            description = soup.find("div", class_="b-user-content")

            FileWork.add_to_file(name=name, article=article, image=image, description=description)


    async def init_parser(self, category, pages):
        tasks = []

        async with aiohttp.ClientSession() as session:
            headers["user-agent"] = UserAgentAndProxy.get_random_ua()
            for page in range(1, pages + 1):
                async with session.get(f"https://royalcaninshop.com.ua/ua/{category}/page_{page}", headers=headers) as response: 
                    res_text = await response.text() 
                    soup = BeautifulSoup(res_text, "lxml")

                    for item in soup.find_all("a", class_="b-product-list__image-link"): 
                        link = "https://royalcaninshop.com.ua" + item.get("href")
                        task = asyncio.create_task(self.parse_page(session, link))
                        tasks.append(task) 

                print(f"[INFO] {page} - done!")
                    
            await asyncio.gather(*tasks)



if __name__ == "__main__": 
    parser = Parser() 
    FileWork.create_file()

    for item in zip(["g93477381-korm-dlya-sobak", "g93477386-korm-dlya-kotov", "g119181419-veterinarnye-diety"], [4, 5, 5]):
        asyncio.run(parser.init_parser(item[0], item[1]))