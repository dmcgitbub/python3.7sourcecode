#! /usr/bin/python
# -*-coding:UTF-8-*-

path = './test.txt'
with open(path, 'w') as f:
    f_name = open(path, 'w')
    print(f"write length:{f_name.write('Hello world!')}")
