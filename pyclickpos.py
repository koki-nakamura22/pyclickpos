# -*- coding: utf-8 -*-

import asyncio
import mouse


def print_click_pos() -> None:
    x, y = mouse.get_position()
    print(f"x: {x}, y:{y}")


def main() -> None:
    print("Press Ctrl + C to quit.")

    mouse.on_click(print_click_pos)

    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


if __name__ == '__main__':
    main()
