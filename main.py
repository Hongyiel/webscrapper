from indeed import extract_indeed_pages,extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_page)

print(indeed_jobs)
# max_indeed_pages = extract_indeed_pages()
# print(max_indeed_pages)
# for n in range(max_pages):
#     print(f"start={n*50}")
