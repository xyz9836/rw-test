import os
import requests

s=requests.session()





def w_config(user_path, token, js_id):
    with open(user_path, "w", encoding="utf8") as fp:
        fp.write(token + "," + js_id)


def r_config(user_path):
    with open(user_path, "r", encoding="utf8") as fp:
        try:
            token, js_id = fp.read().split(",")
            return token, js_id
        except:
            print("记录文件损坏，错误代码3程序退出")
            #sys.exit(3)


if __name__ == "__main__":

    a,b=r_config('baidu.txt')
    print ('a,b',a,b)
    r = s.get('https://www.baidu.com')
    print (r.reason,r.text)
    w_config('baidu.txt', r.reason, r.text)