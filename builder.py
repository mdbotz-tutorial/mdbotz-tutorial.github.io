import os 
import json 
from itertools import count 

os.makedirs("output", exist_ok=True)

def read(name, mode="r"):
    with open(name, mode) as fd:
        return fd.read()

BODY_TEMPLATE = read("body.txt")
FOOTER_TEMPLATE = read("footer.txt")
HEADER_TEMPLATE = read("header.txt")

LINK_TEMPLATE = """\r\t<link rel="stylesheet" href="{path}">"""

pages_list: list[dict] = json.loads(
    read("pages.json")
)

template = read("template.txt")

tutorials = json.loads(
    read("tutorials.json")
)

def create_innerHTML(images):
    innerHTML = ""
    index = count(1).__next__
    for path, description in images.items():
        innerHTML += BODY_TEMPLATE.format(
            path, index(), description
        )
    return innerHTML

def get_stylesheets(paths):
     stylesheets = ""
     for path in paths:
         stylesheets += LINK_TEMPLATE.format(path=path)
     return stylesheets 

def build():

    for page in pages_list:
        
        body = read(f"template/{page['name']}")
        
        new_template = template.format(
            body=body.format(
               header=HEADER_TEMPLATE,
               footer=FOOTER_TEMPLATE,
               tutorials=create_innerHTML(
                   tutorials.get(page["name"], {})
               )
            ),
            stylesheet=get_stylesheets(
                page["stylesheets"]
            )[2:],
            **page
            
        )

        with open(f"output/{page['name']}", "w+") as fd:
            fd.write(new_template)
 

build()
print("page builded successfully")