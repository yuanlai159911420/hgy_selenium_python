import configparser


class ReadIni(object):
    def __init__(self, ini_path, node):
        self.__ini_path = ini_path
        self.__node = node
        self.__cg = self.load_ini()

    def load_ini(self):
        cg = configparser.ConfigParser()
        """读取文件"""
        cg.read(self.__ini_path)
        return cg

    def get_data(self, key):
        return self.__cg.get(self.__node, key)
