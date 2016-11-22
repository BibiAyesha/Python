# Python

There are two files in this project. Please fidn the details of the two fils below.
-----------------------------------------------------------------
1. webCrawler.py - Problem Statement is as below. 
------------------------------------------------------------------
## Web Crawler for Shopping.com

Implement a robust text scraper that will connect to a page on www.shopping.com, and return a result for a given keyword. Two queries can be performed using this program. The first query is getting the total number of results for a given keyword. The second query is to find all results for a given keywords on a specified page. Handle all the exceptions gracefully any feel free to use your favorite library.


### Following are the URLs
    `http://www.shopping.com/products?KW=<keword>`
    `http://www.shopping.com/products~PG-<number>?KW=<keyword>"`

### Queries: 
    Query 1: (requires a single argument)
    `your_program <keyword>`
    
    Query 2: (requires two arguments)
    `your_program <keyword> <page number>`

 
### The focus of this problem is on correctness and design.

-------------------------------------------------------------------
2. UnHhash.py --  Problem statement is as below.
--------------------------------------------------------------------
Write code to find a string of characters that contains only letters from

`acdegilmnoprstuw`

such that the hash(the_string) is

`930846109532517`

if hash is defined by the following pseudo-code:

```
Int64 hash (String s) {
    Int64 h = 7
    String letters = "acdegilmnoprstuw"
    for(Int32 i = 0; i < s.length; i++) {
        h = (h * 37 + letters.indexOf(s[i]))
    }
    return h
}
```

For example, if we were trying to find the 7 letter string where `hash(the_string)` was `680131659347`, the answer would be "leepadg".
