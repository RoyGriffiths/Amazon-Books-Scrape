from bs4 import BeautifulSoup
from urllib.request import urlopen

# Simple Python program that gets the top 50 best seller books from Amazon:
def getTop50Books():

    # Get URL, open it then get the soup with BeautifulSoup:
    url = "https://www.amazon.co.uk/Best-Sellers-Books/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1"
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')

    # Get the list of all the books, then initialise a count:
    books = soup.find_all("li", class_="zg-item-immersion")
    count = 0

    # Iterate through each book, getting data such as the title and author:
    for x in books:
        title = x.find("div", class_="p13n-sc-truncate p13n-sc-line-clamp-1").text

        try:
            author = x.find("a", class_="a-size-small a-link-child").text
        except:
            author = x.find("span", class_="a-size-small a-color-base").text

        try:
            price = x.find("span", class_="p13n-sc-price").text
        except:
            price = "Error"

        try:
            rating = str(x.find("div", class_="a-icon-row a-spacing-none").find("a", class_="a-link-normal").get('title'))[0:3] + " / " + "5"
        except:
            rating = "NA"

        type = x.find("span", class_="a-size-small a-color-secondary").text
        count += 1
        print(str(count) + "." + title + "    By: " + author + ", " + type + ", " + price + "\n" + "            " + "Rating: " + rating)

getTop50Books()