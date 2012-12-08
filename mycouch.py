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
setup and return the couch connection
'''

couch_server = couchdb.Server(url=couch_url)
db = couch_server[db_name]

# load the latest version of the design doc.
del(db[design_doc_name]) # i think this will fail the first time this is run.
db[design_doc_name] = design_doc