import scrapy
import json
from espnscraper.items import BallDataItem

class ESPNCommentarySpider(scrapy.Spider):
    name = 'commentary-spider'

    allowed_domains = ['espncricinfo.com']

    start_urls = ['https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?lang=en&seriesId=1324623&matchId=1324629&inningNumber=2&commentType=ALL&sortDirection=ASC']

    def parse(self, response):
        results = json.loads(response.body)
        
        next_over = results['nextInningOver']

        comments = results['comments']

        for comment in comments:
            item = BallDataItem()

            item['overNumber'] = comment['overNumber']
            item['ballNumber'] = comment['ballNumber']
            item['totalRuns'] = comment['totalRuns']
            item['inningsRuns'] = comment['totalInningRuns']
            item['inningsWickets'] = comment['totalInningWickets']
            
            yield item