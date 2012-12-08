
# downloads the full set of of ID->format pairs from a couch list.
curl "http://127.0.0.1:5984/daphne/_design/main/_list/csv/by_type_and_id?descending=true") > formats.csv