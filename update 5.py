import requests
import time
import threading

url = "https://api.opensea.io/asset/0xd93206BD0062cC054E397eCCCdB8436c3fa5700e/"
update_flag = "/?force_update=true"

def process_range(start, end):
  for i in range(start, end):
    req_url = url + str(i) + update_flag
    r = requests.get(req_url)
    print(i, r.status_code)
    time.sleep(0.00025)

while True:
  t1 = threading.Thread(target=process_range, args=(0, 22500))
  t2 = threading.Thread(target=process_range, args=(22501, 45231))


  t1.start()
  t2.start()


  t1.join()
  t2.join()

