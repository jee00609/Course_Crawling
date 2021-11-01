import requests

ServiceKey = 'OpenApiServiceKey'
DecodedKey = requests.utils.unquote(ServiceKey)
URL = 'http://apis.data.go.kr/B552061/frequentzoneChild/getRestFrequentzoneChild'

def main():
  years = [2017, 2018, 2019, 2020]
  params = {
    'serviceKey' : DecodedKey, 
    'type' : 'json', 
    'numOfRows' : '10',
    'pageNo' : '1',
    'siDo' : 11
  }
  sigunguNames = {
    680 : '강남구',
    740 : '강동구',
    305 : '강북구',
    500 : '강서구',
    620 : '관악구',
    215 : '광진구',
    530 : '구로구',
    545 : '금천구',
    350 : '노원구',
    320 : '도봉구',
    230 : '동대문구',
    590 : '동작구',
    440 : '마포구',
    410 : '서대문구',
    650 : '서초구',
    200 : '성동구',
    290 : '성북구',
    710 : '송파구',
    470 : '양천구',
    560 : '영등포구',
    170 : '용산구',
    380 : '은평구',
    110 : '종로구',
    140 : '중구',
    260 : '중랑구',
  }

  for year in years :
    print("########## ",year," ##########")
    for sigunguCode in sigunguNames.keys() :
      caslt = 0 # 사상자 수
      dth = 0 # 사망자 수
      se = 0 # 중상자 수
      sl = 0 # 경상자 수    
      params['searchYearCd'] = year
      params['guGun'] = sigunguCode
      try :
        response = requests.get(URL, params=params).json()
        if response['resultMsg'] == 'NODATA_ERROR':
          # print("No Data... Skip")
          continue;
        elif response['resultCode'] == '00' :
          res = response['items']['item'][0]
          caslt += res['caslt_cnt'] 
          dth += res['dth_dnv_cnt'] 
          se += res['se_dnv_cnt'] 
          sl += res['sl_dnv_cnt']            
        else:
          raise Exception(response['resultMsg'])      
      except Exception as e:
        print("\nData Request Fail :", e, year, sigunguCode)
        return None
      print(sigunguNames[sigunguCode], "사상자", caslt, "/ 사망자", dth, "/ 중상자", se, "/ 경상자", sl)
  

if __name__ == '__main__':
  main()
  