
# 中国高校微博排行

按官方微博粉丝数量进行排名。

Python 3 单文件脚本（ `run.py` ），仅依赖 [requests](https://github.com/psf/requests) 进行数据爬取。

输出样例（2021年12月10日13时34分57秒获取）：

```

排名　　　　　校名　　　　　         微博数         粉丝数
  1　　　　清华大学　　　　         19,946       520.6万
  2　　　　北京大学　　　　         31,416       472.9万
  3　　　　复旦大学　　　　         15,149       381.6万
  4　　　　武汉大学　　　　         33,240       318.7万
  5　　　上海交通大学　　　         44,722       308.6万
  6　　　　浙江大学　　　　         30,371       273.0万
  7　　　西安交通大学　　　         31,730       199.5万
  8　　　华中科技大学　　　         24,645       145.5万
  9　　　　南开大学　　　　         31,526       136.8万
 10　　　　厦门大学　　　　         31,336       133.0万
 11　　　　天津大学　　　　         45,471       132.8万
 12　　哈尔滨工业大学　　　          7,744       123.9万
 13　　　　四川大学　　　　         25,386        93.3万
 14　　　　同济大学　　　　         21,498        83.6万
 15　　　中国人民大学　　　          3,296        82.2万
 16　　北京航空航天大学　　          2,596        75.5万
 17　　中国科学技术大学　　         15,912        74.8万
 18　　　　中山大学　　　　         16,622        72.2万
 19　　　　南京大学　　　　         28,198        70.6万
 20　　　　郑州大学　　　　         37,906        67.9万
 21　　　　东南大学　　　　         22,962        55.9万
 22　　　北京交通大学　　　         18,431        46.4万
 23　　南京航空航天大学　　         12,036        22.5万
 24　　　　牛津大学　　　　            574         9.1万

```

目前高校数量：24。如需添加，可在 issue 中提出。

（本 README 由 GitHub Actions 运行 run.py 自动生成）
