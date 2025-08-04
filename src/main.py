from textnode import TextNode, TextType

def main():

    node1= TextNode("Hello", TextType.TEXT)
    node2 = TextNode("world", TextType.LINK, "http://example.com")

    print(node1)
    print(node2)
    print(node1 == node2)  

if __name__ == "__main__":
    main()