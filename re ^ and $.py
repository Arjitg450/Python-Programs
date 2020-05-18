import re
pattern = r"^h..o$"
if re.match(pattern,"huuo"):
    print("match1")
if re.match(pattern,"hghk"):
    print("match2")
if re.match(pattern,"auuj"):
    print("match3")
