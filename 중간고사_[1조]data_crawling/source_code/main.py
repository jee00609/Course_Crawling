import json
import pandas as pd
import requests
from guGun import returnGuGunCodeList

ServiceKey = 'OpenApiServiceKey'

DecodedKey = requests.utils.unquote(ServiceKey)
URL = 'http://apis.data.go.kr/B552061/frequentzoneChild/getRestFrequentzoneChild'

#[CODE 2] : response에서 필요한 데이터 추출 및 json 형태로 리턴
def getFileDataFromResult(searchYearCd, response):
  res = response['items']['item'][0]
  jsonResult = {
    'searchYearCd': searchYearCd,
    'spot_nm': res['spot_nm'],
    'occrrnc_cnt': res['occrrnc_cnt'],
    'caslt_cnt': res['caslt_cnt'],
    'dth_dnv_cnt': res['dth_dnv_cnt'],
    'se_dnv_cnt': res['se_dnv_cnt'],
    'sl_dnv_cnt': res['sl_dnv_cnt'],
    'wnd_dnv_cnt': res['wnd_dnv_cnt']
  }
  ListResult = [
    searchYearCd, 
    res['spot_nm'], 
    res['occrrnc_cnt'], 
    res['caslt_cnt'],
    res['dth_dnv_cnt'],
    res['se_dnv_cnt'],
    res['sl_dnv_cnt'],
    res['wnd_dnv_cnt']
  ]
  return (jsonResult, ListResult)

#[CODE 1] : URL request
def getFrequentzoneChildData(searchYearCd, siDo):
  forJsonFile = []
  forCsvFile = []
  sigunguCodes = returnGuGunCodeList(siDo)
  params = {
    'serviceKey' : DecodedKey, 
    'searchYearCd' : searchYearCd, 
    'siDo' : siDo, 
    'type' : 'json', 
    'numOfRows' : '10',
    'pageNo' : '1'
  }

  try:
    for code in sigunguCodes:
      print("\n...Fetching Data... : ", code)
      params['guGun'] = code
      response = requests.get(URL, params=params).json() # bytes to Json
      
      if response['resultMsg'] == 'NODATA_ERROR':
        print('\nNo Data, Continue :', code, '\n')
        continue;
      elif response['resultCode'] == '00' :
        print('\nData Request Success :', code, '\n')
        
        # Call [CODE 2] to filter & format data 
        jsonResult, ListResult = getFileDataFromResult(searchYearCd, response)

        forJsonFile.append(jsonResult)
        forCsvFile.append(ListResult)
      else:
        raise Exception(response['resultMsg'])
  except Exception as e:
    print("\nData Request Fail :", e)
    return None
  
  return (forJsonFile, forCsvFile)

#[CODE 0]
def main():
    jsonResult = []
    result = []

    searchYearCd = int(input('조회하고자 하는 연도값 입력 : '))
    print(
        '\n서울특별시 11, 부산광역시 26, 대구광역시 27, 인천광역시 28, 광주광역시 29, 대전광역시 30, 울산광역시 31, 세종특별자치시 36, 경기도 41, 강원도 42, 충청북도 43, 충청남도 44, 전라북도 45, 전라남도 46, 경상북도 47, 경상남도 48, 제주특별자치도 50'
    )
    siDo = int(input('# 시도 코드 : '))

    #1. Call [CODE 1] to get data
    jsonResult, result = getFrequentzoneChildData(searchYearCd, siDo)
    print("Finished requesting Data : \n", jsonResult, "\n",result)

    #2. Save data into CSV & Json file
    # Json File
    with open('./어린이 사고 다발 지역 정보_%d_%s.json' % (searchYearCd, siDo), 'w', encoding='utf8') as outfile:
      jsonFile = json.dumps(jsonResult, sort_keys=True, ensure_ascii=False)
      outfile.write(jsonFile)

    # CSV File
    columns = ["조회연도", "지점명", "발생건수", "사상자수", "사망자수", "중상자수", "경상자수", "부상신고자수"]
    result_df = pd.DataFrame(result, columns=columns)
    result_df.to_csv('./어린이 사고 다발 지역 정보_%d_%s.csv' % (searchYearCd, siDo), index=False, encoding='cp949')

if __name__ == '__main__':
    main()