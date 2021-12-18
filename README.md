
# 中国高校微博排行

按官方微博粉丝数量进行排名。

Python 3 单文件脚本（ `run.py` ），仅依赖 [requests](https://github.com/psf/requests) 进行数据爬取。

输出样例（2021年12月18日13时34分41秒获取）：

```

排名　　　　　校名　　　　　         微博数         粉丝数
  1　　　　清华大学　　　　         20,076       520.6万
  2　　　　北京大学　　　　         31,567       472.9万
  3　　　　复旦大学　　　　         15,218       381.4万
  4　　　　武汉大学　　　　         33,328       318.8万
  5　　　上海交通大学　　　         44,827       308.5万
  6　　　　浙江大学　　　　         30,387       272.9万
  7　　　西安交通大学　　　         31,812       200.2万
  8　　　华中科技大学　　　         24,720       145.4万
  9　　　　南开大学　　　　         31,587       136.9万
 10　　　　厦门大学　　　　         31,443       133.1万
 11　　　　天津大学　　　　         45,599       132.8万
 12　　哈尔滨工业大学　　　          7,760       123.9万
 13　　　　四川大学　　　　         25,474        93.4万
 14　　　　同济大学　　　　         21,595        83.7万
 15　　　中国人民大学　　　          3,300        82.3万
 16　　北京航空航天大学　　          2,628        75.5万
 17　　中国科学技术大学　　         15,992        74.8万
 18　　　　中山大学　　　　         16,649        72.3万
 19　　　　南京大学　　　　         28,298        70.7万
 20　　　　郑州大学　　　　         38,057        67.9万
 21　　　　东南大学　　　　         23,027        55.9万
 22　　　北京交通大学　　　         18,524        46.4万
 23　　南京航空航天大学　　         12,046        22.5万
 24　　　　牛津大学　　　　            575         9.2万

```

目前高校数量：24。如需添加，可在 issue 中提出。

（本 README 由 GitHub Actions 运行 run.py 自动生成）
