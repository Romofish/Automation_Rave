from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# 指定 ChromeDriver 路径
driver_path = './backend/chromedriver.exe'
service = Service(executable_path=driver_path)

# 指定 Chrome 用户数据目录路径
user_data_dir = r'C:\Users\Public\AppData\Local\Google\Chrome\User Data'

# 设置 Chrome 选项以使用特定的用户数据目录
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")

# 初始化 WebDriver
browser = webdriver.Chrome(service=service, options=chrome_options)

# 打开一个网页

login_url = 'https://www.imedidata.com/'
home_url = 'https://home.imedidata.com/'

browser.get(login_url)

current_url = browser.current_url
if current_url != home_url:
    print('Not logged in. Please log in first.')
    input('Press Enter to close the browser...')
    browser.quit()
    exit()
else:    
    study_link = browser.find_element(By.LINK_TEXT, '文库')
    study_link.click()

input('Press Enter to close the browser...')
browser.quit()

# 注意：不要立即关闭浏览器，如果需要长时间操作
# browser.quit()

