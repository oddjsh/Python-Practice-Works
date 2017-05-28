exDict = {'Jack':15, 'Bob':22, 'Alice':12, 'Kevin':17}
#創造一個Dictionarites(特殊資料型態類似list,tuple)
#其組成為Key與Value
#Key只能夠擁有一個,即冒號前參數
#而Value(冒號後)可以設無限多個

print(exDict)

print(exDict['Jack'])
#指定要顯示第一個key的參數

exDict['Tim'] = 14
#增加一個新的key叫Tim並增加14進入其中

print(exDict)

exDict['Tim'] = 15
#假設Tim增長一歲 即再次輸入指令更改內容

print(exDict)

del exDict['Tim']
#假設Tim不幸去世 因此要刪除Tim這筆資料 及輸入del(delete) 
print(exDict)

exDict = {'Jack':[15,'blonde'], 'Bob':[22,'brown'],
          'Alice':[12,'black'], 'Kevin':[17,'red']}
#重新使這個Dictionarities改為兩個values

print(exDict['Jack'][1])
#顯示出第一個key中的第二個value
