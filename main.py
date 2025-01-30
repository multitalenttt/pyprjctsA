class TLogElement:
    """Базовый класс для логического элемента."""
    def __init__(self):
        self.__in1 = 0
        self.__in2 = 0
        self._res = 0
        if hasattr(self, "_calc"):
            pass
        else:
            raise NotImplementedError("Нелья создать такой объект!!!")

    def __setIn1(self, newIn1):
        if newIn1 in (0,1):
            self.__in1 = newIn1
            self._calc()

    def __setIn2(self, newIn2):
        if newIn2 in (0,1):
            self.__in2 = newIn2
            self._calc()

    In1 = property(lambda x: x.__in1, __setIn1)
    In2 = property(lambda x: x.__in2, __setIn2)
    Res = property(lambda x: x._res)


class TNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(not(self.In1))


class TAnd(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = self.In1 * self.In2

class TE(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(self.In1 == self.In2)

class TOr(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = self.In1 + self.In2
        if self._res == 2:
            self._res = 1

class TNAnd(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(not(self.In1 * self.In2))


class TNOr(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = self.In1 + self.In2
        if self._res == 2:
            self._res = 1
        self._res = int(not(self._res))

class TXor(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(self.In1 != self.In2)

class TImp(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)

    def _calc(self):
        self._res = int(self.In1 <= self.In2)