import requests
from bs4 import BeautifulSoup



def extractSOPage(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
    lastPage = pages[-2].get_text(strip=True)
    return int(lastPage)

def extractJob(html):
    title = html.find("h2").find("a")["title"]
    company, location = html.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip(" \r").strip("\n")
    job_id = html['data-jobid']
    return {'title': title,'company': company,'location': location,
        "link": f"https://stackoverflow.com/jobs/{job_id}"}


def extractSOJobs(URL, lastPage):
    jobs = []
    for page in range(lastPage):
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})

        for result in results:
            job = extractJob(result)
            jobs.append(job)

    return jobs

def getJobs(keyword):
    URL = f"https://stackoverflow.com/jobs?q={keyword}"
    last_pages = extractSOPage(URL)
    jobs = extractSOJobs(URL, last_pages)
    return jobs
