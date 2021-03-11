# pylint: disable=missing-module-docstring

import os

from xdecha import xdecha


async def _worker() -> None:
    chat_id = int(os.environ.get("CHAT_ID") or 0)
    type_ = 'unofficial' if os.path.exists("../xdecha/plugins/unofficial") else 'main'
    await xdecha.send_message(chat_id, f'`{type_} build completed !`')

if __name__ == "__main__":
    xdecha.begin(_worker())
    print('xdecha test has been finished!')
