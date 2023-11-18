from bs4 import BeautifulSoup

def extract_links(input_file, output_file):
    # 读取 HTML 文件
    with open(input_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找包含 'gocshie.com' 的超链接
    links = [a['href'] for a in soup.find_all('a', href=True) if 'gocshie.com' in a['href']]

    # 去重
    unique_links = list(set(links))

    # 将链接写入输出文件
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for link in unique_links:
            out_file.write(link + '\n')

if __name__ == "__main__":
    input_html_file = "src.html"
    output_url_file = "url.txt"

    extract_links(input_html_file, output_url_file)

    print("Extraction complete. Unique links written to url.txt.")