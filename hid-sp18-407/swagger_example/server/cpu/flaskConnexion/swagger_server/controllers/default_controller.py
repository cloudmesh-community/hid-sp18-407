import connexion
import six

import os, platform, subprocess, re

from swagger_server.models.cpu import Cpu  # noqa: E501
from swagger_server import util

import os, platform, subprocess, re

def get_processor_name():
	if platform.system() == "Windows":
		return platform.processor

	elif platform.system() == "Darwin":
		command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
		return subprocess.check_output(command, shell=True).strip()
	
	elif platform.system() == "Linux":
		command = "cat /proc/cpuinfo"
		all_info = subprocess.check_output(command, shell=True).strip()
		for line in all_info.split("\n"):
			if "model name" in line:
				return re.sub(".*model name.*",  "", line, 1)
	
	return "cannot find cpu info"




def cpu_get():  # noqa: E501
    """cpu_get

    Returns cpu information # noqa: E501


    :rtype: Cpu
    """
    return CPU(get_processor_name())



