import couchdb
'''
Reads a list of IDs and loads them all as docs into a couchdb database.
'''

ids_file_loc = "../daphne-masters-paper-data/unique-ids.txt"
f = open(ids_file_loc, 'r')


couch_server = couchdb.Server(url="http://127.0.0.1:5984")
db = couch_server["daphne"]

for line in f:
    if not line:
        continue
    else:
        id = line.strip()
        db[id] = {"type":"library_item"}