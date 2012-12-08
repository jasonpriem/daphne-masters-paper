from mycouch import db
import requests

r = requests.get("http://127.0.0.1:5984/daphne/_design/main/_list/csv/by_type_and_id?descending=true")
f = open("formats.csv", "w")
f.write(r.text)