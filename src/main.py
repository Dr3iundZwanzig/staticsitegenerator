import os
import shutil
from textnode import TextNode, TextType
from copy_directory import copy_directory
from generate_page import generate_pages_recursive
import sys

def main():
    basepath = sys.argv[1:]
    if not basepath:
        basepath = "/"

    static = "./static"
    public = "./docs"
    content = "./content"
    template_path = "./template.html"

        
    if os.path.exists(public):
        shutil.rmtree(public)
    copy_directory(static, public)

    generate_pages_recursive(content, template_path, public, basepath)


if __name__ == "__main__":
    main()