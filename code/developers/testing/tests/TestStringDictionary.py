import os

import pathes
from code.core.strings.StringDictionary import StringDictionary
from code.developers.testing.Test import Test


class TestStringDictionary(Test):
    def __init__(self, name="unnamed Test"):
        Test.__init__(self, name)

    def _test(self):
        language ="test_test"
        StringDictionary.saveAllFilesForLanguage(language)
        path = os.path.join(pathes.DIR_RESOURCES_STRINGS, language)
        self.assertTrue(os.path.exists(path))
        for i in range(0,3):
            filePath  = os.path.join(path, StringDictionary._FILE[i])
            self.assertTrue(os.path.exists(filePath))

