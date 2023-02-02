import socket

# Подключаем сокет к порту, через 
# который прослушивается сервер
server_address = ('localhost', 8080)
with socket.create_connection(server_address) as sock:
    print('Подключено к:', server_address)
    # Отправка данных
    mess = 'Привет!'
    print(f'Отправка: {mess}')
    message = mess.encode()
    sock.sendall(message)
    
    # Смотрим ответ
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        mess = data.decode()
        print(f'Получено: {data.decode()}')

print('Отключено от:', server_address)

# Подключено к: ('localhost', 8080)
# Отправка: Привет!
# Получено: ПРИВЕТ!
# Отключено от: ('localhost', 8080)