# -*- coding: utf-8 -*-
# @Time    : 2023-1-30 14:34
# @Author  : yiming


import requests
import sys

class putImg:

    def __init__(self) -> None:

        self.help = '''
        python main.py "c:/1.jpg"    : Upload file c:/1.jpg
        '''
        self.picUrl = "https://api.wer.plus/api/58map"

    def _getCliValue(self) -> bool:
        '''
        Whether to specify a file
        '''
        return False if len(sys.argv) == 1 else True

    def upload(self) -> str:
        '''
        Upload file
        '''
        if self._getCliValue() and self._readFile():
            if self.tload():
                return f"""
    Uploading [{sys.argv[1]}] succeeded
    URL : {self.fileToUrl}
    """
            else:
                return """
                Unable to upload
                """
        else:
            return self.help

    def tload(self) -> bool:
        try:
            req = requests.post(
                self.picUrl,
                files = {
                    "file":self.file
                }
            )
            self.data = req.json()
            self.fileToUrl = self.data["url"]
            self.file.close()
            return True
        except:
            return False

    def _readFile(self) -> bool:
        try:
            self.file = open(sys.argv[1],"rb")
            return True
        except:
            return False

if __name__ == "__main__":
    print(putImg().upload())
