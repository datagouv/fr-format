import io
import urllib.request


class RemoteReader:
    def read_file(self, path: str) -> io.StringIO | io.TextIOWrapper:
        try:
            response: urllib.request._UrlopenRet = urllib.request.urlopen(path)
            csvfile: io.StringIO = io.StringIO(response.read().decode("utf-8"))
            return csvfile
        except Exception as e:
            raise Exception(f"An error is occured: {e}")


class LocalReader:
    def read_file(self, path: str) -> io.StringIO | io.TextIOWrapper:
        try:
            csvfile: io.TextIOWrapper = open(path, newline="", encoding="utf-8")
            return csvfile
        except Exception as e:
            raise Exception(f"An error is occured: {e}")
