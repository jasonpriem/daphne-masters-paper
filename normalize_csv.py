# nothing here yet, not sure how we'll want it normalized.
f = open("formats.csv", "r")
items = {}
all_formats = set()

# get a dict of items, and set of all possible formats.
for line in iter(f):
    line = line.replace("\n", "")
    cells = line.split(",")
    if cells[1] == '':
        cells[1] = "Not returned"

    formats_this_item_has = cells[1].split("|")
    all_formats = all_formats.union(formats_this_item_has)
    items[cells[0]] = formats_this_item_has

f.close()

all_formats = sorted(all_formats)
print all_formats

# make the normalized csv
formats_normalized = {}
for id, formats_this_item_has in items.iteritems():
    non_sparse_list_of_formats_for_this_item = []
    for possible_format in all_formats:
        if possible_format in formats_this_item_has:
            item_has_this_format = "1"
        else:
            item_has_this_format = "0"

        non_sparse_list_of_formats_for_this_item.append(item_has_this_format)

    formats_normalized[id] = non_sparse_list_of_formats_for_this_item


print "made normalized formats array; now to print it."
f = open("formats_normalized.csv", "w")
f.write("Item_ID," + ",".join(all_formats) + "\n") # header
for id, formats_this_item_has in formats_normalized.iteritems():
    f.write(id + "," + ",".join(formats_this_item_has) + "\n")

f.close()










