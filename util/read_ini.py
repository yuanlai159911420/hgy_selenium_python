import configparser


class ReadIni(object):
    def __init__(self, ini_path, node):
        self.ini_path = ini_path
        self.node = node
        self.cg = self.load_ini()

    def load_ini(self):
        cg = configparser.ConfigParser()
        """读取文件"""
        cg.read(self.ini_path)
        return cg

    def get_data(self, key):
        return self.cg.get(self.node, key)
