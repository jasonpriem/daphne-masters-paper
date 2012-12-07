import couchdb
import requests
url_template = "http://search.lib.unc.edu/search?R=[id]&output-format=export&export-option=xml"

couch_server = couchdb.Server(url="http://127.0.0.1:5984")
db = couch_server["daphne"]

view_res = db.view("main/has-api-result")

print view_res[[0, False]:[0, "zzzzzz"]]

for row in view_res[[0, False]:[0, "zzzzzz"]]:
    query = url_template.replace("[id]", row["id"])
    doc = row.value
    res = requests.get(query)
    doc["api_result"] = res.text

#    print row["id"]
    db.save(doc)