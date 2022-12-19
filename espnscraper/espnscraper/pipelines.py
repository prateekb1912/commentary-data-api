# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class SqlitePipeline:
    def __init__(self):
        self.conn = sqlite3.connect('cricinfo.db')
        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS comments(
            inning INT,
            over INT,
            ball INT,
            runs INT,
            innRuns INT,
            innWkts INT
        )
        """)

    def process_item(self, item, spider):
        
        self.cur.execute("""
            INSERT INTO comments(inning, over, ball, runs, innRuns, innWkts) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, list(item.values()))

        self.conn.commit()
        return item
