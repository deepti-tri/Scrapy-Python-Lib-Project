import scrapy


class MediumSpider(scrapy.Spider):
    name = 'medium'
    allowed_domains = ['www.medium.com']
    start_urls = ['https://medium.com/feed/tag/coding']

    #setting the location of the output csv file
    custom_settings = {
        'FEED_URI' : 'tmp/medium.csv'
    }

    def parse(self, response):
        #Remove XML namespaces
        response.selector.remove_namespaces()

        #Extract article information
        titles = response.xpath('//item/title/text()').extract()
        authors = response.xpath('//item/creator/text()').extract()
        dates = response.xpath('//item/pubDate/text()').extract()
        links = response.xpath('//item/link/text()').extract()

        for item in zip(titles,authors,dates,links):
            scraped_info = {
                'title' : item[0],
                'author' : item[1],
                'date' : item[2],
                'link' : item[3]
            }

            yield scraped_info
