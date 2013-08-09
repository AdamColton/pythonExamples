import multiprocessing
from time import sleep

def worker(jobs, responses, id):
  while True:
    x = jobs.get()
    print(id, ": ", x)
    responses.put(x*x)
    jobs.task_done()
    sleep(0.1) #with out this, the 

if __name__ == '__main__':    
  jobs = multiprocessing.JoinableQueue()
  responses = multiprocessing.JoinableQueue()
  for id in range(4):
    p = multiprocessing.Process(target=worker, args=(jobs, responses, id))
    p.daemon = True
    p.start()
  for i in range(20):
    jobs.put(i)
  jobs.join()
  while not responses.empty():
    print(responses.get())