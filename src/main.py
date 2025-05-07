from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    nodeT = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(nodeT)
    nodeH = HTMLNode('a', 'paragraph value', '',
                     {"href": "https://www.google.com","target": "_blank",})
    print(nodeH)

main()