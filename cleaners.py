def clean(link):
    link = str(link)
    if link == None:
        return ""
    if link.lower() == "nan":
        return ""
    if link.lower() == "none":
        return ""
    if link.lower() == "no":
        return ""
    return link
