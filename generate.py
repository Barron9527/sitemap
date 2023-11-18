def generate_sitemap(input_file, output_file):
    # 读取 url.txt 文件中的超链接
    with open(input_file, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file]

    # 生成 sitemap.xml 内容
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for url in urls:
        sitemap_content += f'  <url>\n    <loc>{url}</loc>\n  </url>\n'

    sitemap_content += '</urlset>'

    # 将 sitemap 内容写入输出文件
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write(sitemap_content)

if __name__ == "__main__":
    input_url_file = "url.txt"
    output_sitemap_file = "sitemap.xml"

    generate_sitemap(input_url_file, output_sitemap_file)

    print("Sitemap generation complete. See sitemap.xml.")