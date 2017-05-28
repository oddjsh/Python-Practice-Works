import csv
#導入CSV功能

with open('example.csv') as csvfile :
    readCSV = csv.reader(csvfile,delimiter=',')
#設定readCSV為讀取CSV檔案的指令，並且透過逗號來區分每一排
    dates = []
#設定Dates列表
    colors = []
#設定colors列表
    for row in readCSV:
#指定row(排)在CSV中的位置
        color = row[3]
        #顏色是第四排
        date = row[0]
        #日期為第一排

        print(row)
        #顯示全部排
        print(row[0])
        #顯示第一排
        print(row[0],row[1],row[2])
        #顯示一、二、三排

        dates.append(date)
        #在Dates列表中增加日期(第一排)的資料
        colors.append(color)
        #在Colors列表中增加顏色(第四排)的資料
            
    print(dates)
    #顯示日期
    print(colors)
    #顯示顏色
    try:
    #讓使用者能夠做不同輸入嘗試，防止在使用者輸入錯誤後使整個script停止
        whatColor = input('What color do you wish to know the date of?')
        #定義user input詢問使用者想知道哪個顏色對應的日期

        if whatColor in colors:
        #再訂一個一if statement作為使用者的輸入檢查
        #大部分try,except為最後的檢查手段(避免程式錯誤終止)
        #因此在那之前最好先設定if, else來做其他淺島的檢查手段
        #並將所有指令放入try,except中來對所有指令的最終檢查
        
            coldex = colors.index(whatColor.lower())
            #定義輸入的資料為顏色(red,green,blue)中所對應的哪一個
            #.lower()能將使用者輸入自動變成小寫，就不會因大小寫問題而影響指令
            
            theDate = dates[coldex]
            #抓取在dates中每個顏色所對應的日期
            print('The date of',whatColor,'is:',theDate)
        else:
            print('Color not found, or is not a color!')
            #當if statement不成立時顯示
        
    except Exception as e:
    #定義當使用者輸入錯誤(exception)時
        print(e)
        #將顯示'input is not in list(使用者輸入不再列表中)'

    print('continuing')
    #最後將顯示一個繼續
