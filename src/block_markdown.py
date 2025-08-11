def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    final_list = []
    for section in sections:
        section = section.strip()
        if section == "":
            continue
        final_list.append(section)
    return final_list