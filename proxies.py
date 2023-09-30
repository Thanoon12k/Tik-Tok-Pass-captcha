import threading
import requests
import queue

q=queue.Queue()
with open("proxies.txt",'r') as f:
    proxies=f.read().split("\n")
    for p in proxies:
        q.put(p)

def test_proxies():
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("http://ipinfo.io/json", proxies={"http": proxy, "https": proxy})
            
            if res.status_code==200:
               print(f"[ {threading.current_thread().name}] ", "proxy ip : ", proxy, '\t\t  status : ', res.status_code, "resp_ip-" ,res.json()['ip'])
               ##you can optional save these working proxies to new file
                    # with open('valid_proxies.txt', 'a') as f:  # 'a' mode will append to the file
                    # f.write(proxy + '\n')
                    # f.close()

            else:
                print(f"[ {threading.current_thread().name}] ", "proxy ip : ", proxy, '\t\t  status : ', res.status_code, "resp_ip-" ,"       ***  ")
            
        except:
           
             print(f"Error in proxy server , [{proxy}] ")


for _ in range(10):
    threading.Thread(target=test_proxies).start()