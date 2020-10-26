
from suds.client import Client

# wsdl_url = "http://60.12.95.62:5001/?wsdl"
# wsdl_url = "http://127.0.0.1:5001/?wsdl"
# wsdl_url = "http://localhost:8777/oz/hello?wsdl"
wsdl_url = "http://127.0.0.1:9757/?wsdl"

import  json
def say_hello_test(url, name):
    try:
        client = Client(url)

        rs =client.service.say('wkx')
        # rs = client.service.hello_world2()
        print(rs)
    except Exception as e:
        print("23")



if __name__ == '__main__':
    say_hello_test(wsdl_url, 'test')