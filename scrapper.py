import requests
from bs4 import BeautifulSoup



# 1.get_page
# 2.get_pages number
# 3.get_info

def get_last_page(url):
    result = requests.get(url)
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
    job_id = html['data-jobid']
    return{
            'title' : title,
            'company':company,
            'location':location,
            "apply_link": f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page,url):
    jobs = []

    # range can not accept string type so need to convert string -> int type
    for page in range(last_page):
        print(f"Scrapping SO: Page: {page}")
        result = requests.get(f"{url}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}"
    last_page = get_last_page(url)
    jobs = extract_jobs(last_page,url)
    return jobs
