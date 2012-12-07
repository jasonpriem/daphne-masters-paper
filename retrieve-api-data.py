import couchdb
import requests
url_template = "http://search.lib.unc.edu/search?R=[id]&output-format=export&export-option=xml"

couch_server = couchdb.Server(url="http://127.0.0.1:5984")
db = couch_server["daphne"]

for row in db.view("main/by-type-and-id"):
    query = url_template.replace("[id]", row["id"])
    doc = row.value
    res = requests.get(query)
    doc["api_result"] = res.text

    db.save(doc)