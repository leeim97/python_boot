import sys

# print(sys.path)
for path in sys.path:
    print(path)

print(type(sys.path))

# 파이썬 모듈 검색 경로
#1. sys.modules
#2. built_in_modules
#3. sys.path

sys.path.append("/15_module_package/modules")

from show_info1 import *

show_name1()