"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import time


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)

        driver = webdriver.Chrome()

        driver.get('https://www.ssa.gov/oact/babynames/decades/names' + year + '.html')

        # 等待頁面完全載入
        time.sleep(2)  # 給予 2 秒載入時間

        # Get the entire HTML content of the page
        html = driver.page_source
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        #total_men, total_women = 0, 0  # 老師設定的tuple
        #  右鍵 > inspect > 可以往上爬(爬到table)，不要往下爬
        tags = soup.find_all('table', {'class': "t-stripe"})
        #print(type(tags))  # 看看 tags 的datatype = resultset(不能直接tags.text)

        for tag in tags:
            #print(type(tag))
            #print(tag.text)
            # string: '...\n95\nBlake 41, 717 Alexandra 30, 968\n96\n'
            tokens = tag.text.split()
            #print(tokens)
            num_count = 0
            male_number = 0
            female_number = 0
            for token in tokens:
                if ',' in token:
                    num_count += 1
                    if num_count % 2 == 1:
                        # male
                        # 122,456
                        token_number = int(token.replace(',', ''))
                        male_number += token_number
                    else:
                        # female
                        # 96,345 有逗號要重串
                        token_number = int(token.replace(',', ''))
                        female_number += token_number
            print('Male Number: ' + str(male_number))
            print('Female Number: ' + str(female_number))
        driver.quit()


if __name__ == '__main__':
    main()
