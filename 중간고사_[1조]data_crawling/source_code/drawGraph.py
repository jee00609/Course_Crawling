import numpy as np
import requests
from guGun import returnGuGunCodeList
import matplotlib.pyplot as plt

ServiceKey = 'OpenApiServiceKey'
DecodedKey = requests.utils.unquote(ServiceKey)
URL = 'http://apis.data.go.kr/B552061/frequentzoneChild/getRestFrequentzoneChild'

def main():
    finalResult = {}
    years = [2017, 2018, 2019, 2020]
    sidoCodes = [11, 26, 27, 28, 29, 30, 31, 36, 41, 42, 43, 44, 45, 46, 47, 48, 50]

    params = {
        'serviceKey' : DecodedKey, 
        'type' : 'json', 
        'numOfRows' : '10',
        'pageNo' : '1'
    }
    
    for year in years :
        caslt = 0 # 사상자 수
        dth = 0 # 사망자 수
        se = 0 # 중상자 수
        sl = 0 # 경상자 수
        
        for sidoCode in sidoCodes :
            sigunguCodes = returnGuGunCodeList(sidoCode)
            sido_caslt = 0 
            sido_dth = 0 
            sido_se = 0 
            sido_sl = 0
            
            for sigunguCode in sigunguCodes :
                params['searchYearCd'] = year
                params['siDo'] = sidoCode
                params['guGun'] = sigunguCodes
            
                try :
                    response = requests.get(URL, params=params).json()
                    if response['resultMsg'] == 'NODATA_ERROR':
                        # print("No Data... Skip")
                        continue;
                    elif response['resultCode'] == '00' :
                        res = response['items']['item'][0]
                        # totall
                        caslt += res['caslt_cnt'] 
                        dth += res['dth_dnv_cnt'] 
                        se += res['se_dnv_cnt'] 
                        sl += res['sl_dnv_cnt'] 
                        #sido
                        sido_caslt += res['caslt_cnt'] 
                        sido_dth += res['dth_dnv_cnt'] 
                        sido_se += res['se_dnv_cnt'] 
                        sido_sl += res['sl_dnv_cnt']            
                    else:
                        raise Exception(response['resultMsg'])      
                except Exception as e:
                    print("\nData Request Fail :", e, year, sidoCode, sigunguCode)
                    return None
  
        print("✅", year, "년 전국 / 총 사상자", caslt)
        finalResult[year] = caslt

    print(finalResult)
    myList = finalResult.items()
    x, y = zip(*myList)
    
    x = np.arange(4)
    years = ['2017', '2018', '2019', '2020']
    values = [216, 250, 334, 48]
    
    plt.bar(x, values, color='#f3efec', width=0.5)
    plt.xticks(x, years)
    
    plt.xlabel('Year')
    plt.ylabel('Casualties')
    plt.show()
    
    
if __name__ == '__main__':
    main()