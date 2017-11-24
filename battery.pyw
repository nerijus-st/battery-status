import psutil
import time
import ctypes

while True:
    battery = psutil.sensors_battery()

    if battery.power_plugged and battery.percent > 97:
        ctypes.windll.user32.MessageBoxW(0, "Battery is at {}".format(battery.percent),
                                         "Battery Info", 0)
    elif battery.power_plugged is False and battery.percent < 30:
        m, s = divmod(battery.secsleft, 60)
        h, m = divmod(m, 60)
        ctypes.windll.user32.MessageBoxW(0, "Battery is at {}% and left {} hr {} min".format(battery.percent, h, m),
                                         "Battery Info", 0)
    time.sleep(60)
