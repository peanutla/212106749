import random
import time
import requests
import urllib3
import datetime
# 用Fiddler爬取用户代理
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
}
# 商品地址
url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/7c1208da-907a-4391-9901-35a60096a3f9/99bbbca0-45cf-4a34-926c-e8ce39330a1e'

# 根据url申请请求头
def getPupu():
    # 设计获取价格波动时间

    result = requests.get(url, headers=headers, verify=False)
    return result
    randoms=random.randint(2,6)
    time.sleep(randoms)

# 运用json方法解析字典
result = getPupu()
food = result.json()
Puname = food['data']['name']
Spec = food['data']['spec']
Price = food['data']['price']/100
market_price = food['data']['market_price']/100
title = food['data']['share_content']

# 输出商品信息
print("-------------------商品: "+Puname+"-------------------------------")
print("规格: "+Spec)
print("价格: "+str(Price))
print("原价/折扣价: "+str(market_price)+"/"+str(Price) )
# print("详细内容: "+title)
print("-------------------------商品: "+Puname+"的价格波动--------------------------------")

# while()循环记录价格波动
if __name__ == '__main__':
    while (1):
        result = getPupu()
        Price = food['data']['price']
        time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print("当前时间为" +time+ ", 价格为" + str(Price/100))
