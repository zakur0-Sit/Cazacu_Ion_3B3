def build_xml_element(tag, value, **kwargs):
    xml_element = "<" + str(tag)
    for key, val in kwargs.items():
        xml_element += (" " + str(key) + "=\"" + str(val) + "\"")
    xml_element += "> " + str(value) + " </" + str(tag) + ">"
    return xml_element

print(build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))