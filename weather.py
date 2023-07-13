import datetime
now = datetime.datetime.now()
week_day = now.isoweekday()
if week_day in (6,7):
    pass
else:
    from datetime import datetime
    if int(datetime.today().strftime('%H')) < 19:
        import requests
        import json
        url = 'https://restapi.amap.com/v3/weather/weatherInfo?city=310000&key=a354a690323557e4bf62731bab4ee0d1&extensions=all'
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
                'Content-Type': 'application/json;charset=UTF-8'}
        response = requests.get(url)
        res = response.text
        res = json.loads(res)
        forecasts = res['forecasts'][0]
        casts = forecasts['casts'][0] 
        a = '城市：%s'%forecasts['city'] + '\n' + '日期：%s'%casts['date'] + '\n' + '白天天气现象:%s'%casts['dayweather'] \
            + '\n' + '晚上天气现象:%s'%casts['nightweather'] + '\n' + '白天温度：%s'%casts['daytemp'] + '\n' + \
                '晚上温度%s'%casts['nighttemp'] + '\n' + '白天风向：%s'%casts['daywind']  + '\n' + '晚上风向：%s'%casts['nightwind'] \
                    + '\n' + '白天风力：%s'%casts['daypower']  + '\n' + '晚上风力：%s'%casts['daypower'] 
    else:
        # a = '要来一杯咖啡吗？'
        # a = '测试一下'
         pass
    #利用企微机器人发送文字
    import hashlib, base64
    import json
    import requests
    #机器人链接
    jiqiren_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f77f51f5-a904-4aa6-bba5-ad753f59e0f6'
    # jiqiren_url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e47d30ab-4359-4c4a-85a7-e1ad112c802f'
    data = {
        "msgtype": "text",
        "text": {
            "content": a,
            "mentioned_list":["@all"]
            # "mentioned_list":["wangqing","@all"],
            # "mentioned_mobile_list":["13800001111","@all"]
        }
    }
    requests.post(jiqiren_url,data = json.dumps(data)) 