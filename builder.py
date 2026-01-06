import os 
import json 
import shutil 
from itertools import count 
# from bs4 import BeautifulSoup

# shutil.rmtree("output")

def read(name, mode="r"):
    with open(name, mode) as fd:
        return fd.read()

BODY_TEMPLATE = read("body.txt")
FOOTER_TEMPLATE = read("footer.txt")
HEADER_TEMPLATE = read("header.txt")

pages_list = json.loads(
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

os.makedirs("output", exist_ok=True)

# shutil.copytree("css", "output/css")
# shutil.copytree("js", "output/js")
# shutil.copytree("images", "output/images")

# shutil.rmtree("css")
# shutil.rmtree("css")
# shutil.rmtree("images")
# shutil.rmtree("output/images")
# shutil.rmtree("output/css")

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
            **page
        )

        # new_template = BeautifulSoup(
        #     new_template, 'html.parser'
        # ).prettify()

        with open(f"output/{page['name']}", "w+") as fd:
            fd.write(new_template)
 

print("page builded")
build()