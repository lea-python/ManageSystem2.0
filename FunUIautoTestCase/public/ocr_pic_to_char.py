from aip import AipOcr


def pic_to_char(filePath):
    APP_ID = '23189955'
    API_KEY = 'UKcGsXBMHx3fx6Ulv3qqPUL2'
    SECRET_KEY = 'HiFguq0jIOAmWTbgHDNnXOB0WMnSddOm'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # 初始化AipFace对象
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    
    # 读取图片
    # filePath = "D:\\ManageSystem2.0\\MoudlePic\\收起侧边栏.png"
    # filePath = "D:\\ManageSystem2.0\\Log\\2023-04-14_LOG\\2023-04-14-16-32-03_院区管理.png"

    
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    
    # 定义参数变量
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }
    
    # 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content(filePath), options)
    print(result)
    words_result=result['words_result']
    print(words_result)
    for k in words_result:
        print(k)

    
pic_to_char(filePath="D:\\ManageSystem2.0\\MoudlePic\\收起侧边栏.png")
