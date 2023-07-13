import datetime
now = datetime.datetime.now()
week_day = now.isoweekday()
if week_day in (6,7):
    pass
else:
    import requests
    import re
    import os
    from random import randint
    url = r'https://image.baidu.com/search/acjson?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/95.0.4638.69 Safari/537.36'
    }
    keyword = '午餐美食特写'
    pn = 1 + randint(30,1000)
    param = {
            'tn': 'resultjson_com',
            'logid': '11930718112558637704',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': '',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': '1',
            'fr': '',
            'expermode': '',
            'force': '',
            'cg': '',    # 这个参数没公开，但是不可少
            'pn': pn,    # 显示：30-60-90 代表从第几张图片开始获取
            'rn': '30',  # 每页显示 30 条
            'gsm': '1e',
            '1618827096642': ''  
    }
    request = requests.get(url=url, headers=headers, params=param)
    if request.status_code == 200:
        print('Request success.')
    request.encoding = 'utf-8'
    html = request.text
    image_url_list = re.findall('"thumbURL":"(.*?)",', html, re.S)
    # print(image_url_list)
    save_dir = r'D:/crawl_picture'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    n = randint(0,29)
    image_url = image_url_list[n]
    image_data = requests.get(url=image_url, headers=headers).content
    with open(os.path.join(save_dir, 'picture.jpg'), 'wb') as fp:
        fp.write(image_data)

    #利用企微机器人发送图片
    import hashlib, base64
    import json
    import requests
    a = '天天神券https://market.waimai.meituan.com/gd/single.html?el_biz=waimai&el_page=gundam.loader&activity_id=240561&tenant=gundam&gundam_id=1r1I80&click_cps_url=https%3A%2F%2Fclick.meituan.com%2Ft%3Ft%3D1%26c%3D2%26p%3DqmdlRL5z_oKQ'
    #机器人链接
    jiqiren_url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e47d30ab-4359-4c4a-85a7-e1ad112c802f'

    file_image = open(r'D:\crawl_picture\picture.jpg','rb').read()
    is_f = base64.b64encode(file_image)     #根据企微api的要求，要把图片编成 base64 编码
    md5 = hashlib.md5(file_image)       #也是根据企微api要求来编码
    data = {
        'msgtype':'image',
        'image':{
            'base64':is_f.decode('utf-8'),
            'md5':md5.hexdigest()
                }
            }
    
    data2 = {
    "msgtype": "text",
        "text": {
        "content": a,
        "mentioned_list":["@all"]
        # "mentioned_list":["wangqing","@all"],
        # "mentioned_mobile_list":["13800001111","@all"]
    }
    }
    requests.post(jiqiren_url,data=json.dumps(data))        #机器人发送图片
    requests.post(jiqiren_url,data=json.dumps(data2))