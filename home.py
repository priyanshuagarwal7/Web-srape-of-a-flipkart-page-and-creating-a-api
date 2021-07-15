from flask import Flask , jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def laptops():
    html_text = requests.get('https://www.flipkart.com/search?q=hp%20laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off').text

    soup = BeautifulSoup(html_text , 'lxml')
    main_div = soup.find_all('div' , class_ = "col col-7-12")
    all_laptops = {}
    for divs in main_div:
        laptop_name = divs.find('div' , class_ = "_4rR01T").text

        result = {
            "Name":" ",
            "Processor":" ",
            "RAM":" ",
            "OS":" ",
            "HDD/SSD":" ",
            "Display":" ",
            "Other Features":" ",
            "Warranty":" "
        }
        result["Name"] = laptop_name
        features = divs.find_all('li' ,class_ = "rgWa7D")
        length = len(features)
        n = range(length)   
        keys = list(result)
        for x in n:
            result[keys[x+1]] = features[x].text
        all_laptops[laptop_name] = result
    return jsonify(all_laptops)
            

if __name__=="__main__":
    app.run(debug=True)