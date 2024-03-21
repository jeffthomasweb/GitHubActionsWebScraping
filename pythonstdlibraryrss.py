import xml.etree.ElementTree as ET

def xml_parser_xpath(local_file: str) -> list[str]:

    read_file_as_bytes: bytes = b""

    #Read xml file saved locally
    with open(local_file, "rb") as xmlfile:
        read_file_as_bytes = xmlfile.read()

    tree: ET.Element = ET.fromstring(read_file_as_bytes)
    
    #Using Xpath

    #Get Story title
    xpath_title: list[ET.Element] = tree.findall(".//item/title")

    #Get Story description
    xpath_description: list[ET.Element] = tree.findall(".//item/description")

    final_list: list[str] = []
    
    length_xpath_stories: int = len(xpath_title)
    
    for i in range(0, length_xpath_stories):
        if (xpath_title[i].text is not None and xpath_description[i].text is not None):
            final_list.append(". ".join([str(xpath_title[i].text), \
                str(xpath_description[i].text)]))
    
    return final_list

npr_rss_list = xml_parser_xpath("npr.xml")
ars_rss_list = xml_parser_xpath("arstechnica.xml")
wgrz_rss_list = xml_parser_xpath("wgrznews.xml")

with open("rss_feeds_combined.txt", "w") as output_file:
    output_file.writelines("**********NPR stories**********\n\n")
    for individual_npr in npr_rss_list:
        output_file.writelines(individual_npr)
        output_file.writelines("\n\n")
    output_file.writelines("**********Ars Technica stories**********\n\n")
    for individual_ars in ars_rss_list:
        output_file.writelines(individual_ars)
        output_file.writelines("\n\n")
    output_file.writelines("**********Buffalo News stories**********\n\n")
    for individual_buffalo in wgrz_rss_list:
        output_file.writelines(individual_buffalo)
        output_file.writelines("\n\n")
