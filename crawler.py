import requests
from urllib import parse
from bs4 import BeautifulSoup

class StockCrawler():
    targe_url = 'https://cn.investing.com/instruments/HistoricalDataAjax'
    payloadData = {
        'curr_id': 6408,
        'smlID': 1159963,
        'header': 'AAPL历史数据',
        'interval_sec': 'Daily',
        'sort_col': 'date',
        'sort_ord': 'DESC',
        'action': 'historical_data'
    }

    payloadHeader = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest'
    }

    def __init__(self, start_date, end_date) -> None:
        self.payloadData['st_date'] = start_date
        self.payloadData['end_date'] = end_date

    def request_data(self):
        r = requests.post(self.targe_url, data=parse.urlencode(self.payloadData), headers=self.payloadHeader)
        return r
    
    def soup_data(self):
        r = self.request_data()
        if not r.ok:
            return None

        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        return soup

    def json_array(self):
        result = []
        soup = self.soup_data()

        if not soup:
            return None
        
        # 第一筆跟最後一筆不需要
        for i in range(1, len(soup.find_all('tr'))-1):
            this_tr_all_td = soup.find_all('tr')[i].find_all('td')
            this_date = this_tr_all_td[0].text
            this_price = this_tr_all_td[1].text
            result.append(f'{this_date}: {this_price}')
        
        return result
