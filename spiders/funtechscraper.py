import scrapy


class FuntechSpider(scrapy.Spider):
    name = 'funtech'
    start_urls = ['https://www.funtech.si/si/vsi-oddelki/komp/']

    def parse(self, response):
        for products in response.css('div.artikel_podlaga'):
            try:
                yield {
                    'name': products.css('div.artikel_naslov::text').get(),
                    'cena': products.css('div.cena_desno_glavna::text').get().replace(' €','')
                }
            except:
                yield {
                    'name': products.css('div.artikel_naslov::text').get(),
                    'cena': 'PRODANO'
                }

        next_page = response.css('a.ascend').attrib['href']

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)