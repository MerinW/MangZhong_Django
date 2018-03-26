# MangZhong_Django
my first django project 2017-9-12

功能需求概述
建立webgis平台实现农产品的实时动态展示，信息的查询搜索，问题的及时上传数据的及时共享，对于数据利用专业模型进行多种方面的分析，进而能够为农业决策提供一定依据。
重点功能说明

注册登录子系统

普通用户可以直接通过邮箱进行注册登录，后面也可以通过邮箱找回密码，管理员登录界面和用户使用同一入口，管理员账号由开发者指定。
管理员：进入单独的管理后台界面，可以对全部用户进行操作，并自动生成日志记录，对不同管理员可进行分组，分别设置权限。用户个人中心
用户可在注册后进入个人中心对信息进行修改，此时可以上传自己的土地数据，农产品数据，以及对地块信息进行修改等。

数据分析子系统
提供多种查询检索方式，如属性查询、条件检索、空间查询、SQL查询、缓冲区分析等等。通过选择或输入查询条件，或在电子地图选取查询区域范围上实现查询。
1.历年数据查询分析：根据获得的数据进行处理，发布为服务，通过专题地图的方式进行渲染。
2.价格分析。农业生产中很关键的一环就是价格，我们每天获取国家政府部门发布的价格，将不同产品的价格，以及同种产品在不同地区的价格进行可