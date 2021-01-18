import csv

def save_to_file(jobs):
    # r readable mode
    # w writable mode
    # etc...
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        # print(type(job.values())) # type: dict_values are coming.
        writer.writerow(list(job.values())) # type: dict_values are coming.

    return
