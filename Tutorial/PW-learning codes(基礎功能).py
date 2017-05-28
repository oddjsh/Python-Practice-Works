def epic():
    ('wow this is great!')
#定義EPIC的功能
if __name__ == '__main__':
    print('such great module!')
#定義當執行的文件是這個文件(PW-learning code.py)時
#將會印出such great module這行文字
#反之當執行的文件不是這個文件而是由其他文件導入(import)此文件時
#將不會執行這行命令下的指令


print('''

So this is a simple
muti-line
print, pretty cool, huh? or eh?

===============
|             |
|             |
|             |
|    B O X    |
|             |
|             |
|             |
===============

''')
#一次顯示許多行的方式

#abs(絕對值)
exNum1 = -5
exNum2 = 5

print(abs(exNum1))

if abs(exNum1) == abs(exNum2):
    print('The absoultly value of these two are the same.')

#輸入help()可以開啟python幫助搜尋功能
#按Ctrl+C可以退出
#也可以在import一個module後再打help(module)也會跑出功能說明

#在Shell中輸入Alt+P可以叫出上一個輸入的指令


#顯示列表最大最小值
exList = [1,2,3,6,7,44,8,89]

print(max(exList))
#max為找最大值公式
print(min(exList))
#min為找最小值公式


#四捨五入公式(round)
x = 5.622
print(round(x))

x = 5.222
print(round(x))

#無條件捨去或進位公式(math.floor / math.ceil)
import math
print(math.floor(x))

print(math.ceil(x))

#int(number/string[,base])轉換數字或字串為整數，如果是字串，需提供進位的基數
intMe = 5+6

#str(x)將x轉為字串
print(str(intMe))
