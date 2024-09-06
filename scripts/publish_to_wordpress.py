import os
import requests
from datetime import datetime, timezone

def publish_to_wordpress():
    wordpress_url = os.getenv('WORDPRESS_URL')
    wordpress_username = os.getenv('WORDPRESS_USERNAME')
    wordpress_password = os.getenv('WORDPRESS_PASSWORD')

    # 获取今天的日期并格式化
    today = datetime.now(timezone.utc)
    date_today = today.strftime('%Y-%m-%d')

    # 获取最新的Markdown文件内容
    file_name = f'data/producthunt-daily-{date_today}.md'
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    # 构建请求数据
    post_data = {
        'title': 'PH今日热榜',
        'content': content,
        'status': 'publish'
    }

    # 构建请求头
    headers = {
        'Content-Type': 'application/json'
    }

    # 构建请求URL
    api_url = f'{wordpress_url}/wp-json/wp/v2/posts'

    # 发送POST请求
    response = requests.post(api_url, json=post_data, headers=headers, auth=(wordpress_username, wordpress_password))

    # 检查响应状态
    if response.status_code == 201:
        print("Post published successfully.")
    else:
        print(f"Failed to publish post: {response.status_code}, {response.text}")

if __name__ == "__main__":
    publish_to_wordpress()
