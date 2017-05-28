import pygame
#將pygame導入
import time
#將時間導入
import random
#導入隨機的定義


pygame.init()
#開啟遊戲
display_width = 800
display_height = 600
#將顯示的高度與寬度設定為800*600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
#定義顏色(照光譜排列組合:黑無光=>全0 白為全部光的結合=>255(總共256種顏色包含零所以最高255))

block_color = (53,115,255)
#定義障礙物的顏色

car_width = 55
#定義車子的寬度(看圖片的尺寸)

gameDisplay = pygame.display.set_mode((display_width,display_height))
#把pygame顯示出來 set mode為設定顯示的解析度(800*600)
#單一括號會將數字便認為周長，所以要用雙括號
pygame.display.set_caption('Pactical Racing Game')
#設置遊戲的標題(這次為賽車遊戲)
clock = pygame.time.Clock()
#設置遊戲時間(在遊戲中加入時間的元素)
#以上為遊戲基本設定 =>基本上為不變動的元素
#下面開始為遊戲的內容

carImg = pygame.image.load('Race Car.png')
#讀取賽車的圖檔

    

def things_dodged(count):
#增加算分的機制(每躲過一個障礙物加一分)
    font = pygame.font.SysFont(None,25)
    #定義顯示的字體(SysFont為系統預設字體)
    text = font.render("Dodged: "+str(count),True,black)
    #顯示文字的設定
    gameDisplay.blit(text,(0,0))
    #分數要顯示的位置


def things(thingx, thingy, thingw, thingh, color):
#定義障礙物(X座標,Y座標,物件寬,物件高,物件顏色)
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    #畫出障礙物的指令
    
    
def car(x,y):
#定義賽車的位置與其圖片
#pygame中x y的定義與一般相反=>原點在左上角
#因此要選取位置時橫向移動為X的加減 而Y的減值則定義位置的上下
    gameDisplay.blit(carImg,(x,y))
    #將圖片在後台讀取並放置在賽車的位置

def text_objects(text, font):
#定義text_object的功能
    textSurface = font.render(text,True,black)
    #定義text_object的顯示內容(forn.render為顯示物件在新出現的裱框內，在此為文字/黑)
    #中間的TRUE為對平滑化(Antialias)表同意，會使文字的出現較平順
    return textSurface, textSurface.get_rect()
    #使用來叫出框架(get_rect)的(return為定義下所做的動作，在此即為顯示出長方形框架)

def message_display(text):
#定義顯示文字的用途(如何顯示)
    largeText = pygame.font.Font('freesansbold.ttf',115)
    #定義文字的顯示字型(freesansbold)大小(115)
    TextSurf, TextRect = text_objects(text, largeText)
    #定義顯示文字的框架與顯示方式(TextRect表框架為長方形)
    TextRect.center = ((display_width/2),(display_height/2))
    #將文字出現定位點定義
    gameDisplay.blit(TextSurf, TextRect)
    #將定義好的文字與框架顯示在後台

    pygame.display.update()
    #將剛剛在後台顯示的畫面刷新出來顯示在畫面上

    time.sleep(2)
    #將文字顯示時間限制在2秒內，2秒後才能繼續遊戲

    game_loop()
    #將所有東西重設，遊戲重新開始
    

def crash():
#定義撞車(才可以將撞車後的狀態與遊戲結束的狀態分離開來)
    message_display('You Crashed!')
#當撞車時會出現顯示的文字

