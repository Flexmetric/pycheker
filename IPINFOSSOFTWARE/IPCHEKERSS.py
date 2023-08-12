import requests
from pyfiglet import Figlet
import folium
import sys

def get_info_by_ip(ip='127.0.0.1'):
	try:
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		data = {
			'[IP]': response.get('query'),
			'[Провайдер]': response.get('isp'),
			'[Org]': response.get('org'),
			'[Страна]': response.get('country'),
			'[Регион]': response.get('regionName'),
			'[Город]': response.get('city'),
			'[ZIP]': response.get('zip'),
			'[Lat]': response.get('lat'),
			'[Lon]': response.get('lon'),
		}

		for k, v in data.items():
			print(f'{k} : {v}')

		area = folium.Map(location=[response.get('lat'), response.get('lon')])
		area.save(f'{response.get("query")}_{response.get("city")}.html')

	except requests.exceptions.ConnectionError:
		print('[ОШИБКА] Пожалуйста, просмотрите ваш интернет!')


def main():
	preview_text = Figlet(font='slant')
	print(preview_text.renderText('IPCHEKER SQS'))
	print('\t\tby_SQSoftware')
	print('\t\tНаш тгк:https://t.me/squadsoftware')
	print('\t\tСозал: @zxclrgion')
	try:
		ip = input('Введите сюда IP вашего обидчика: ')
		get_info_by_ip(ip=ip)
	except KeyboardInterrupt:
		print('\n[START] Начинаем поиск:')


if __name__ == '__main__':
	main()

