# pylint: disable=missing-module-docstring

from xdecha.logger import logging  # noqa
from xdecha.config import Config, get_version  # noqa
from xdecha.core import (  # noqa
    xdecha, filters, Message, get_collection, pool)

xdecha = xdecha()  # xdecha is the client name
