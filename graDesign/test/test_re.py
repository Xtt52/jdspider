import re

product_name = '商品名称：联想拯救者Y7000P'
match_re = re.match(".*：(.*)", product_name)
if match_re:
    product = match_re.group(1)
else:
    product = "name未匹配。。。"

match_re = re.match("(.*)：", product_name)
if match_re:
    product_tag = match_re.group(1)
else:
    product_tag = "tag未匹配。。。"

print(product)
print(product_tag)
