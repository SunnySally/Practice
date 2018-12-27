import urllib.request
import json
list = [603869, 603829, 600088, 603500, 600022, 600036, 600048, 600169, '000723', 600282, 600507, '002812', '002563', 603866, 603757, 603222, '002730', '002409', '002605', 601500, 603488, '000869', '002841', 603288]
jsonList = []
for l in list:
    url = 'http://ai.iwencai.com/diag/V3/detail/actualcontrolperson?code=' + str(l)
    strHtml = urllib.request.urlopen(url).read()
    # print(strHtml)
    newObject = strHtml.decode('utf-8')
    # json_str = json.dumps(strHtml)
    # print(newObject)
    jsonList.append(newObject)
# print(jsonList)
f = open('./result.json', 'w')
json.dump(jsonList, f)
print('生成Json文件完成！')