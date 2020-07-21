# 中国高校微博排行

按官方微博粉丝数量进行排名。

Python 3 单文件脚本（ `run.py` ），仅依赖 [requests](https://github.com/psf/requests) 进行数据爬取。

输出样例（2020年7月21日获取）：

```
排名　　　　　校名　　　　　         微博数         粉丝数
   1　　　　清华大学　　　　         14,327      4,101,267
   2　　　　北京大学　　　　         26,441      3,379,561
   3　　　　复旦大学　　　　         11,786      2,818,485
   4　　　上海交通大学　　　         38,259      2,640,552
   5　　　　武汉大学　　　　         26,501      2,070,633
   6　　　西安交通大学　　　         27,828      1,968,086
   7　　　　浙江大学　　　　         27,362      1,629,448
   8　　　　天津大学　　　　         36,048      1,185,691
   9　　　华中科技大学　　　         20,853      1,184,846
  10　　　　南开大学　　　　         26,605      1,128,254
  11　　　　厦门大学　　　　         24,782      1,110,924
  12　　哈尔滨工业大学　　　          6,256        753,409
  13　　北京航空航天大学　　          1,956        749,614
  14　　　　四川大学　　　　         19,887        688,042
  15　　　　同济大学　　　　         15,636        670,854
  16　　　　中山大学　　　　         13,966        668,500
  17　　　中国人民大学　　　          2,920        660,761
  18　　　　郑州大学　　　　         29,644        614,000
  19　　　　南京大学　　　　         23,152        517,285
  20　　中国科学技术大学　　         12,085        382,920
  21　　　　东南大学　　　　         18,025        355,639
  22　　　北京交通大学　　　         13,412        286,505
  23　　南京航空航天大学　　         11,781        150,890
  24　　　　牛津大学　　　　            549         80,637
```

目前高校数量：24。如需添加，可在 issue 中提出。