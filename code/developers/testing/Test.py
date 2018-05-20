class Test:
    """
    Base class of Test. Override the method _test() and use the run()-method to start the Test.
    """

    def __init__(self, name="unnamed Test"):
        self.assertions=0
        self.errors = []
        self.fails = []
        self.name = name

    def run(self):
        """ final
        The method to start the Test
        """
        self.__onStart()
        self._test()
        self.__onEnd()

    def __onStart(self):
        print("running Test '"+self.name+"':")

    def __onEnd(self):
        print("finished Test '"+self.name+"' with "
              +str(self.assertions)+" assertions, "
              +str(len(self.fails))+" fails and "
              +str(len(self.errors))+" errors"
              )

    def _test(self):
        """ protected
        Override this and ONLY this method in your Tests
        """
        pass

    def __onAssertion(self):
        self.assertions += 1

    def __onFail(self, comment):
        self.fails.append("FAIL: "+comment)

    def __onError(self, comment):
        self.errors.append("ERROR: "+comment)

    def __onSuccess(self, comment):
        output = "SUCCESS: "+comment
        pass

    def assertValue(self, value1, value2, comment=None, funcName="assertValue"):
        self.__onAssertion()
        comment = self.__createComment(value1, value2, funcName, comment)
        try:
            if value1 != value2:
                self.__onFail(comment)
            else:
                self.__onSuccess(comment)
        except RuntimeError:
            self.__onError(comment)

    def __createComment(self, value1, value2, funcName, comment=None):
        if comment is None:
            return funcName+"("+str(value1)+", "+str(value2)+")"
        return comment

    def assertBool(self, value, boolValue, comment=None, funcName="assertBool"):
        comment = self.__createComment(value, 0, funcName, comment)
        if type(boolValue) is bool:
            self.assertValue(value, boolValue, comment, funcName)
        else:
            self.__onAssertion()
            self.__onError(comment)

    def assertInt(self, value, intValue, comment=None, funcName="assertInt"):
        comment = self.__createComment(value, intValue, funcName, comment)
        if type(intValue) is int:
            self.assertValue(value, intValue, comment, funcName)
        else:
            self.__onAssertion()
            self.__onError(self.__createComment(value, intValue, funcName))
    def assertZero(self, value, comment=None):
        funcName = "assertZero"
        comment = self.__createComment(value, 0, funcName, comment)
        self.__onAssertion()
        if type(value) is (int, float):
            if value == 0:
                self.__onSuccess(comment)
                pass
        self.__onError(comment)

    def assertTrue(self, value, comment=None):
        self.assertBool(value, True, comment, "assertTrue")

    def assertFalse(self, value, comment=None):
        self.assertBool(value, False, comment, "assertFalse")

    def assertFloat(self, value, floatValue, comment=None, funcName="assertFloat"):
        comment = self.__createComment(value, 0, funcName, comment)
        if type(floatValue) is float:
            self.assertValue(value, floatValue, comment, funcName)
        else:
            self.__onAssertion()
            self.__onError(comment)

    def assertString(self, value, stringValue, comment=None, funcName="assertString"):
        """
        Tests if the given value is a string and if both strings are equal.
        :param value: The value to test
        :param stringValue: The string to test equality
        :param comment: Default=None; Comment for debugging. Will be shown as output on fail
        :param funcName: Default=function_name; Name of the function for debugging. Part of the default comment
        """
        comment = self.__createComment(value, 0, funcName, comment)
        if type(stringValue) is str:
            self.assertValue(value, stringValue, comment, funcName)
        else:
            self.__onAssertion()
            self.__onError(comment)
