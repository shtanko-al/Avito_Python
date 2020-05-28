""""
TCP сервер, асинхронный
"""
import asyncio
import datetime


class EchoServerClientProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        if message == 'stop':
            self.transport.close()
        elif message == 'calendar':
            date = datetime.datetime.now()
            date_f = date.strftime("%d-%m-%Y %H:%M")
            # print(date_f)
            # print(type(date_f))
            self.transport.write(date_f.encode())
        elif message[0:4] == 'echo':
            mes = message[5:]
            self.transport.write(mes.encode())
        else:
            mes = 'доступные комманды:\
                * echo `<message>` – возвращает <message>\
                * calendar – возвращает клиенту текущее время в формате dd.mm.YYYY HH:MM\
                * stop – закрывает сервер\
                * любая другая команда – вывод сообщения о доступных командах\
                '
            self.transport.write(mes.encode())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Each client connection will create a new protocol instance
    coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 10001)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print('сервер должен работать')

    # Close the server
    # server.close()
    # loop.run_until_complete(server.wait_closed())
    # loop.close()
