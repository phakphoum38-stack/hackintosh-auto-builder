import platform
import subprocess

def scan_hardware():

    cpu = platform.processor()

    try:
        gpu = subprocess.getoutput(
            "wmic path win32_VideoController get name"
        )
    except:
        gpu = "Unknown GPU"

    return {
        "cpu": cpu,
        "gpu": gpu
    }
