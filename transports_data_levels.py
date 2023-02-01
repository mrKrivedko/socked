def application (data, protocol):
    """
    Уровень, функция application() - отвечает за формат данных, их шифрование
    input функции - данные, которые хотим отправить по сети, протокол данных ('SMTP','HTTP','FTP')
    output: данные + информация про формат данных и шифрование.
    """
    return {'data': data, 'protocol': protocol}

def transport(data, protocol):
    """
    3 уровень, функция transport() - отвечает за способ передачи данных и их транспортировку
    input: результат работы функции application(), протокол транспортировки данных ('TCP', 'UDP')
    output: данные + информация про транспортировку.
    """
    return {'data': data, 'protocol': protocol}

def internet(data):
    """
    2 уровень, функция internet() - отвечает за маршрутизацию в сети. Она ищет кому и как доставить данные
    input: результат работы функции transport()
    output: данные + информация про адресата и маршрут доставки.
    """
    return {'data': data}

def network_interface (data, connection):
    """
    1 уровень, функция network_interface - отвечает за соединение с сетью
    input: результат работы функции internet(), информация о соединении
    output: кортеж из 2 значений:
        1. данные, преобразованные в бинарный формат.
        2. информация о типе соединения (1 - 'Ethernet', 2 -'Wi-Fi', другие числа - "No connection").
    """
    ...

data = '01101'
print (data)
data_app = application(data,'SMTP')
print ('application level - ', data_app)
data_transport = transport (data_app,'TCP')
print ('transport level - ', data_transport)
data_ip = internet (data_transport)
print ('internet level - ', data_ip)
data_from_network = network_interface (data_ip,'Wi-Fi')
print ('network_interface level - ', data_from_network)