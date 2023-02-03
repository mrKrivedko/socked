import socket

# Подключаем сокет к порту, через 
# который прослушивается сервер
server_address = ('swapi.dev', 80)
with socket.create_connection(server_address) as sock:
    print('Подключено к:', server_address)
    # Отправка данных
    mess = 'hello! this ilon mask fucked day now'
    print(f'Отправка: {mess}')
    message = b'GET /api/ HTTP/1.1\r\nHost:www.swapi.dev\r\n\r\n'
    sock.sendall(message)
    
    # Смотрим ответ
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(4096)
        amount_received += len(data)
        mess = data.decode()
        print(f'Получено: {data.decode()}')

print('Отключено от:', server_address)

# Подключено к: ('localhost', 8080)
# Отправка: Привет!
# Получено: ПРИВЕТ!
# Отключено от: ('localhost', 8080)
