from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
import csv # CSV : Comma Separated Values

db = {} # 검색어 저장 임시 데이터 베이스

app = Flask("SuperScrapper")

@app.route("/") # @ decorator : 밑에 위치한 함수 실행
def home():
  return render_template("home.html")

# @app.route("/<username>") # dynamic URL
# def hitMeUp(username):
#   return f"Hello, {username}! How are you doing?"  

@app.route("/report")
def report(): # 검색 결과를 HTML에 렌더링
  word = request.args.get('word')
  if word:
    word = word.lower()
    existingJobs = db.get(word)
    if existingJobs: # 임시 데이터베이스에 있는 결과 즉 이미 검색했었던 단어일 경우
      jobs = existingJobs
    else: # 임시 데이터베이스에 결과가 없다면, 즉 새롭게 검색하는 단어일 경우
      jobs = get_jobs(word) # 스택오버플로우에서 검색어로 관련 직업 크롤링
      db[word] = jobs # 결과를 임시 데이터베이스에 저장
  else: # URL 파라미터에 word 값이 없을 경우 홈으로 리다이렉트
    return redirect("/")
  return render_template(
    "report.html", 
    searchingBy=word, 
    resultNumber=len(jobs), 
    jobs=jobs
  )

@app.route("/export")
def export(): # 검색 결과를 CSV 파일로 저장
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = db.get(word) # 임시 데이터베이스에서 해당 검색어에 해당하는 결과값 jobs에 반환
    if not jobs:
      raise Exception()  
    save_to_file(jobs) # 파일 저장 함수 콜
    #파일의 이름을 변경
    return send_file("jobs.csv",
    attachment_filename=word+'.csv',
    as_attachment=True)
  except:
    return redirect("/")

def save_to_file(jobs): 
  file = open("jobs.csv", mode="w") # write
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "apply_link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return

app.run(host="0.0.0.0")