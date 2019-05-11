# -*- coding: utf-8 -*-
import scrapy
from amazonreviews.items import AmazonreviewsItem

# exporting package list from  conda venv to req.txt
# conda list -e > req.txt
# creating a venv in  conda and installing packages from req.txt
# conda create -n new environment --file req.txt


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['web']
    start_urls = ['https://www.amazon.in/Apple-iPhone-Silver-64GB-Storage/dp/B0711T2L8K/ref=sr_1_1?pf_rd_i=1389401031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=66601440-7bcb-4e94-aaa3-7f6a21c2ed6f&pf_rd_r=73QJ3CHSR9MFVEG73A6V&pf_rd_s=center-1&pf_rd_t=101&qid=1557424649&refinements=p_89%3AApple&s=electronics&sr=1-1']

    def parse(self, response):

        # text = response.xpath(
        #     '//*[@data-hook="review-body"][1]//text() | div[@data-hook="review-collapsed"][1]//text()').extract()
        # yield {'text': text}
        # star_rating = response.xpath(
        #     '//*[@data-hook="review-star-rating"][1]//text()').re('^[0-9]')
        # yield {'star_rating': star_rating}

        item = AmazonreviewsItem()

        all_reviews_div = response.xpath('//div[@data-hook="review"]')

        # review_txt = all_reviews_div.xpath(
        #     '//*[@data-hook="review-body"]//text() | div[@data-hook="review-collapsed"]//text()')

        # rating = all_reviews_div.xpath(
        #     '//*[@data-hook="review-star-rating"]//text()')

        count = 0

        for review in range(0, len(all_reviews_div)):

            print(len(all_reviews_div))

            data = all_reviews_div[review].xpath(
                '//*[@data-hook="review-body"]//text() | div[@data-hook="review-collapsed"]//text()').extract()

            print(data)

            # item['review_txt'] = review_txt
            # item['rating'] = rating
            # yield {
            #     "review_txt": ''.join(review.xpath('//text()').extract()),
            #     "rating": ''.join(rating[count].xpath('//text()').re('^[0-9]'))

            # }
            # count = count+1
