import firebase_admin
from firebase_admin import credentials, firestore
from bs4 import BeautifulSoup
import requests

cred = credentials.Certificate('/Users/mahaashreeanburaj/Downloads/booksite-testrun-firebase-adminsdk-x13kd-6fe80f1c10.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

all_books = soup.find_all('article',class_='product_pod')

for book in all_books:
    title = book.h3.a['title']
    price = book.find('p',class_='price_color').text.strip()

    book_data = {
        'title' : title,
        'price': price
    }
    db.collection('books').add(book_data)
    
print("success baby")

