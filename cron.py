import requests
import time
n = 1
while n > 0: 
    req = requests.get('https://psncheckerbyhackedyouagain.herokuapp.com/health')
    print(req)
    time.sleep(174)