
_LEVEL_INFO = 1
_LEVEL_DEBUG = 2
_LEVEL_ERROR = 3


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def printLog(level: int, tag: str, msg: str):
    tag = f"[{tag.center(12)}]"
    if level == _LEVEL_DEBUG:
        tag = bcolors.OKGREEN + tag + bcolors.ENDC
    elif level == _LEVEL_INFO:
        tag = bcolors.OKBLUE + tag + bcolors.ENDC
    elif level == _LEVEL_ERROR:
        tag = bcolors.WARNING + tag + bcolors.ENDC
    print(tag + " " + msg)


class Log:

    @staticmethod
    def d(tag: str, msg: str):
        printLog(_LEVEL_DEBUG, tag, msg)

    @staticmethod
    def e(tag: str, msg: str):
        printLog(_LEVEL_ERROR, tag, msg)

    @staticmethod
    def i(tag: str, msg: str):
        printLog(_LEVEL_INFO, tag, msg)
