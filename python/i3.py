import os

import requests
from bs4 import BeautifulSoup
import mysql.connector

# 创建数据库连接
conn = mysql.connector.connect(
    host="192.168.5.151",
    user="esports",
    password="123456",
    database="esports"
)

# 创建游标对象
cursor = conn.cursor()

'''


def download_and_save_image(image_url, save_path):
    """
    下载图片并保存到指定路径
    参数：
    image_url (str): 图片的 URL
    save_path (str): 保存图片的路径
    """
    try:
        response = requests.get(image_url, verify=False)
        with open(save_path, "wb") as f:
            f.write(response.content)
        print("已下载图片文件:", os.path.basename(save_path))
    except Exception as e:
        print(f"下载图片时出错: {e}")


# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')

# 图片文件保存目录
save_dir2 = "../resource/recomment/video_cover"

# 提取有效数据并打印
# videos = soup.find('div', class_='video-content')
video_cards = soup.find_all('a', class_='video-card')
for card in video_cards:
    video_title = card.find('div', class_='video-card-title').text.strip()
    video_cover = card.find('div', class_='lazy-image')['style']
    video_cover = 'http:' + video_cover.split("url(")[-1].split(")")[0].strip('\'"')
    video_link = card['href']
    video_count = card.find('span', class_='count').text.strip()
    video_like = card.find('span', class_='like').text.strip()
    video_duration = card.find('div', class_='right').text.strip()

    # 提取文件名
    file_name = video_cover.split("/")[-1]
    # 保存图片到指定目录
    save_path = os.path.join(save_dir2, file_name)
    download_and_save_image(video_cover, save_path)
    video_cover = "http://121.36.26.12:8081/resource/recomment/video_cover/" + file_name

    # 插入视频信息到 video 表
    cursor.execute("INSERT INTO video (video_title, video_cover, video_link, video_count, video_like, video_duration,type) VALUES (%s, %s, %s, %s, %s, %s,%s)",
                   (video_title, video_cover, video_link, video_count, video_like, video_duration,"1"))
    conn.commit()

    # 打印结果
    print(f"视频标题: {video_title}")
    print(f"视频封面链接: {video_cover}")
    print(f"视频链接: {video_link}")
    print(f"视频播放数: {video_count}")
    print(f"视频点赞数: {video_like}")
    print(f"视频总时长: {video_duration}")
    print("----------")