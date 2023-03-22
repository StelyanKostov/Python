from tkinter import *
from tkinter.ttk import *
import requests
from bs4 import BeautifulSoup as bs


def btc_price():
    URL = 'https://coinmarketcap.com/currencies/bitcoin/'
    req = requests.get(URL)
    soup = bs(req.content, 'html.parser')
    price = soup.find('div', {'class': 'priceValue'})
    data = price.select_one('span')

    return data.text


root = Tk()
root.title('Bitcoin price')


def app():

    try:

        price = btc_price()

    except:

        app()

    w = 70
    h = 20
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 1) - (w / 1)
    y = (hs / 75) - (h / 2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.overrideredirect(True)
    root.lift()
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.wm_attributes("-transparentcolor", 'black')
    label.config(text=price)
    label.pack(padx=1, pady=1)
    label.after(100000, app)


label = Label(root, font=('', 10), background='black', foreground='white')
app()
mainloop()
