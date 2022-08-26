# -*- coding: UTF-8 -*-
import yaml

# 读取yaml文件
def get_test_data(test_data_path):
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    with open(test_data_path,encoding='utf8') as f:
        dat = yaml.load(f, Loader=yaml.SafeLoader)
        print(dat)
        test = dat['tests']
        for td in test:
            case.append(td.get('case', ''))
            http.append(td.get('http', {}))
            expected.append(td.get('expected', {}))
        print("------case-----------")
        print(case)
        print("------http---------")
        print(http)
        print("------expected-------")
        print(expected)
    parameters = zip(case, http, expected)
    return case, parameters

if __name__ =="__main__":
    path0="test_products.yaml"
    get_test_data(path0)