## 도로 교통 공단 보행 어린이 사고 다발 지역 정보 서비스
[도로 교통 공단 보행 어린이 사고 다발 지역 정보 서비스 URL](https://www.data.go.kr/data/15058925/openapi.do)

## 참고하는 자료 URL
[URL](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000297)

## 요청변수(Request Parameter)

* ServiceKey
* searchYearCd 
* siDo
* guGun
* type
* numOfRows
* pageNo

## 출력결과(Response Element)

* 시도시군구명 (sido_sgg_nm) 
* 지점명 (spot_nm) 
* 발생건수 (occrrnc_cnt) 
* 사상자수 (caslt_cnt) 
* 사망자수 (dth_dnv_cnt) 
* 중상자수 (se_dnv_cnt) 
* 경상자수 (sl_dnv_cnt) 
* 부상신고자수 (wnd_dnv_cnt) 
* 경도 (lo_crd)
* 위도 (la_crd)
* 다발지역폴리곤 (geom_json)
* 총건수 (totalCount)
* 검색건수 (numOfRows)
* 페이지 번호 (pageNo)

## 파일에 저장할 데이터 값들

* 조회한 연도 (searchYearCd)
* 지점명 (spot_nm) 
* 발생건수 (occrrnc_cnt) 
* 사상자수 (caslt_cnt) 
* 사망자수 (dth_dnv_cnt)
* 중상자수 (se_dnv_cnt) 
* 경상자수 (sl_dnv_cnt) 
* 부상신고자수 (wnd_dnv_cnt)

## 참고
[디코딩 관련](https://dreambyul.tistory.com/501)

[디코딩 관련2](https://rocksea.tistory.com/332)

[바이트 자료형?](https://dojang.io/mod/page/view.php?id=2462)

[바이트 문자열](https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal)

[지도 모듈](https://k-glory.tistory.com/24)

[DataFrame](https://3months.tistory.com/292)