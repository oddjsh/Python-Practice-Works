import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green
#畫點(第一行=>顯示位置,第二行=>顯示的點,顏色

pygame.draw.line(gameDisplay, blue, (100,200),(300,450),5)
#畫線(顯示位置,顏色,兩點座標,線的寬度)

pygame.draw.rect(gameDisplay,red , (400,400,50,25))
#畫長方形(顯示位置,顏色,左上角定位點,長,寬)

pygame.draw.circle(gameDisplay, white, (150,150), 75)
#畫圓圈(顯示位置,顏色,中心點,半徑)

pygame.draw.polygon(gameDisplay, green, ((25,75),(76,125),(250,375),(400,25),(60,540)))
#畫不規則形狀(顯示位置,顏色,顯示的點)會依據順序將點連起來後填滿顏色

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
