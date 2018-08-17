from bs4 import BeautifulSoup
import requests
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
lis = []
lis.append("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_5?ie=UTF8&pg=1")
lis.append("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_5?ie=UTF8&pg=2")
lis.append("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_5?ie=UTF8&pg=3")
lis.append("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_5?ie=UTF8&pg=4")
lis.append("https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_5?ie=UTF8&pg=5")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#1")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#2")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#3")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#4")
#lis.append("https://www.amazon.in/gp/bestsellers/books/#5")
for i in range(len(lis)):
    print lis[i]
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



for j in range(len(lis)):
    #print lis[j]
    page = requests.get(lis[j])
    #print page
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
            link_new = "https://www.amazon.in"+link
            print link_new
        except:
            link = "Not available"
            print link
        try:
            aut_name = books[i].findAll("div",{"class":"a-row a-size-small"})
            author = aut_name[0].get_text()
            print author
        except:
            aut_name = "Not available"
            print "Not available"
        try:
            rating = books[i].find(class_ = "a-icon-alt").get_text()
            #rating=r["title"]
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
            price = "Rs "+books[i].find(class_ = "a-size-base a-color-price").get_text().strip()
            print price
        except:
            price = "Not available"
            print "Not available"

        temp.append(name)
        temp.append(link_new)
        temp.append(author)
        temp.append(price)
        temp.append(reviews)
        temp.append(rating)

        alpha.append(temp)


    
with open ('in_book.csv','wb') as file:
   writer = csv.writer(file)
   for row in alpha:
      writer.writerow(row)


#x= find_all()
#x.a['href']
