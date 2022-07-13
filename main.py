from bs4 import BeautifulSoup


def getPizzas():
    with open('home.html', 'r') as html_file:
        content = html_file.read()
        beautiful_soup = BeautifulSoup(content, 'html.parser')
        pizza_cards = beautiful_soup.find_all('div', class_='card')
        for index, pizza in enumerate(pizza_cards):
            pizza_name = pizza.h5.text
            pizza_price = pizza.a.text.split(' ')[-1]
            with open(f'pizza_info/{index}.txt', 'w') as files:
                files.write(f'{pizza_name} goes for price {pizza_price}')


if __name__ == '__main__':
    getPizzas()
