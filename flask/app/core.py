import configparser
import logging
import os
from typing import Tuple, List

from werkzeug.local import LocalProxy
from flask import current_app, jsonify
from flask.wrappers import Response

# logger object for all views to use
logger = LocalProxy(lambda: current_app.logger)
core_logger = logging.getLogger("core")

def create_response(
    data: dict = None, status: int = 200, message: str = ""
) -> Tuple[Response, int]:

    if type(data) is not dict and data is not None:
        raise TypeError("Data should be a dictionary")
    
    data["message"] = message
    response = {"success": 200 <= status < 300, "result": data}
    return jsonify(response), status


def serialize_list(items: List) -> List:
    """Serializes a list of SQLAlchemy Objects, exposing their attributes.
    
    :param items - List of Objects that inherit from Mixin
    :returns List of dictionaries
    """
    if not items or items is None:
        return []
    return [x.to_dict() for x in items]

def all_exception_handler(error: Exception) -> Tuple[Response, int]:
    """Catches and handles all exceptions, add more specific error Handlers.
    :param Exception
    :returns Tuple of a Flask Response and int
    """
    return create_response(message=str(error), status=500)

