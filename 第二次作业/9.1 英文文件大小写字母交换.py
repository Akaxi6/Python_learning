# 假设有一个英文文件（Akaxi_1）编写程序读取其内容，并将其中的大写字母变成小写字母，小写字母变成大写字母

with open('Akaxi_1.txt', 'r') as fp:    # 读取内容

    content = fp.read()
    print(content)
    new_content = ''    # 建立空字符串用来保存大小写替换

    for char in content:
        if char.isupper():
            new_char = char.lower()
        elif char.islower():
            new_char = char.upper()
        else:
            new_char = char
        new_content = new_content + new_char
    print(new_content)

with open('Akaxi_1_changed.txt', 'w') as fp:    # 修改内容
    fp.write(new_content)





















