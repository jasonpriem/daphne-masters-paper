import couchdb
design_doc = {
    "_id": "_design/main",
    "language": "javascript",
    "views": {
        "by_type_and_id": {
            "map": '''function(doc) {
                if (doc.type == "library_item") {
                    var resourceType = doc.resource_type ? doc.resource_type : "NA"
                    emit([resourceType, doc._id], doc)
                }
            }'''
        },
        "has_api_result": {
            "map": '''function(doc) {
                if (doc.type == "library_item") {
                    var hasApiResult = doc.api_result ? 1 : 0
                    emit([hasApiResult, doc._id], doc)
                }
            }'''
        },
        "count_num_done_with_api": {
            "map": '''function(doc) {
                if (doc.type == "library_item") {
                    var hasApiResult = doc.api_result ? 1 : 0
                    emit([hasApiResult, doc._id], doc)
                }
            }'''
        }
    },
    "lists":{
        "csv": '''function(head, req) {
            var row;
            start({
                "headers": {
                    "Content-Type": "text/html"
                }
            });
            while(row = getRow()) {
                var formats = row.key[0]
                if (typeof formats == "object") {
                    formats = formats.join("|")
                }
                send(row.key[1] + "," + formats + "\\n");
            }
        }'''
    }
}

couch_url = "http://127.0.0.1:5984"
db_name = "daphne"
design_doc_name = "_design/main"

'''
define functions
'''

# from http://blog.marcus-brinkmann.de/2011/09/17/a-better-iterator-for-python-couchdb/
def couchdb_pager(db, view_name='_all_docs',
                  startkey=None, startkey_docid=None,
                  endkey=None, endkey_docid=None, bulk=5000):
    # Request one extra row to resume the listing there later.
    options = {'limit': bulk + 1}
    if startkey:
        options['startkey'] = startkey
        if startkey_docid:
            options['startkey_docid'] = startkey_docid
    if endkey:
        options['endkey'] = endkey
        if endkey_docid:
            options['endkey_docid'] = endkey_docid
    done = False
    while not done:
        view = db.view(view_name, **options)
        rows = []
        # If we got a short result (< limit + 1), we know we are done.
        if len(view) <= bulk:
            done = True
            rows = view.rows
        else:
            # Otherwise, continue at the new start position.
            rows = view.rows[:-1]
            last = view.rows[-1]
            options['startkey'] = last.key
            options['startkey_docid'] = last.id

        for row in rows:
            yield row





'''
setup and return the couch connection
'''

couch_server = couchdb.Server(url=couch_url)
db = couch_server[db_name]

# load the latest version of the design doc.
del(db[design_doc_name]) # i think this will fail the first time this is run.
db[design_doc_name] = design_doc