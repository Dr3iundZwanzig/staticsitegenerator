import os
import shutil
from textnode import TextNode, TextType
from copy_directory import copy_directory
from generate_page import generate_pages_recursive

def main():

    static = "./static"
    public = "./public"
    content = "./content"
    template_path = "./template.html"

        
    if os.path.exists(public):
        shutil.rmtree(public)
    copy_directory(static, public)

    generate_pages_recursive(content, template_path, public)


if __name__ == "__main__":
    main()