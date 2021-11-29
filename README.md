
# 中国高校微博排行

按官方微博粉丝数量进行排名。

Python 3 单文件脚本（ `run.py` ），仅依赖 [requests](https://github.com/psf/requests) 进行数据爬取。

输出样例（2021年11月29日13时34分47秒获取）：

```

排名　　　　　校名　　　　　         微博数         粉丝数
  1　　　　清华大学　　　　         19,770       519.8万
  2　　　　北京大学　　　　         31,224       472.5万
  3　　　　复旦大学　　　　         15,020       381.7万
  4　　　　武汉大学　　　　         33,082       318.8万
  5　　　上海交通大学　　　         44,578       308.8万
  6　　　　浙江大学　　　　         30,350       273.0万
  7　　　西安交通大学　　　         31,610       198.3万
  8　　　华中科技大学　　　         24,548       145.5万
  9　　　　南开大学　　　　         31,443       136.8万
 10　　　　厦门大学　　　　         31,191       133.0万
 11　　　　天津大学　　　　         45,302       132.8万
 12　　哈尔滨工业大学　　　          7,719       123.9万
 13　　　　四川大学　　　　         25,266        93.1万
 14　　　　同济大学　　　　         21,350        83.2万
 15　　　中国人民大学　　　          3,288        82.1万
 16　　北京航空航天大学　　          2,567        75.4万
 17　　中国科学技术大学　　         15,811        74.8万
 18　　　　中山大学　　　　         16,586        72.1万
 19　　　　南京大学　　　　         28,066        70.6万
 20　　　　郑州大学　　　　         37,678        67.9万
 21　　　　东南大学　　　　         22,861        55.9万
 22　　　北京交通大学　　　         18,322        46.4万
 23　　南京航空航天大学　　         12,033        22.5万
 24　　　　牛津大学　　　　            573         9.1万

```

目前高校数量：24。如需添加，可在 issue 中提出。

（本 README 由 GitHub Actions 运行 run.py 自动生成）
