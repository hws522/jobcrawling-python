from saramin import extract_saramin_jobs, extract_saramin_pages

last_saramin_page = extract_saramin_pages()

sramin_jobs = extract_saramin_jobs(last_saramin_page)

print(sramin_jobs) 