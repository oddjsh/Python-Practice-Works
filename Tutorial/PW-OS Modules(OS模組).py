import os

curDir = os.getcwd()
#取得現在工作檔案的位置(Current Working Direction)
print(curDir)

os.mkdir('newDir')
#新增一個資料夾

import time

time.sleep(2)
#等待兩秒鐘

os.rename('newDir','newDir2')
#更改資料夾名字
time.sleep(2)

os.rmdir('newDir2')
#刪除資料夾

'''
os模組: 
  os模組包裝了不同操作系統的通用接口，使用戶在不同操作系統下，可以使用相同的函數接口，返回相同結構的結果。 

  os.name:返回當前操作系統名稱（'posix', 'nt', 'os2', 'mac', 'ce' or 'riscos'） 

  os中定義了一組文件、路徑在不同操作系統中的表現形式參數，如 
    os.sep（文件夾分隔符，windows中是 \ ） 
    os.extsep（擴展名分隔符，windows中是 . ） 
    os.pathsep（目錄分隔符，windows中是 ; ） 
    os.linesep（換行分隔符，windows中是 \r\n ） 

  os中有大量文件、路徑操作的相關函數，如： 
    listdir(path):列舉目錄下的所有文件 
    makedir(path):創建文件夾，註：創建已存在的文件夾將異常 
    makedirs(path):遞歸式的創建文件夾，註：創建已存在的文件夾將異常 
    remove(filename):刪除一個文件 
    rmdir(path):刪除一個文件夾，註：刪除非空的文件夾將異常 
    removedirs(path):遞歸的刪除文件夾，直到有一級的文件夾非空，註：文件夾路徑不能以'\'結束 
    rename(src,dst):給文件或文件夾改名（可以改路徑，但是不能覆蓋目標文件） 
    renames(src,dst):遞歸式的給文件或文件名改名 
    walk(path):列舉path下的所有文件、文件夾 

  os中與進程相關的操作，如： 
    execl(path):運行一個程序來替代當前進程，會阻塞式運行 
    _exit(n):退出程序 
    startfile(filename):用與文件關聯的程序運行，關聯程序打開後，立即返回 
    system(cmd):運行一個程序或命令，會立即返回，並在cmd執行完成後，會返回cmd退出代碼 

  os.path
在不同的操作系統中調用不同的模組，是一個可import的模組，這個模組中提供很多有用的操作： 
    abspath(path):返回path的絕對路徑，若path已經是絕對路徑了，則保持。 
    basename(path):返回path中的文件名。 
    commonprefix(list):返回list中的統一前綴，用於獲得一組字符串的左起相同的內容 
    dirname(path):返回path中的文件夾部分，結果不包含'\' 
    exists(path):文件或文件夾是否存在 
    getatime(path):文件或文件夾的最後訪問時間，從新紀元到訪問時的秒數 
    getmtime(path):文件或文件夾的最後修改時間 
    getctime(path):文件或文件夾的創建時間 
    getsize(path):文件或文件夾的大小，若是文件夾返回0 
    isabs(path):返回是否是絕對路徑 
    isfile(path):返回是否是文件路徑 
    isdir(path):返回是否是文件夾路徑 
    islink(path):返回是否是快捷方式 
    join(path1,path2,...):將path進行組合，若其中有絕對路徑，則之前的path將被刪除 
    normcase(path):轉換路徑中的間隔符 
    normpath(path):轉換路徑為系統可識別的路徑 
    realpath(path):轉換路徑為絕對路徑 
    split(path):將路徑分解為(文件夾,文件名) 
    splitext(path):將路徑分解為(其余部分,.擴展名)，若文件名中沒有擴展名，擴展名部分為空字符串 
  在操作與系統不支持的對象時，拋出OSError異常。
'''
