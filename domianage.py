import whois

url = "https://www.g32423oogle.com/"

try :
    domian_info = whois.whois(url)
    print(domian_info)
except whois.parser.PywhoisError :
    print("fail")