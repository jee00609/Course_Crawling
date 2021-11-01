import requests
from guGun import returnGuGunCodeList

ServiceKey = 'OpenApiServiceKey'
DecodedKey = requests.utils.unquote(ServiceKey)
URL = 'http://apis.data.go.kr/B552061/frequentzoneChild/getRestFrequentzoneChild'

def main():
  years = [2017, 2018, 2019, 2020]
  sidoCodes = [11, 26, 27, 28, 29, 30, 31, 36, 41, 42, 43, 44, 45, 46, 47, 48, 50]
  regionName = {
    11: '서울특별시',
    26: '부산광역시',
    27: '대구광역시',
    28: '인천광역시',
    29: '광주광역시', 
    30: '대전광역시', 
    31: '울산광역시', 
    36: '세종특별자치시', 
    41: '경기도', 
    42: '강원도', 
    43: '충청북도', 
    44: '충청남도',
    45: '전라북도', 
    46: '전라남도', 
    47: '경상북도', 
    48: '경상남도', 
    50: '제주특별자치도', 
  }
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
          print("\nData Request Fail :", e, year, regionName[sidoCode], sigunguCode)
          return None
    
      print(year,"년 /", regionName[sidoCode], "/ 총 사상자", sido_caslt, "/ 총 사망자", sido_dth, "/ 총 중상자", sido_se, "/ 총 경상자", sido_sl)
  
    print("✅", year, "년 전국 / 총 사상자", caslt, "/ 총 사망자", dth, "/ 총 중상자", se, "/ 총 경상자", sl)

if __name__ == '__main__':
  main()
  