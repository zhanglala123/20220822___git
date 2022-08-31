import  json

jstr = json.dumps(['hello',{'username':'xiaoming'}])
# 转换为字符串
print(jstr, type(jstr)) # ["hello", {"username": "xiaoming"}] <class 'str'>

with open('./data.txt',mode='w') as file:
    file.write(jstr)

#----------------------------------------------------------------------------
ls = json.loads('["hello", {"username": "xiaoming"}]')
print(ls,type(ls))

#-----------------------------------------------------------
#import  json
test_data = {
    "id":1,
    "test_steps":[
        "1.打开浏览器",
        "2.输入用户信息"
    ]
}

with open('./data.json',mode='w',encoding='utf8') as file:
    json.dump(test_data, file)

#--------------------------------------------------------------
#import  json
with open('./data.json',encoding='utf8') as file:
    data = json.load(file)
    print(data,type(data)) # {'id': 1, 'test_steps': ['1.打开浏览器', '2.输入用户信息']} <class 'dict'>