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

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path.replace(".md", ".html"), "w") as d:
        d.write(template_file)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content = os.listdir(dir_path_content)
    for object in content:
        if os.path.isfile(os.path.join(dir_path_content, object)):
            print("isFile")
            generate_page(os.path.join(dir_path_content, object), template_path, os.path.join(dest_dir_path, object))
        if os.path.isdir(os.path.join(dir_path_content, object)):
            generate_pages_recursive(os.path.join(dir_path_content, object), template_path, os.path.join(dest_dir_path, object))