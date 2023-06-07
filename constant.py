from screeninfo import get_monitors


constants = {
    'browser_name' : 'chrome',
    'browser_driver_path' : 'PROJECT AREA/Scraping/Ants/lib/geckodriver.exe',
    'get_monitor' : get_monitors()[0],
    'monitor_height' : int(get_monitors()[0].height * 60 / 100),
    'monitor_width' : int(get_monitors()[0].width * 85 / 100)
    }