# Project10-12306-Web-of-Science-Crawler
README.md：说明
config.ini：登录名、密码等的配置文件
hack12306.py：主程序
city_code.txt：城市中文名称与三字码对应文件

# Function Introduction
hack12306.py 是一个 Python 3.x 版的12306.cn订票程序。执行程序，等待浏览器页面跳出后输入验证码点击登录，即可完成自动购票。

支持的功能：
    1、支持配置出发地、目的地、乘车日
    2、支持配置车次类型（动车、高铁等）
    3、支持配置出发时间
    4、需要手动输入登录验证码
    5、支持配置预定车次的选择顺序（使用order字段配置，数字0：从上至下选择；数字x（1、2、3、4...）：车次从上到下的序号，配置2表示列表中的第二个车次）
    6、支持预定、购票自动完成	
    7、支持配置文件路径指定
    8、支持席别指定
    9、支持是否允许分配无座

# Config
直接修改 hack12306.py 当前目录下的config.ini 或者 拷贝一份 config.ini 到任意目录，在执行时指定绝对路径

    特别说明：
        1、[cookieInfo]中starts和ends为中文名称

# Run
方式一：直接运行（配置文件使用hack12306.py相同目录下的config.ini）
	python hack12306.py

方式二：指定config.ini路径（配置文件使用指定的config.ini）
	python hack12306.py -c /Users/xxx/config.ini

	参数说明：
		'-c', '--config', '可选参数, 指定配置文件, 默认使用当前目录 config.ini'
