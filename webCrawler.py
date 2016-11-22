#webCrawler.py

"""
    In this python script I have used
    1. urllib to connect to the server and get the html page
    2. BeautifulSoap to get and to walk through the DOM structure
    the HTML page
    3. sys package to get the sommand line arguments

"""
import sys
import urllib.request, bs4


"""
In the function getRespKeyWord
   1. fetching the keyword, and creating the url
   2. sending it to the server and getting html page of the URL.
   3. creating beatifulsoap class from the html that we got from the above step.
   4. fetching the corresponding div to get the results
   (total number of results are desplayed in the div which has class numTotalResults, so fetching the class from beautiful structure.
    the result is displayed in the specified format
    example - Results 161 - 200 of 1128
    splitting the above results and getting the last num which represents total number of results for the given query.)
"""
def getRespKeyword(keyWord):
    url = "http://www.shopping.com/products"+"?KW="+keyWord
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

""""
In the Function getRespPgNum 
  1. fetch the pgNum and keyword to form the url
  2. check if pgNum is int, otherwise return -1
  3. If the pgNum is 0, then it doesn't exist, so return -1
  4. In the DOM structure find the form which holds all the results on the page. 
  5. select all the divs under the form then count the div using beautifulsoap.
  6. The divs under the form are the displayed items.
  7. If there are no divs then there are no items, so return -1.
"""

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
     

