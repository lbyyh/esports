from bs4 import BeautifulSoup
import mysql.connector
import requests
import os


# 创建数据库连接
conn = mysql.connector.connect(
    host="192.168.5.151",
    user="esports",
    password="123456",
    database="esports"
)
# 创建游标
cursor = conn.cursor()
# 图片文件保存目录
save_dir = "../resource/legacy"

def download_and_save_image(image_url, save_dir):
    """
    下载图片并保存到指定目录

    参数：
    image_url (str): 图片的 URL
    save_dir (str): 保存图片的目录
    """
    try:
        response = requests.get(image_url, verify=False)
        # 提取文件名
        file_name = image_url.split("/")[-1]
        # 保存图片到指定目录
        save_path = os.path.join(save_dir, file_name)
        with open(save_path, "wb") as f:
            f.write(response.content)
        print("已下载图片文件:", file_name)
    except Exception as e:
        print(f"下载图片时出错: {e}")


html = '''<div class="team-wrap" data-v-5bc87674=""><ul class="team-list" data-v-5bc87674="" style="transform: translate(-861px);"><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/0a2f3ad91e14602eae4c10b70403681d9032f8c8.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">UP</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/a1858308f7251261f8d3a97912abcdf39f2152b5.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">TES</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/176363723a29df1246030e3eba51e71d3be00373.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">LNG</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/7a0bd8b0bcc77dd4a3b7687d7349dcb8d5d8ac9f.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">TT</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/c86ac68213687d66a15fd3ff66668e6ba3c17328.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">NIP</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/05a37988ad4e87fba7ca6b0eadb603982e41cad7.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">FPX</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/b8e287225a586dded6e24d183e17351eacec379c.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">OMG</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/7af596e4a35b7e287ff7ceb3bd42d4ba638d106b.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">AL</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/256e6b6c4e57ca196feb0ff3661daed4686a0f72.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">RA</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/1eb01d43ce5069e04ff3df69e949cae2d9929915.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">JDG</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/737aeb7338739305c1f65c36eb1ef72f9ce3d098.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">WBG</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/7dff90050ed9335b600a61239439fd379ddaa3ee.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">LGD</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/cd94367914022022c4f0ea5eab3307a7c74df1ae.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">RNG</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/9f0e6cf7c384d96a46720c86b43a45a60df5b9eb.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">EDG</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/bc9fb3f95f9f6e4cc5d2313d3d8e3b7b3086fa83.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">WE</span></li><li class="team" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/3e875598eb939cbeca899f3322a4e5474f160561.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">IG</span></li><li class="team team-active" data-v-5bc87674=""><img src="//i1.hdslb.com/bfs/legacy/2ca4893d7e2f2f85ba22fbd4ce1c2067713df81a.png@64w_64h.avif" loading="lazy" class="team-logo" data-v-5bc87674=""><span class="team-name" data-v-5bc87674="">BLG</span></li></ul></div>'''

soup = BeautifulSoup(html, 'html.parser')

teams = soup.find_all('li', class_='team')

team_info = []
for team in teams:
    team_name = team.find('span', class_='team-name').text
    team_logo = team.find('img')['src']
    team_info.append((team_name, team_logo))

# 创建表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS teamss (
        id INT AUTO_INCREMENT PRIMARY KEY,
        team_name VARCHAR(255),
        team_logo VARCHAR(255)
    )
""")

# print(team_logo)

for name, logo in team_info:
    # 下载并保存图片
    # download_and_save_image("http:"+logo, save_dir)
    # 插入数据到表
    cursor.execute("INSERT INTO teamss (team_name, team_logo) VALUES (%s, %s)", (name, "http://121.36.26.12:8081/resource/legacy/"+logo.split("/")[-1]))

conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()