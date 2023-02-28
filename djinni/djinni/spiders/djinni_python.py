import scrapy


class DjinniPythonSpider(scrapy.Spider):
    name = "djinni_python"
    allowed_domains = ["djinni.co"]
    start_urls = ["http://djinni.co/"]

    def parse(self, response):
        pass
