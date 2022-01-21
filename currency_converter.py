import requests, json

currency = input()
lower_currency = currency.lower()
r = requests.get('http://www.floatrates.com/daily/' + lower_currency + '.json').json()
added_currency = []

if currency == 'eur':
    usd = open('usd2.txt', 'a')
    usd.write(str(r['usd']['rate']) + '\n')
    usd.close()
    added_currency.append('usd')
elif currency == 'usd':
    eur = open('eur2.txt', 'a')
    eur.write(str(r['eur']['rate']) + '\n')
    eur.close()
    added_currency.append('eur')
elif currency != 'usd' and currency != 'eur':
    usd = open('usd2.txt', 'a')
    usd.write(str(r['usd']['rate']) + '\n')
    usd.close()
    added_currency.append('usd')
    eur = open('eur2.txt', 'a')
    eur.write(str(r['eur']['rate']) + '\n')
    eur.close()
    added_currency.append('eur')

def check_rates():
    global r, added_currency
    wanted_currency = input()
    lower_wanted = wanted_currency.lower()
    if len(wanted_currency) == 0:
        exit()
    amount = float(input())
    print('Checking the cache...')
    if wanted_currency in added_currency:
        print('Oh! It is in the cache!')
        exchange = open(lower_wanted + '2.txt', 'r')
        for i in range(1):
            for line in exchange:
                rate = float(line)
        exchange.close()
        total = round(amount * rate, 2)
        print(f'You received {total} {wanted_currency.upper()}.')
        check_rates()
    else:
        print('Sorry, but it is not in the cache!')
        rate = float(r[wanted_currency]['rate'])
        total = round(amount * rate, 2)
        print(f'You received {total} {wanted_currency.upper()}.')
        added_currency.append(wanted_currency)
        exchange = open(lower_wanted + '2.txt', 'a')
        wanted = str(r[wanted_currency]['rate'])
        exchange.write(wanted + '\n')
        exchange.close()
        check_rates()

check_rates()
