from chap_2_saver.model import TFModel
from chap_2_saver.view import TFView
class TFController:

    def __init__(self):
        self._m = TFModel()
        self._v = TFView()

    def calc(self, num1,num2) -> float:
        m = self._m
        m.num1 = num1
        m.num2 = num2
        return m.exec()
