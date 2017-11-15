import urllib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def getinfo():
    
    area_list = []
    
    no2_list = []
    
    so2_list = []
    
    co_list = []
    
    o3_list = []
    
    pm10_list = []
    
    pm25_list = []
    
    print('合肥：340100，淮北 ：340600，亳州：341600，宿州：341300，蚌埠：340300，\
          阜阳：341200，淮南：340400，滁州：341100，六安：341500，马鞍山：340500，\
          芜湖：340200，宣城：341800，铜陵：340700，池州：341700，安庆：340800，黄山：341000')
    
#    city = input('请输入城市代码')
#    
#    print(type(city))
#    
#    date1 = input('请输入开始日期，例如：2017-01-22')
#    
#    print(type(date1))
#    
#    date2 = input('请输入结束日期,例如：2017-11-18')
#    
#    print(type(date2))
    city = 340600
    
    date1 = '2017-11-12'
    
    date2 = '2017-11-15'
    
    
   
    url = 'http://www.aepb.gov.cn/pages/Aepb15_SJZX_List.aspx?CityCode={citycode}&LX=4&KSSJ={start}%2023&JSSJ={end}%2023'.format(citycode = city,start = date1,end = date2)
    
    print(url)
    
    totalpages = str(urllib.request.urlopen(url).read(),encoding = 'utf-8').split("<font color='red'>")[1].split("</font>")[0]
    
    print(totalpages)
    
    print(type(totalpages))
    
    totalpages = int(totalpages)
    
    print(type(totalpages))
    
    for page in range(1,totalpages+1):
        
        url =  'http://www.aepb.gov.cn/pages/Aepb15_SJZX_List.aspx?CityCode={citycode}&LX=4&KSSJ={start}%2023&JSSJ={end}%2023&page={page}'.format(citycode = city,start = date1,end = date2,page = page)
        html = str(urllib.request.urlopen(url).read(),encoding = 'utf-8').split('<td algin="center" height="26px">')[1:]
        for i in html:
            index = i.find('algin="center">')
            if index < 0:
                area_list.append(i.split('</td>')[0].split('\r\n')[1])
                continue
            
            data_list = i.split('</td>')
            
            no2_list.append(data_list[0].split('\r\n')[1])
            
            so2_list.append(data_list[1].split('">')[1].split('\r\n')[1])
            
            co_list.append(data_list[2].split('">')[1].split('\r\n')[1])
            
            o3_list.append(data_list[3].split('">')[1].split('\r\n')[1])
            
            pm10_list.append(data_list[4].split('">')[1].split('\r\n')[1])
            
            pm25_list.append(data_list[5].split('">')[1].split('\r\n')[1])
            
            
           
            
                
            
                
            
            
            
            
#            area_list.append(i.split('</td>')[0])
            
            
        
            
        
#        print(url)
        
#        print(html)
            
#    print(area_list,len(area_list))
#    print(no2_list,len(no2_list))
#    
#    print(so2_list, len(so2_list))
            
            
            
    df = pd.DataFrame([area_list, no2_list, so2_list, co_list, o3_list, pm10_list, pm25_list]).T
    df.to_csv('edata.csv', index = False, header = False)
    print('success')
#        
        
    
    
#    html = str(urllib.request.urlopen(url).read(),encoding = 'utf-8')
#    html =  str(urllib.request.urlopen(url).read(),encoding = 'utf-8').split('data-hippo-type="shop" title="')[1:]
    
    


    
    
    
    
    
    
    

getinfo()