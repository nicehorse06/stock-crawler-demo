# 爬蟲demo

* target: https://cn.investing.com/equities/apple-computer-inc-historical-data

## 使用方式
* StockCrawler帶入開始和結束時間，如以下範例或`demo.py`

```python
from crawler import StockCrawler

this_crawler = StockCrawler('2021/12/20', '2022/01/20')
print(this_crawler.json_array())
```