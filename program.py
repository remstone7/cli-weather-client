import requests
import bs4

def main():
    # print header
    print_the_header()
    # get zipcode from user
    code = input('What zipcode do you want for the weather? ')

    html = get_html_from_web(code)
    # parse the html

    get_weather_from_html(html)

    # display the forecast



def print_the_header():
    print('-----------------------')
    print('       WEATHER APP     ')
    print('-----------------------')


def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)

    return response.text

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')

    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    print(condition, temp, scale)

if __name__ == '__main__':
    main()
