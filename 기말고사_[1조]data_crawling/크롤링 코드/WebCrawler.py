from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# 사람인 평균 연봉 정보 크롤링
def saramin_salary(result):
    for page in range(1, 501): # 1페이지당 20개의 항목들이 있다.
        # 페이지를 제외한 사람인 사이트 url
        saramin_url = 'https://www.saramin.co.kr/zf_user/salaries/total-salary/list?page=%d&order=rank&industry_cd=&company_cd=&rec_status=&search_company_nm_org=&search_company_nm=&min_salary=&max_salary=&request_modify_company_nm=' %page
        html = urllib.request.urlopen(saramin_url)
        saramin_soup = BeautifulSoup(html, 'html.parser')
    
        tag_ul = saramin_soup.find("ul", {"class":"list_salary"}) # list_salary 클래스 ul
        tag_list = list(tag_ul.find_all('li')) # ul 내의 li 태그들을 다 찾아 리스트화
        
        for in_li in tag_list: # li 태그 내의 정보
            company_name = in_li.find("a", {"class":"link_tit"}).text # 기업 이름
            company_dd = in_li.find_all('dd') # 기업 정보
            company_type = company_dd[0].text # 기업 형태
            company_work = company_dd[1].text # 산업(업종)
            company_salary = in_li.find('span', {"class":"txt_g txt_avg"}).text # 평균 연봉 (단위: 만)
            result.append([company_name, company_type, company_work, company_salary]) # result 에 추가
            
    return result

def main():
    result = []
    
    print("Saramin salary crawling >>>>>")
    saramin_salary(result)
    saramin_tbl = pd.DataFrame(result, columns = ['기업 이름', '기업 형태', '산업(업종)', '평균 연봉'])
    #테이블을 csv 파일로 Export
    saramin_tbl.to_csv('./평균연봉_cp949.csv', encoding='cp949', mode='w', index = False)
    saramin_tbl.to_csv('./평균연봉_utf8.csv', encoding='utf8', mode='w', index = False)

    print("Finished")

if __name__ == '__main__':
    main()