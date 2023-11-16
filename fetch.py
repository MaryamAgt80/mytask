import json
import urllib.request
import pandas

def go_and_extract(url):
    with urllib.request.urlopen(url) as content:
        allfile = json.loads(content.read())
        listdata = allfile['series'][0]
        data = listdata['data']
        date=[]
        x=[]
        y=[]
        percentChange=[]
        change=[]
        for item in data:
            date.append(item['date'])
            x_item=item['x']
            x.append(x_item[:-4ُ])
            y.append(item['y'])
            percentChange.append(item['percentChange'])
            change.append(item['change'])
        return {'date':date,'x':x,'y':y,'percentChange':percentChange,'change':change}

def save_data(data_list,x_data,y_data,percentChange_list,change_list,FileName):
    datadictionary = {
        'date': data_list,
        'x': x_data,
        'y': y_data,
        'percentChange': percentChange_list,
        'change': change_list
    }
    df = pandas.DataFrame(datadictionary)
    df.to_csv(FileName, mode='a', index=False, header=False)



def request_urls(urls,FileName):
    date_list = []
    x_list = []
    y_list = []
    percentChange_list = []
    change_list = []
    for url in urls:
        AllListData=go_and_extract(url)
        date_list.extend(AllListData['date'])
        x_list.extend(AllListData['x'])
        y_list.extend(AllListData['y'])
        percentChange_list.extend(AllListData['percentChange'])
        change_list.extend(AllListData['change'])
    save_data(date_list,x_list,y_list,percentChange_list,change_list,FileName)
    print(f'data saved in {FileName}')




urls_USDJPG=['https://markets.tradingeconomics.com/chart/usdjpy:cur?d1=2020-11-16&d2=2021-11-15&interval=1d&securify=new&url=/japan/currency&AUTH=xSc2nXdhvZYw1SUkF64CRsxV6fsakHwO880xDBoHFFbJoAnRinsjtOEkaQK803Ua&ohlc=0',
      'https://markets.tradingeconomics.com/chart/usdjpy:cur?d1=2021-11-16&d2=2022-11-15&interval=1d&securify=new&url=/japan/currency&AUTH=xSc2nXdhvZYw1SUkF64CRsxV6fsakHwO880xDBoHFFbJoAnRinsjtOEkaQK803Ua&ohlc=0',
      'https://markets.tradingeconomics.com/chart/usdjpy:cur?interval=1d&span=1y&securify=new&url=/japan/currency&AUTH=NROp%2BqryE%2BOz6h6xipY6ZlOGqWuD5stKAPSYUeuC8R95%2BCL9lPLKOKlbJZW6me%2BO&ohlc=0']
urls_USDBonds=[
    'https://markets.tradingeconomics.com/chart/usgg10yr:ind?d1=2020-11-16&d2=2021-11-15&interval=1d&securify=new&url=/united-states/government-bond-yield&AUTH=trj8tp9TPvDZ9t1jvwMasM1NfcaA5pw5fX%2FNoM7hvueYdTA1VRY60jAIcMqAW4e%2B%2BEMaJMKlnPhyM93qKQmwqA%3D%3D&ohlc=0',
    'https://markets.tradingeconomics.com/chart/usgg10yr:ind?d1=2021-11-16&d2=2022-11-15&interval=1d&securify=new&url=/united-states/government-bond-yield&AUTH=trj8tp9TPvDZ9t1jvwMasM1NfcaA5pw5fX%2FNoM7hvueYdTA1VRY60jAIcMqAW4e%2B%2BEMaJMKlnPhyM93qKQmwqA%3D%3D&ohlc=0',
    'https://markets.tradingeconomics.com/chart/usgg10yr:ind?interval=1d&span=1y&securify=new&url=/united-states/government-bond-yield&AUTH=trj8tp9TPvDZ9t1jvwMasM1NfcaA5pw5fX%2FNoM7hvueYdTA1VRY60jAIcMqAW4e%2B%2BEMaJMKlnPhyM93qKQmwqA%3D%3D&ohlc=0'
]
urls_JAPBonds=[
    'https://markets.tradingeconomics.com/chart/gjgb10:ind?d1=2020-11-16&d2=2021-11-15&interval=1d&securify=new&url=/japan/government-bond-yield&AUTH=trj8tp9TPvDZ9t1jvwMasHVFcx1ET4kttgfxAGUk28fTxE9%2BSN%2BN207deygbWXO0&ohlc=0',
    'https://markets.tradingeconomics.com/chart/gjgb10:ind?d1=2021-11-16&d2=2022-11-15&interval=1d&securify=new&url=/japan/government-bond-yield&AUTH=trj8tp9TPvDZ9t1jvwMasHVFcx1ET4kttgfxAGUk28fTxE9%2BSN%2BN207deygbWXO0&ohlc=0',
    'https://markets.tradingeconomics.com/chart/gjgb10:ind?interval=1d&span=1y&securify=new&url=/japan/government-bond-yield&AUTH=trj8tp9TPvDZ9t1jvwMasHVFcx1ET4kttgfxAGUk28fTxE9%2BSN%2BN207deygbWXO0&ohlc=0'
]

FileName=''
request_urls(urls_USDJPG,FileName)