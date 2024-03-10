from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup
import json

phnRev=[]
customer_name=[]
rating=[]
review=[]
b_url='https://www.flipkart.com/samsung-galaxy-s24-ultra-5g-titanium-violet-256-gb/product-reviews/itmd4f51262e3e6b?pid=MOBGX2F38JBJGZSE&lid=LSTMOBGX2F38JBJGZSELMVCH5&marketplace=FLIPKART&page='
for i in range(1,20):
    url = b_url + str(i)
    request_site = Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Referer": "https://www.flipkart.com/"})
    html = request.urlopen(request_site)
    soup = BeautifulSoup(html, 'html.parser')

    name=soup.find_all('p',{'class':'_2sc7ZR _2V5EHH'})
    rat=soup.find_all('div',{'class':'_3LWZlK _1BLPMq'})
    rev = soup.find_all('div', {'class': 't-ZTKy'})

    for i in name:
        name=i.text
        customer_name.append(name)
    for i in rat:
        rat=i.text
        rating.append(rat)
    for i in rev:
        rev=i.text
        review.append(rev)



# print(rating)
    for names,ratng,rew in  zip(customer_name, rating, review):
        phone = {
            'Buyer_name':names,
            'Rating':ratng,
            'Review':rew}
        phnRev.append(phone)
# print(rating)
# print(phnRev)
jsonfile = open("S24_review.json","w")
json.dump(phnRev,jsonfile)