import scrapy

from scrapy.http import Response


def delete_double_symb(text: list) -> str:
    if len(text) > 1:
        out = [list(text)[0], ]
        for i in range(1, len(text)):
            if text[i] == text[i - 1] and text[i] in " .,;":
                continue
            else:
                out.append(text[i])
        return "".join(out)
    return ""


def delete_empty_cells(array: list) -> list:
    out = [delete_double_symb(elm) for elm in array if (elm != "" and elm != ",")]
    return out


def parse_detail_page(response: Response) -> None:
    yield {
        "title": response.css("h1::text").get().strip(),
        "company": response.css(".job-details--title::text").get().strip(),
        "salary": response.css("h1 .public-salary-item::text").get(),
        # "technologies": delete_empty_cells([text for text in response.css(
        #     ".job-additional-info--body")[0].css("span::text").getall()]),
        "category": delete_empty_cells([text.replace("\n", "").strip() for text in response.css(
            ".job-additional-info--body")[0].css("div::text").getall()]),
        # "additional": delete_empty_cells([text.replace("\n", "").strip() for text in response.css(
        #     ".job-additional-info--body")[1].css("div::text").getall()]),
        "publicated": delete_empty_cells([text.replace("\n", "").strip() for text in response.css(
            ".text-muted::text").getall()]),
        "description": delete_empty_cells([text.replace("\n", "").strip() for text in response.css(
            ".profile-page-section")[0].css("div::text").getall()]),
        # "about_company": delete_empty_cells([text.replace("\n", "").strip() for text in response.css(
        #     ".profile-page-section")[1].css("div::text").getall()]),
    }


class DjinniPythonSpider(scrapy.Spider):
    name = "djinni_python"
    allowed_domains = ["djinni.co"]
    start_urls = ["https://djinni.co/jobs/?primary_keyword=Python"]

    def parse(self, response: Response, **kwargs):
        urls_on_page = response.css(
            "ul.list-jobs .order-1 a::attr(href)"
        ).getall()
        for url in urls_on_page:
            url_full = response.urljoin(url)
            yield scrapy.Request(url_full, parse_detail_page)

        next_page = response.css(".pagination li.page-item a::attr(href)").getall()[-1]
        url_next_page = response.urljoin(next_page)
        yield scrapy.Request(url_next_page, self.parse)
