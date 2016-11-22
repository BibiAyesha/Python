import sys
import urllib.request, bs4

def getRespKeyword(keyWord):
    url = "http://www.shopping.com/products"+"?KW="+keyWord
    print(url)
    res = urllib.request.Request(url)
    response = urllib.request.urlopen(res)
    soup = bs4.BeautifulSoup(response.read(),"html.parser")
    elems= soup.select('.numTotalResults')
    if len(elems) == 0 :
        num = -1 
        print("No Results Found"+keyWord)
    else:
        num = int(elems[0].text.split(" ")[5].split('\n')[0])
        print("total number of products for the keyword ",keyWord," is : ",num)
    return num




def getRespPgNum(keyWord, pgNum):
    if isinstance(pgNum, int):
        if pgNum == 0:
            print("Invalid Page num")
            return -1
        url = "http://www.shopping.com/products"+"~PG-"+str(pgNum)+"?KW="+keyWord
        res = urllib.request.Request(url)
        response = urllib.request.urlopen(res)
        soup = bs4.BeautifulSoup(response.read(),"html.parser")
        pages= soup.select("form > div")
        num = len(pages)-2
        if num == -1:
            print("There are no ",keyWord," on specified page ",pgNum)
            return -1
        else:
            print("There are ",num," number of ",keyWord,"s available on page number ",pgNum)
            return num
    else:
        return -1
     

