import requests

While True:
    city = input("请输入城市名：")
    if not city:
        break

    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
    print(req.text)
