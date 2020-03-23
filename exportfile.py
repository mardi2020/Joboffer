import csv

def saveToFile(jobs):
    f = open("jobs.csv", mode="w")
    writter = csv.writer(f)
    writter.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writter.writerow(list(job.values()))
    return 
