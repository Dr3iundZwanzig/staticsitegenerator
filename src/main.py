import os
import shutil
from textnode import TextNode, TextType
from copy_directory import copy_directory
from generate_page import generate_page

def main():

    static = "./static"
    public = "./public"
    from_path = "./content/index.md"
    template_path = "./template.html"
    dest_path = "./public/index.html"
        
    if os.path.exists(public):
        shutil.rmtree(public)
    copy_directory(static, public)

    generate_page(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()