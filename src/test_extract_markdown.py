import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links, extract_title

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i,imgur.com/hund.png)"
        )
        matches2 = extract_markdown_images(
            "This is text with an [image](https://i,imgur.com/hund.png)"
        )
        self.assertEqual([("image", "https://i,imgur.com/hund.png")], matches)
        self.assertNotEqual([("image", "https://i,imgur.com/hund.png")], matches2)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://i,imgur.com/cat.png)"
        )
        matches2 = extract_markdown_links(
            "This is text with a ![link](https://i,imgur.com/cat.png)"
        )
        self.assertEqual([("link", "https://i,imgur.com/cat.png")], matches)
        self.assertNotEqual([("link", "https://i,imgur.com/cat.png")], matches2)
    
    def test_extract_markdown_nothing(self):
        matches = extract_markdown_images("!Nothing")
        self.assertEqual([], matches)

    def test_extract_title(self):
        text = """
# Tolkien F#an Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien

## Blog posts

- [Why Glorfindel is More Impressive than Legolas](/blog/glorfindel)
- [Why Tom Bombadil Was a Mistake](/blog/tom)
- [The Unparalleled Majesty of "The Lord of the Rings"](/blog/majesty)

## Reasons I like Tolkien

- You can spend years studying the legendarium and still not understand its depths
- It can be enjoyed by children and adults alike
- Disney _didn't ruin it_ (okay, but Amazon might have)
- It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Aiya, Ambar!")
}
```

Want to get in touch? [Contact me here](/contact).

This site was generated with a custom-built [static site generator](https://www.boot.dev/courses/build-static-site-generator-python) from the course on [Boot.dev](https://www.boot.dev).

"""
        title = extract_title(text)

        self.assertEqual("Tolkien F#an Club", title)