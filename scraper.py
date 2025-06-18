import requests
import pandas as pd

def scrape_jobs_from_remoteok():
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
    except Exception as e:
        print("Error fetching jobs:", e)
        return pd.DataFrame()

    jobs = []
    for job in data[1:]:  # first item is metadata
        if job.get("position") and job.get("company"):
            jobs.append({
                "Job Title": job["position"],
                "Company": job["company"],
                "Location": job.get("location", "Remote"),
                "Tags": ", ".join(job.get("tags", [])),
                "Link": "https://remoteok.com" + job["url"]
            })

    return pd.DataFrame(jobs)
