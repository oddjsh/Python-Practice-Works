x = [5,6,7,8,9,1,2,3,4]

x.append(2)
#增加一個數字在列表中(2)
print(x)

x.insert(2,99)
#在第二個數字後面增加99這個數字
print(x)

x.remove(2)
#移除第一個2
print(x)

x.remove(x[2])
#移出第三個(序列從0開始)數字
print(x)

print(x[5:7])
#顯示第六與第七個數字但並不會顯示第八個數字
#(在第五與第七個逗號間的數字只有兩個1,3)

print(x[-1])
#顯示倒數第一個數字

print(x[-2])
#顯示倒數第二個數字

print(x.index(1))
#顯示X列表中數字一所在的序列位置

print(x.count(6))
#顯示X列表中數字6的數量

x.sort()
#將X列表按數字大小重新排列
print(x)

y = ['Janet','Jessy','Kelly','Alice','Joe','Bob']
y.sort()
#sort功能會將文字照字幕順序重新排列
print(y)
y.reverse()
#reverse將會使列表順序顛倒
print(y)
