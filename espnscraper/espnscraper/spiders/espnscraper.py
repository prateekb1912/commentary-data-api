import scrapy
import json
from espnscraper.items import BallDataItem

class ESPNCommentarySpider(scrapy.Spider):
    name = 'commentary-spider'

    allowed_domains = ['espncricinfo.com']

    start_urls = [f'https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?lang=en&seriesId=1324623&matchId=1324629&inningNumber={inn_num}&commentType=ALL&sortDirection=ASC&fromInningOver={over_num}' for inn_num in range(1,3) for over_num in range(1,20,2)]

    def parse(self, response):
        results = json.loads(response.body)
        
        comments = results['comments']

        print(results['nextInningOver'])

        for comment in comments:
            item = BallDataItem()

            item['inning'] = comment['inningNumber']
            item['overNumber'] = comment['overNumber']
            item['ballNumber'] = comment['ballNumber']
            item['totalRuns'] = comment['totalRuns']
            item['inningsRuns'] = comment['totalInningRuns']
            item['inningsWickets'] = comment['totalInningWickets']

            yield item