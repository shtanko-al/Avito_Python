import asyncio
import random
import time


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 10001)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()


async def asynchronous():
    tasks = [asyncio.ensure_future(task_coro()) for _ in range(20)]
    await asyncio.wait(tasks)


async def task_coro():
    """Coroutine non-deterministic task"""
    mes = message[random.randint(1, 4)]
    time.sleep(random.random())
    await tcp_echo_client(mes)
    # print('Task %s done' % pid)


message = {1: 'Hello World!',
           2: 'echo abracadabra',
           3: 'calendar',
           4: 'stop'}

if __name__ == '__main__':
    client_loop = asyncio.get_event_loop()
    client_loop.run_until_complete(asynchronous())
    client_loop.close()
