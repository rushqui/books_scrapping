import urllib2
import json
from bs4 import BeautifulSoup 
from flask import Flask
app = Flask(__name__)

@app.route("/scrappingGandhi/<searchPhrase>")
def scrapping_booksGandhi(searchPhrase):
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
        book_writer =  booksItems.find('h3').text.strip()

        if find_price2 != None:
        	book_price = find_price2.text
        else:
        	book_price = ("No disponible ahora") 

        book["cover"] = book_image
        book["tile"] = book_title
        book["writer"] = book_writer
        book["price"] = book_price
        book["format"] = find_format


        books.append(book)
        

    return json.dumps(books)



@app.route("/scrappingPorrua/<searchPhrase>")
def scrapping_booksPorrua(searchPhrase):
    modifed_phrase = searchPhrase.replace(" ","%20")
    quote_page = "https://www.porrua.mx/busqueda/todos/"+modifed_phrase
    page = urllib2.urlopen(quote_page)

    books = []
    soup = BeautifulSoup(page.read(),'html.parser')
    books_search = soup.find(id="librosContainer")
    
    for booksItems in books_search.find_all('div',class_="col-md-3 col-sm-4"):
        book = {}
        find_image = booksItems.a
        book_image = find_image.img['src']
        book_title = booksItems.h5.contents[0]
        book_writer = booksItems.h5.font.text
        book_price = booksItems.h5.strong.text.strip()
        find_format = booksItems.find(class_="imgs_ebook")


        if find_format != None:
            find_format = ("ebook")
        else:
            find_format = ("fisico") 

        book["cover"] = book_image
        book["title"] = book_title
        book["writer"] = book_writer
        book["price"] = book_price
        book["format"] = find_format


        
        books.append(book)

    return json.dumps(books)  



@app.route("/scrappingSotano/<searchPhrase>")
def scrapping_booksSotano(searchPhrase):
    modifed_phrase = searchPhrase.replace(" ","+")
    quote_page = "https://www.elsotano.com/busqueda.php?q="+modifed_phrase
    page=urllib2.urlopen(quote_page)

    books = []
    soup=BeautifulSoup(page,'html.parser')
    books_search = soup.find('div',class_="contenedorLibros")

    for booksItems in books_search.find_all('figure',class_="effect-zoe"):
        book = {}

        find_image = booksItems.a
        book_image = find_image.img['src']
        book_title = booksItems.find('p',class_="susTit").text
        book_writer = booksItems.find('p',class_="subTitulo")
        book_price = booksItems.find('span',class_="subTit1").text
        book_format = booksItems.find('img',class_="etiquetaEsEbook")

        if book_writer != None:
            book_writer = book_writer.text
        else:
            book_writer = ("no disponible")
       
        if book_format != None:
            book_format = ("ebook")
        else:
            book_format = ("fisico")    


        book["cover"] = book_image
        book["title"] = book_title
        book["writer"] = book_writer
        book["price"] = book_price
        book["format"] = book_format

        books.append(book)

    return json.dumps(books)




    


    

