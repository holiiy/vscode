import os
import requests
from tqdm import tqdm
 
def download_file():
    # 获取用户输入的 URLs
    urls = input("请输入文件的 URLs (使用 ',' 分隔每个 URL): ")
    url_list = urls.split(',')
 
    # 获取用户输入的存储目录
    directory = input("请输入存储目录: ")
 
    # 检查目录是否存在
    if not os.path.exists(directory):
        print("目录不存在，请重新输入")
        return
 
    for url in url_list:
        url = url.strip()  # 去除可能的前导和尾随空格
 
        # 从 URL 中生成一个默认文件名（URL 的最后一部分）
        filename = url.split('/')[-1]
 
        # 合并目录和文件名来获取完整的文件路径
        filepath = os.path.join(directory, filename)
 
        try:
            # 发送一个HTTP请求到URL
            response = requests.get(url, stream=True)
 
            # 确保请求成功
            response.raise_for_status()
            
            # 获取文件大小
            file_size = int(response.headers.get('Content-Length', 0))
 
            # 初始化进度条
            progress = tqdm(response.iter_content(1024), f'Downloading {filename}', total=file_size, unit='B', unit_scale=True, unit_divisor=1024)
            
            # 以二进制模式打开一个新的文件
            with open(filepath, 'wb') as file:
                for data in progress.iterable:
                    # 写入文件并更新进度条
                    file.write(data)
                    progress.update(len(data))
        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.RequestException) as err:
            print ("Error: ", err)
 
# 使用
download_file()