import connexion
import six
import wordCountApp

from swagger_server.models.cpu import CPU  # noqa: E501
from swagger_server import util


def count_get():  # noqa: E501
    """count_get

    Returns word count information: # noqa: E501


    :rtype: Words
    """
    return CPU(get_processor_name()
