import re
txt = "hello my name is Arumugam. hei"

pattern = r"my name is .\w+"
result = re.findall(pattern, txt)
print(result)

