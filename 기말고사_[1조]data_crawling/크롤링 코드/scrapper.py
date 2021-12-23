import requests
from bs4 import BeautifulSoup

#(4) 해당 url 이 가진 마지막 페이지 번호 반환
def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find_all("a", class_="s-pagination--item")
  last_page = pages[-2].get_text(strip=True) #pages[-1] = 마지막 값은 next이므로 스킵
  return int(last_page);

#(3) 한 페이지 당 내부 태그 순회
def extract_job(html):
  title = html.find("a", "s-link")["title"]
  #company_row 리스트 안에 어떤 요소가 몇 개 올지 알고 있을 때 -> unpacking 기능
  company, location = html.find("h3","mb4").find_all("span", recursive=False) # recursive : 더 깊에 안 들어가게 함, 즉 다 가져오지 않고 같은 레벨의 요청 값만 가져옴. 예를 들어 span 안에 또 span이 있으면 그 span은 가져오지 않음
  company = company.get_text(strip=True)
  location = location.get_text(strip=True)

  job_id = html['data-jobid']

  return {'title': title, 'company': company, 'location': location, "apply_link": f"https://stackoverflow.com/jobs/{job_id}"}

#(2) 페이지 각각을 돌면서 extract_job을 호출하여 각 페이지의 정보 크롤링
def extract_jobs(last_page, url):
  jobs = []
  # 첫 페이지부터 끝 페이지까지 순회
  for page in range(last_page):
   result = requests.get(f"{url}&pg={page+1}")
   soup = BeautifulSoup(result.text, "html.parser")
   results = soup.find_all("div", class_="-job")
  #  print(f"Scraping StackOverflow: Page {page+1} //", len(results)) 
   for result in results:
     job = extract_job(result)     
     jobs.append(job)
  return jobs           

#(1) stackOverflow 에서 가지고 온다.
def get_jobs(word):
  url = f"https://stackoverflow.com/jobs?q={word}"
  last_page = get_last_page(url) # 해당 url이 가진 마지막 페이지 값 구하는 함수
  jobs = extract_jobs(last_page, url)
  return jobs