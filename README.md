# 爬蟲demo

* target: https://cn.investing.com/equities/apple-computer-inc-historical-data

## 使用方式
* `pip install -r requirement.txt`
* `python demo.py`，執行範例code
* 使用爬蟲`StockCrawler`的方式如下，需帶入開始和結束時間，時間格式為YYYY/MM/DD

```python
from crawler import StockCrawler

this_crawler = StockCrawler('2021/12/20', '2022/01/20')
print(this_crawler.json_array())
```