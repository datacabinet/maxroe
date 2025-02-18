from ._version import __version__
from .handlers import setup_handlers
import logging
logger = logging.getLogger(__name__)

def _jupyter_labextension_paths():
    return [{
        "src": "labextension",
        "dest": "maxroe"
    }]


# my_jupyter_extension/__init__.py
def _jupyter_server_extension_paths():
    return [{
        "module": "maxroe"
    }]
def _jupyter_server_extension_points():
    return [{
        "module": "maxroe",
    }]

def load_jupyter_server_extension(nbapp):
    logger.info("My Jupyter server extension is loaded!")
    setup_handlers(nbapp)
