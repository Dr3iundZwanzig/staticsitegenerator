class HTMLnode():
    def __init__(self, tag=None, value=None, children=None,  props=None):
        self.tag = tag              #string like "h1"
        self.value = value          #string value of the tag
        self.children = children    #list of HTMLnode objects
        self.props = props          #dictionary attributes of the tag

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        return " "+" ".join(f'{key}="{value}"' for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLnode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLnode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
