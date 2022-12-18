# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BallDataItem(scrapy.Item):
    inning = scrapy.Field()
    overNumber = scrapy.Field()
    ballNumber = scrapy.Field()
    totalRuns = scrapy.Field()
    inningsRuns = scrapy.Field()
    inningsWickets = scrapy.Field()