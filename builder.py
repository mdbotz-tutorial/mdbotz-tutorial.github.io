import os 
import json 
import shutil 
from itertools import count 


# shutil.rmtree("output")

BODY_TEMPLATE = """
      <div class="tutorials">
         <img class="tutorial-img" src="{0}" alt="tutorial image's">
         <p class="count">{1}</p>
         <p class="description">{2}</p>
      </div>
"""


FOOTER_TEMPLATE = """
       <footer class="footer">
          <a class="support" id="group" style="text-decoration: none;" href="https://telegram.me/MdBotzSupport">
               support group
          </a>
          <a class="support" id="channel" style="text-decoration: none;" href="https://t.me/venombotupdates">
               support channel
          </a>
        </footer>
"""

HEADER_TEMPLATE = """
        <div class="top">
           <img class="logo" src="./images/logo.png" alt="logo image">
           <h3 class="company-1" id="company">MD</h3>
           <h3 class="company-2" id="company">BOTZ</h3>
        </div>
""".strip()


def read_file(name, mode="r"):
    with open(name, mode) as fd:
        return fd.read()
    
pages_list = json.loads(
    read_file("pages.json")
)

template = read_file("template.txt")

tutorials = json.loads(
    read_file("tutorials.json")
)

def create_innerHTML(images):
    innerHTML = ""
    index = count(1).__next__
    for path, description in images.items():
        innerHTML += BODY_TEMPLATE.format(
            path, index(), description
        )
    return innerHTML

# os.makedirs("output", exist_ok=True)

# shutil.copytree("css", "output/css")
# shutil.copytree("js", "output/js")
# shutil.copytree("images", "output/images")

def build():

    for page in pages_list:
        
        body = read_file(f"template/{page['name']}")
        
        new_template = template.format(
            body=body.format(
               header=HEADER_TEMPLATE,
               footer=FOOTER_TEMPLATE,
               tutorials=create_innerHTML(
                   tutorials[page["name"]]
               )
            ),
            **page
        )

        with open(f"output/{page['name']}", "w+") as fd:
            fd.write(new_template)
 


build()