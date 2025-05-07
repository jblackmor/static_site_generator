class HTMLNode:
    def __init__ (self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        props_html_string = ""
        if self.props == None:
            return props_html_string
        for k,v in self.props.items():
            props_html_string += f' {k}="{v}"'
        return props_html_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__ (self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("invalid HTML: leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    

class ParentNode(HTMLNode):
    def __init__ (self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("invalid HTML: there must be a tag")
        if self.children == None:
            raise ValueError("invalid HTML: there must be children")
        final_child_string = ''
        for child in self.children:
            final_child_string += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{final_child_string}</{self.tag}>'
    
    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'