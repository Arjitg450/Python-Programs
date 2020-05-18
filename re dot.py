import re
pattern = r"h..o"
if re.match(pattern,"huuo"):
    print("match1")
if re.match(pattern,"hgho"):
    print("match2")
if re.match(pattern,"huuj"):
    print("match3")
