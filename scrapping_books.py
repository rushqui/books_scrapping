import urllib2
import json
from bs4 import BeautifulSoup 
from flask import Flask
app = Flask(__name__)

@app.route("/scrappingGandhi/<searchPhrase>")
def scrapping_books(searchPhrase):
    modifed_phrase = searchPhrase.replace(" ","+")
    quote_page = "https://busqueda.gandhi.com.mx/busca?q="+modifed_phrase
    page = urllib2.urlopen(quote_page)

    books = []
    soup = BeautifulSoup(page.read(),'html.parser')
    books_search = soup.find('ul',class_="products-grid")

    for booksItems in books_search.find_all('li',class_="item"):
        book = {}
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

        book["cover"] = book_image
        book["tile"] = book_title
        book["price"] = book_price

        if find_format:
        	book["format"] = find_format


        books.append(book)
        

    return json.dumps(books)

