import asyncio



async def handle_echo(reader, writer):
    while True:
        data = await reader.read(128)
        if data:
            writer.write(data.decode().upper().encode())
            await writer.drain()
        else:
            writer.close()
            return


def main():
    HOST, PORT = "localhost", 8080
    event_loop = asyncio.get_event_loop()
    factory = asyncio.start_server(handle_echo, HOST, PORT)
    server = event_loop.run_until_complete(factory)
    try:
        event_loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        event_loop.run_until_complete(server.wait_closed())
        event_loop.close()

main()