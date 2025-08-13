import os
from markdown_to_html import markdown_to_html_node
from extract_markdown import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r") as f:
        markdown_file = f.read()
    with open(template_path, "r") as t:
        template_file = t.read()

    html = markdown_to_html_node(markdown_file).to_html()
    title = extract_title(markdown_file)
    
    template_file = template_file.replace("{{ Title }}", title)
    template_file = template_file.replace("{{ Content }}", html)

    with open(dest_path, "w") as d:
        d.write(template_file)