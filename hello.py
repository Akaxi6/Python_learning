def main():
    if __name__ == '__main__':   # 定义的函数名字作为__name__属性，函数名字就代替了name
        print('This program is run directly')
    elif __name__ == 'hello':
        print('This program is used as a module')