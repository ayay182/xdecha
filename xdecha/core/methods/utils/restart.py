# pylint: disable=missing-module-docstring

__all__ = ['Restart']

import os
import sys

import psutil

from xdecha import logging
from ...ext import RawClient

_LOG = logging.getLogger(__name__)
_LOG_STR = "<<<!  #####  %s  #####  !>>>"


class Restart(RawClient):  # pylint: disable=missing-class-docstring
    async def restart(self, update_req: bool = False) -> None:  # pylint: disable=arguments-differ
        """ Restart the Abstractxdecha """
        _LOG.info(_LOG_STR, "Restarting xdecha")
        await self.stop()
        try:
            c_p = psutil.Process(os.getpid())
            for handler in c_p.open_files() + c_p.connections():
                os.close(handler.fd)
        except Exception as c_e:  # pylint: disable=broad-except
            print(_LOG_STR % c_e)
        if update_req:
            print(_LOG_STR % "Installing Requirements...")
            os.system(  # nosec
                "pip3 install -U pip && pip3 install --no-cache-dir -r requirements.txt")
        os.execl(sys.executable, sys.executable, '-m', 'xdecha')  # nosec
        sys.exit()
