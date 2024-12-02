'''Node classes'''

class HTMLNode():
    def __init__(self, tag = None, value = None, 
                 children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __repr__(self) -> str:
        return (
            f"tag: {self.tag}\n"
            f"value: {self.value}\n"
            f"children: {self.children}\n"
            f"props: {self.props}"
        )

    def to_html(self):
        raise NotImplementedError
            
    def props_to_html(self):
        if self.props is None:
            return ""
        return  "".join([f' {k}="{v}"' for k, v in  self.props.items()])
    
class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, 
                 props=None) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            return ValueError

        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, 
                 props=None) -> None:
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag value")

        if self.children == []:
            raise ValueError("No children input")
        
        child_html = ""
        for child in self.children:
            child_html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{child_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"