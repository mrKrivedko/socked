import socket

server_address = ('192.168.0.123', 8080)
with socket.create_server(server_address) as sock:
    while True:
        # ждем соединения
        print('Ожидание соединения...')
        connect, client_address = sock.accept()
        print('Подключено к:', client_address)
        # Принимаем данные порциями и ретранслируем их
        connect.setblocking(False)
        try:
            while True:
                data = connect.recv(16)
                print(f'Получено: {data.decode()}')
                if data:
                    print('Обработка данных...')
                    temp_data = data.decode('utf-8').upper()
                    data = temp_data.encode('utf-8')
                    print('Данные обработаны, отправка клиенту...')
                    connect.sendall(data)
                else:
                    print('Нет данных от:', client_address)
                    break
        except socket.error:
            print('Нет данных от:', client_address)
            connect.close()
            # print(f'Получено: {data.decode()}')
            # if data:
            #     print('Обработка данных...')
            #     temp_data = data.decode('utf-8').upper()
            #     data = temp_data.encode('utf-8')
            #     print('Данные обработаны, отправка клиенту...')
            #     connect.sendall(data)
            # else:
            #     print('Нет данных от:', client_address)
            #     break


# Ожидание соединения...
# Подключено к: ('127.0.0.1', 32800)
# Получено: Привет!
# Обработка данных...
# Данные обработаны, отправка клиенту...
# Получено: 
# Нет данных от: ('127.0.0.1', 32800)
# Ожидание соединения...