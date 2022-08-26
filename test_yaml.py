import  yaml

#解析数据
data0 = """

- Cat
- Dog
- Goldfish
"""
print(yaml.safe_load(data0)) #['Cat', 'Dog', 'Goldfish']

data1 = {
    "name":'xiaoming',
    'age':20
}

print(yaml.safe_dump(data1))
#写入文件

data2 = {
    'data':[1,2,3,4,5],
    "name":'xiaoming',
    'age':20
}
with open('./data.yaml',mode='w',encoding='utf8') as file:
    yaml.safe_dump(data2,file)

#文件读取

with open('./data.yaml',mode='r',encoding='utf8') as file:
    print(yaml.safe_load(file))