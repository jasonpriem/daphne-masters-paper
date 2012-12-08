from mycouch import db
from lxml import etree

"""
test the parser
note you have supply your own "sample_resp.xml"; it's kept out of the repo
because the IRB says it's Super Secret Data.

Commented out now for performance reasons; this runs like 100k+ times in production...
"""

"""
sample = open("sample_resp.xml", "r").read()
root = etree.XML(sample)
formats = root.xpath(".//institutions/UNC/formats/item/text()")
assert formats == ["Book"]

sample = open("sample_resp_two_formats.xml", "r").read()
root = etree.XML(sample)
formats = root.xpath(".//institutions/UNC/formats/item/text()")
assert formats == ["Video", "Book"]
"""


view_res = db.view("main/by_type_and_id")
for row in view_res[["NA", 0]:["NA", "zzzzzz"]]:
    doc = row.value
    root = etree.XML(doc["api_result"])
    formats = root.xpath(".//institutions/UNC/formats/item/text()")
    doc["resource_type"] = formats

    db.save(doc)