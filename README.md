
# 中国高校微博排行

按官方微博粉丝数量进行排名。

Python 3 单文件脚本（ `run.py` ），仅依赖 [requests](https://github.com/psf/requests) 进行数据爬取。

输出样例（2021年11月25日13时34分15秒获取）：

```

排名　　　　　校名　　　　　         微博数         粉丝数
  1　　　　清华大学　　　　         19,715       519.7万
  2　　　　北京大学　　　　         31,158       472.5万
  3　　　　复旦大学　　　　         14,981       381.8万
  4　　　　武汉大学　　　　         32,990       318.9万
  5　　　上海交通大学　　　         44,530       308.8万
  6　　　　浙江大学　　　　         30,348       272.8万
  7　　　西安交通大学　　　         31,563       198.4万
  8　　　华中科技大学　　　         24,518       145.6万
  9　　　　南开大学　　　　         31,417       136.8万
 10　　　　厦门大学　　　　         31,145       133.0万
 11　　　　天津大学　　　　         45,241       132.8万
 12　　哈尔滨工业大学　　　          7,713       123.9万
 13　　　　四川大学　　　　         25,221        93.1万
 14　　　　同济大学　　　　         21,302        83.2万
 15　　　中国人民大学　　　          3,287        82.0万
 16　　北京航空航天大学　　          2,557        75.4万
 17　　中国科学技术大学　　         15,774        74.9万
 18　　　　中山大学　　　　         16,574        72.1万
 19　　　　南京大学　　　　         28,017        70.6万
 20　　　　郑州大学　　　　         37,597        67.8万
 21　　　　东南大学　　　　         22,825        55.9万
 22　　　北京交通大学　　　         18,283        46.4万
 23　　南京航空航天大学　　         12,031        22.5万
 24　　　　牛津大学　　　　            573         9.1万

```

目前高校数量：24。如需添加，可在 issue 中提出。

（本 README 由 GitHub Actions 运行 run.py 自动生成）
