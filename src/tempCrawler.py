# import os
#
# listaTextos = os.listdir(r"\Users\Juan\Desktop\Texts\chunkText")
#
# print(len(listaTextos))
#
# listaNumerosHoteles = list(map(lambda x: x.split('_')[1],listaTextos))
# print(listaNumerosHoteles)
# links_comienzo = list(map(lambda x: 'https://www.tripadvisor.com/Hotel_Review-g60878-d' + x + '-Reviews-The_Loyal_Inn-Seattle_Washington.html',listaNumerosHoteles))
#
# print(len(links_comienzo))
# print(links_comienzo)


import scrapy

class chunkScrawler(scrapy.Spider):
    name = 'tripadvisor'
    start_urls = ['https://www.tripadvisor.com/Hotel_Review-g60878-d72572-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d72579-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d72586-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73718-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73727-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73739-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73757-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73787-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73799-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73821-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73855-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73923-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73943-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73947-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73950-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73957-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d73985-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d74051-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d74583-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d74626-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d75662-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d76061-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d76083-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d76442-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d77055-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d77264-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d77270-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d77274-Reviews-The_Loyal_Inn-Seattle_Washington.html',
     'https://www.tripadvisor.com/Hotel_Review-g60878-d77629-Reviews-The_Loyal_Inn-Seattle_Washington.html']

    def parse(self, response):
        array = ['72572', '72579', '72586', '73718', '73727', '73739', '73757', '73787', '73799', '73821', '73855', '73923', '73943', '73947', '73950', '73957', '73985', '74051', '74583', '74626', '75662', '76061', '76083', '76442', '77055', '77264', '77270', '77274', '77629']
        cont = 0
        for products in response.css('div._1vnZ1tmP'):
            yield {
               array[cont] : products.css('h1._1mTlpMC3::text').get()
            }


