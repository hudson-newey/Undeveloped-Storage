import time
import requests
from difflib import SequenceMatcher
from bs4 import BeautifulSoup

minimumPercent = 10 # must be 10% lower than valued
objects = []
prices = []

def percentDiferance(seller, comparison): return ((comparison - seller)/seller) * 100
def countObjects(rawdata): return rawdata.count("AU $") - 12
def similar(a, b): return SequenceMatcher(None, a, b).ratio()

# tell the user that a deal has been found
def dealFound(item, diferance, object):
    print("\nItem found:")
    print("\t-" + object)
    print("\t-" + diferance + "% Deal!")

def compareObjects(searchTerm, postalcode, similarity):
    page = requests.get('https://www.ebay.com.au/sch/i.html?_nkw='+searchTerm+'&_in_kw=1&_ex_kw=&_sacat=0&LH_Sold=1&_udlo=&_udhi=&LH_Auction=1&LH_BIN=1&_samilow=&_samihi=&LH_FS=1&LH_LPickup=2&_fsradio2=%26LH_PrefLoc%3D99&_sadis=25&_stpos='+postalcode+'&_fspt=1&_sargn=-1%26saslc%3D1&_salic=15&_sop=12&_dmd=1&_ipg=200&LH_Complete=1&_fosrp=1')
    soup = BeautifulSoup(page.text, 'html.parser')
    comparisonObj = soup.find(class_='vip').text

    for i in range(len(objects)):
        if (similar(comparisonObj, objects[i]) > (similarity / 100)):
            # if 2 identical items are found
            # get price of second object
            price = soup.find(class_='lvprice prc').text
            price = price.replace('\n', '').replace('AU $', '')

            diferance = percentDiferance(int(price), int(prices[i]))
            if (diferance >= minimumPercent):
                dealFound(i, diferance, objects[i]) # item, price, object



def sellerObjects(searchTerm, postalcode):
    page = requests.get('https://www.ebay.com.au/sch/i.html?_nkw='+searchTerm+'&_in_kw=1&_ex_kw=&_sacat=0&_udlo=&_udhi=&LH_Auction=1&LH_BIN=1&_ftrt=901&_ftrv=1&_sabdlo=&_sabdhi=&_samilow=&_samihi=&LH_FS=1&LH_LPickup=2&_fsradio2=%26LH_PrefLoc%3D99&_sadis=25&_stpos='+postalcode+'&_fspt=1&_sargn=-1%26saslc%3D1&_salic=15&_sop=12&_dmd=1&_ipg=200&_fosrp=1')
    soup = BeautifulSoup(page.text, 'html.parser')
    object = soup.find(class_='vip').text

    price = soup.find(class_='lvprice prc').text
    price = price.replace('\n', '').replace('AU $', '')
    objects.append(object)
    prices.append(price)


def main():
    print("Minimum Deal (%)")
    minimumPercent = int(input(":"))
    print("Listing Similarity, (%)")
    similarity = int(input(":"))
    print("Postal Code,")
    postalCode = str(input(":"))


    # search funciton
    while(True):
        print("\nEnter Search Term,")
        searchterm = str(input(":"))
        sellerObjects(searchterm, postalCode)
        compareObjects(searchterm, postalCode, similarity)
        time.sleep(1.2) # wait so you don't get blocked
    pass


# call main function
main()
