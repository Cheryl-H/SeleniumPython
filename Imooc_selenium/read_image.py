# _*_coding:utf-8_*_
# 多行注释快捷键 Ctrl+/

from Imooc_selenium.ShowapiRequest import ShowapiRequest

# image = Image.open('D:/F/code.png')
# text = pytesseract.image_to_string(image)

r = ShowapiRequest("http://route.showapi.com/184-5", "81045", "0a36242999594aa4a28ef6d9540180bf")
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addFilePara("image", r"D:/F/code.png")  # 文件上传时设置
res = r.post()
# text = res.json()['showapi_res_body']['Result']
print(res.text)  # 返回信息
