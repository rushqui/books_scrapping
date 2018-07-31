import urllib2
import json
from bs4 import BeautifulSoup 

def scrapping_books(phrase):
    modifed_phrase = phrase.replace(" ","+")
    quote_page = "https://busqueda.gandhi.com.mx/busca?q="+modifed_phrase
    page = urllib2.urlopen(quote_page)

    books = {}
    soup = BeautifulSoup(page.read(),'html.parser')
    books_search = soup.find('ul',class_="products-grid")

    for booksItems in books_search.find_all('li',class_="item"):
    	find_image = booksItems.a
    	book_image = find_image.img['src']
    	book_title = booksItems.h2.text.strip()
    	find_price = booksItems.find('p',class_="special-price") 
    	find_price2 = find_price.find('span',class_="price") 
    	find_format = booksItems.find('h4').text.strip()

        if find_price2 != None:
        	book_price = find_price2.text
        else:
        	book_price = ("No disponible ahora") 

        books["cover"] = book_image
        books["tile"] = book_title
        books["price"] = book_price

        if find_format:
        	books["format"] = find_format

        return json.dumps(books)


#book_titles = soup.find_all('h2',class_="product-name")
#book_prices = soup.find_all('span',class_="price")

#for productName in book_titles:
#	print(productName.text)

#for productPrice in book_prices:
#	print(productPrice.text)

#print name_box.text