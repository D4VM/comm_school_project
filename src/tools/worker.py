from redis import Redis
from rq import Queue
from tools.scrape import scrape_product
import time


q = Queue(connection=Redis())

job = q.enqueue(scrape_product, 'https://www.myauto.ge/ka/pr/98153702')

while not job.is_finished:
    time.sleep(1)

job_result = job.return_value()
print(job_result)
