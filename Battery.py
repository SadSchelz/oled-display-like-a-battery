import time, ssd1306, gfx
from machine import Pin, I2C

i2c = I2C(-1, scl=Pin(17), sda=Pin(16))

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

graphics = gfx.GFX(128, 64, oled.pixel)

BatteryNum = 100

def BatteryCubes():
    if BatteryNum == 75:
        graphics.fill_rect(96, 0, 30, 64, 0)
        graphics.rect(96, 0, 30, 64, 1)
    elif BatteryNum == 50:
        graphics.fill_rect(64, 0, 30, 64, 0)
        graphics.rect(64, 0, 30, 64, 1)
    elif BatteryNum == 25:
        graphics.fill_rect(32, 0, 30, 64, 0)
        graphics.rect(32, 0, 30, 64, 1)
    elif BatteryNum == 0:
        graphics.fill_rect(0, 0, 30, 64, 0)
        graphics.rect(0, 0, 30, 64, 1)  

graphics.fill_rect(0, 0, 30, 64, 1)
graphics.fill_rect(32, 0, 30, 64, 1)
graphics.fill_rect(64, 0, 30, 64, 1)
graphics.fill_rect(96, 0, 30, 64, 1)
graphics.rect(0, 0, 30, 64, 0)
graphics.rect(32, 0, 30, 64, 0)
graphics.rect(64, 0, 30, 64, 0)
graphics.rect(96, 0, 30, 64, 0)      
while BatteryNum >= 0:
    BatteryCubes()
    oled.show()
    BatteryNum -= 25
    time.sleep(3)
