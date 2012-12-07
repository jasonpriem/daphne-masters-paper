import couchdb
import requests

couch_server = couchdb.Server(url="http://127.0.0.1:5984")
db = couch_server["daphne"]
print db

for row in db.view("main/by-type-and-id"):
    print row["_id"]