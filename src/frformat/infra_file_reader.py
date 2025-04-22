import io
import urllib.request


class RemoteReader:
    def read_file(self, path: str) -> io.TextIOBase:
        response: urllib.request._UrlopenRet = urllib.request.urlopen(path)
        csvfile = io.StringIO(response.read().decode("utf-8"))
        return csvfile


class LocalReader:
    def read_file(self, path: str) -> io.TextIOBase:
        csvfile = open(path, newline="", encoding="utf-8")
        return csvfile
