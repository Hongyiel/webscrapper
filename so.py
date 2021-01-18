import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"


# 1.get_page
# 2.get_pages number
# 3.get_info

def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    # find will bring just one
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page) # string -> int

def extract_job(html):
    # div changed to h2
    title=html.find(
    "h2",{"class":"mb4"
    }).find("a")["title"]

    # if there are two items on span then each value can get in same time
    company, location=html.find(
    "h3",{"class" : "mb4"
    }).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    # print(company.get_text(strip=True) ,location.get_text(strip=True))
    return{'title' : title, 'company':company, 'location':location}

def extract_jobs(last_page):
    jobs = []
    # range can not accept string type so need to convert string -> int type
    for page in range(last_page):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return []
