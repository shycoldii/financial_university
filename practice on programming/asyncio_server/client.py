import asyncio


async def tcp_echo_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    await writer.drain()
    while True:
        msg = input("Message:")
        if msg.lower() != 'exit' and msg != "":
            writer.write(msg.encode())
            await writer.drain()
            data = await reader.read(128)
            print(data.decode())
            if not data:
                writer.close()
                return
        else:
            writer.close()
            return


HOST, PORT = "localhost", 8080

loop = asyncio.get_event_loop()
task = loop.create_task(tcp_echo_client(HOST, PORT))
loop.run_until_complete(task)
