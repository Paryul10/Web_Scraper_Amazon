from bs4 import BeautifulSoup
import requests
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

lis = []
lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1")
lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_2?_encoding=UTF8&pg=2")
lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_3?_encoding=UTF8&pg=3")
lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_4?_encoding=UTF8&pg=4")
lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_5?_encoding=UTF8&pg=5")
#lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/#1")
##lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/#2")
#lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/#3")
#lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/#4")
##lis.append("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/#5")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#1")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#2")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#3")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#4")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#5")
base_url="https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/#"


#for i in range(1,6):
    #lk= base_url+str(i)
    #print lk
    #be=requests.get(lk)
    #print be



#print soup.find_all('a')

#for i in range(len(books)):
    #print books[i]
    #print "###################################################################################"
#books=soup.find_all(class_="zg_itemWrapper")
#print books
#print len(books)#20 books of page 1 captured in a list "BOOKS"
#book1=books[0]
#print book1.prettify()
count = [0]
#books=[]
alpha = []

lists = ["Name","URL","Author","Price","Number of Ratings","Average Rating"]
alpha.append(lists)
#pages = [str(i) for i in range(1,6)]


for j in range(len(lis)):
    #print lis[j]
    #lk= base_url+str(i)
    #print lk
    #be=requests.get(lk)
    #print be
    page = requests.get(lis[j])
    #print  page
    #print page.content
    soup = BeautifulSoup(page.content,'html.parser')
    books = soup.find_all(class_="zg_itemWrapper")#book_list is a list which contains all the elements in id="zg_center"
    for i in range(len(books)):
        count[0] += 1
        temp = []
        print "count=",count[0]
        try:
            name = books[i].find(class_ = "p13n-sc-truncate p13n-sc-line-clamp-1").get_text().strip()
            #temp.append(name)
            print name
        except:
            name = "Not available"
            #temp.append(name)
            print "Not available"
        try:
            link = books[i].find(class_ = "a-link-normal").get("href")
            #link[0]
            link_new = "https://www.amazon.com"+link
            print link_new
        except:
            link = "Not available"
            print link
        try:
            aut_name = books[i].find(class_ = "a-row a-size-small").get_text()
            print aut_name
        except:
            aut_name = "Not available"
            print "Not available"
        try:
            rating = books[i].find(class_ = "a-icon-alt").get_text()
            #rating=r["title"]
            if (rating == "Prime"):
                rating = "Not available"
            print rating
        except:
            rating = "Not available"
            print "Not available"
        try:
            reviews = books[i].find(class_ = "a-size-small a-link-normal").get_text()
            print reviews
        except:
            reviews = "Not available"
            print "Not available"
        try:    
            price = books[i].find(class_ = "p13n-sc-price").get_text().strip()
            print price
        except:
            price = "Not available"
            print "Not available"

        temp.append(name)
        temp.append(link_new)
        temp.append(aut_name)
        temp.append(price)
        temp.append(reviews)
        temp.append(rating)

        alpha.append(temp)


    
with open ('out_book.csv','wb') as file:
   writer = csv.writer(file)
   for row in alpha:
      writer.writerow(row)


#x= find_all()
#x.a['href']