def game_loop():
#將下方所有遊戲操縱的指令規範在game_loop中好之後做變動
        
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    #XY定義點為圖片顯示點(但是圖片會從此點往右下角伸展，因此若直接等於寬或高會削減到圖片)
    x_change = 0
    #新定義一個X座標變動的指令好用來寫賽車橫向操作移動時的指令

    thing_startx = random.randrange(0, display_width)
    #定義障礙物橫向出現的座標(在此為從座標0到邊界中隨機出現)
    thing_starty = -600 #pixels
    #定義障礙物上下出現的座標(負數表示要在邊界外就先出現因為物件會有不同大小)
    thing_speed = 4 #pixels
    #定義障礙物移動速度
    thing_width = 100
    #定義障礙物寬
    thing_height = 100
    #定義障礙物高

    dodged = 0
    #定義初始分數從0開始

    thingCount = 1
    #挑戰=>增加障礙物數量
    
    gameExit = False
    #定義遊戲結束的方式  #原本Crashed改為gameExit避免一撞車就把遊戲關了
    while not gameExit:
    #定義當遊戲沒有結束時要如何
        for event in pygame.event.get():
    #pygame會自動捕捉所有在遊戲中的任何動態
    #並將其包含在pygame.event.get()中
            if event.type == pygame.QUIT:
    #定義當玩家點選右上方X退出(QUIT在pygame中即為右上角X)時
                pygame.quit()
                quit()
                #當玩家按右上角X時的動作=>離開遊戲

            if event.type == pygame.KEYDOWN:
            #增加條件當按下按鍵(KEYDOWN)時
                if event.key == pygame.K_LEFT:
                #設按下按鍵時的條件，K_LEFT代表方向鍵向左鍵
                    x_change = -5
                    #設遇到上一個條件是觸發的情況，x_change即為上方定義的(初始位置為0)
                elif event.key == pygame.K_RIGHT:
                #設按下按鍵時的條件，K_LEFT代表方向鍵向左鍵
                    x_change = 5
    #下方定義不再按按鍵時的情況 => 如果沒有設定義，就算放開按鍵上方指令還是會持續進行
    #物件或角色就會持續性的向左或向右移動，因此要定義一個當把按鍵放開時會發生的條件
            if event.type == pygame.KEYUP:#KEYUP即為放開按鍵
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0    #定義放開左右鍵時橫向座標改變為0
                  
    #結束loop(這一長串的定義)的條件
        
        x += x_change
    #定義刷新時物件位置改變為初始位置的X加減x_change
        gameDisplay.fill(white)
    #定義刷新顯示為白色(一定要擺在最前面，否則會蓋掉前面的物件=>fill如填滿效果將整個畫面填滿)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
    #重新刷出障礙物用上面定義的things(thingx, thingy, thingw, thingh, color)來寫
        thing_starty += thing_speed
    #讓障礙物能夠持續向下移動(Y座標每次刷新都增加剛剛定義的障礙物速度)
        
        car(x,y)
    #定義要刷新的物品在這為賽車
        things_dodged(dodged)
    #要刷新的分數計算(上面定義的，後面為顯示的次數
    
        if x > display_width- car_width or x < 0:
            crash()
    #設條件當車子碰到邊界即遊戲結束(x定義點為圖片左上，
    #故要將右側邊界減掉圖片的寬度才不會發生圖片出去卻還沒出局的狀況)

        if thing_starty > display_height:
            thing_starty = 0 -thing_height
        #設條件當Y座標大於顯示範圍的高度時就要重新再刷新一次
        #而出現的位置要減掉物件的高度，才不會變成突然出現
            thing_startx = random.randrange(0,display_width)
        #同樣物件的X座標也要隨著重新刷新而改變所以要與上方顯示相同再寫一次，
        #否則物件只會在同一個X座標重複出現
            dodged += 1
        #設條件當閃避障礙物後分數加1
            thing_speed += 1
        #增加遊戲難度當閃避後障礙物移動速度增加
            thing_width += (dodged * 1.2)
        #增加遊戲難度讓每次閃避後障礙物寬度增加

        if y < thing_starty+thing_height:
        #定義撞車的情況(障礙物的Y座標+上障礙物本身的高度大於賽車本身的Y座標時=>撞車)
            print('y crossover')

            if x > thing_startx and x+car_width < thing_startx+thing_width:
            #定義當撞車時的X座標應在哪(撞車時車子的X座標或是X+車寬的座標在障礙物的X座標+寬度的中間)
                print('x crossover')
                crash()
            #定義當y crossover與x crossover同時發生時表示撞車
        
        pygame.display.update()
    #刷新遊戲的顯示(括號中可以選擇特定的刷新物件，如果留白就會刷新整個顯示全部的物件)
    #也可用pygame.display.flip 這就一定會刷新全部的畫面
        clock.tick(60)
    #設定畫面的更新速度(也就是每秒幀率 每一秒鐘顯示多少畫面/張數)越高畫面越順暢

game_loop()
#將gmae_loop重新再跑一次
pygame.quit()
#玩家將遊戲結束的指令(如同開始的init()結束也要有quit)
quit()
#將整個python結束的指令            
