
# 中国高校微博排行

按官方微博粉丝数量进行排名。

Python 3 单文件脚本（ `run.py` ），仅依赖 [requests](https://github.com/psf/requests) 进行数据爬取。

输出样例（2021年12月01日13时35分31秒获取）：

```

排名　　　　　校名　　　　　         微博数         粉丝数
  1　　　　清华大学　　　　         19,798       520.1万
  2　　　　北京大学　　　　         31,264       472.7万
  3　　　　复旦大学　　　　         15,047       381.7万
  4　　　　武汉大学　　　　         33,114       318.8万
  5　　　上海交通大学　　　         44,606       308.8万
  6　　　　浙江大学　　　　         30,351       273.0万
  7　　　西安交通大学　　　         31,631       198.3万
  8　　　华中科技大学　　　         24,564       145.5万
  9　　　　南开大学　　　　         31,457       136.8万
 10　　　　厦门大学　　　　         31,216       133.0万
 11　　　　天津大学　　　　         45,330       132.8万
 12　　哈尔滨工业大学　　　          7,723       123.9万
 13　　　　四川大学　　　　         25,289        93.1万
 14　　　　同济大学　　　　         21,372        83.2万
 15　　　中国人民大学　　　          3,289        82.1万
 16　　北京航空航天大学　　          2,573        75.4万
 17　　中国科学技术大学　　         15,836        74.8万
 18　　　　中山大学　　　　         16,591        72.1万
 19　　　　南京大学　　　　         28,089        70.6万
 20　　　　郑州大学　　　　         37,723        67.9万
 21　　　　东南大学　　　　         22,879        55.9万
 22　　　北京交通大学　　　         18,345        46.4万
 23　　南京航空航天大学　　         12,033        22.5万
 24　　　　牛津大学　　　　            573         9.1万

```

目前高校数量：24。如需添加，可在 issue 中提出。

（本 README 由 GitHub Actions 运行 run.py 自动生成）
