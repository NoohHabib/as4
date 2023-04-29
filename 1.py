import xml.etree.ElementTree as etree

def get_attr_count(elem):
    """Returns the number of attributes of an XML element."""
    return len(elem.attrib)

def get_score(node):
    """Returns the score of an XML node."""
    score = get_attr_count(node)
    for child in node:
        score += get_score(child)
    return score

# read input
n = int(input("num"))
xml = ""
for i in range(n):
    xml += input("enter")

# parse XML document
root = etree.ElementTree(etree.fromstring(xml)).getroot()

# compute score
score = get_score(root)

# output result
print(score)