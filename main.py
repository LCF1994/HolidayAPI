import json
import requests
import datetime

TOKEN = "bHVjYXNjYW1wb3NmZUBob3RtYWlsLmNvbSZoYXNoPTEzMTUwMDA2Mw"


def request_json(year_requested, city_name, state_name):
    url = "https://api.calendario.com.br/"
    param = {
        'ano': year_requested,
        'estado': state_name,
        'cidade': city_name,
        'token': TOKEN,
        'json': 'true'
    }
    r = requests.get(url, param)

    return json.loads(r.content), r.status_code


def write_csv(holiday_list: list, year_file):
    with open(f'lista_de_feriados_{year_file}.csv', 'w') as f:
        f.write(';'.join(['date', 'name', 'type', 'description', 'link', 'type_code'])+'\n')

        for holiday in holiday_list:
            line = ';'.join([holiday['date'],
                            holiday['name'],
                            holiday['type'],
                            holiday['description'],
                            holiday['link'],
                            str(holiday['type_code'])
                             ])+'\n'
            f.write(line)


if __name__ == '__main__':
    print('Gerando lista de feriados . . . \n')
    year = datetime.date.today().strftime('%Y')
    api_response, status_code = request_json(year, 'MANGARATIBA', 'RJ')

    write_csv(api_response, year)
    print('Lista de feriados gerada com sucesso !')
    print(f'Arquivo gerado com o nome : lista_de_feriados_{year}.csv')
    input('Press Enter to Exit')
