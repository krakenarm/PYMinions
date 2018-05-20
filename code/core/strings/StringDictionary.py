
import json
import os


import pathes
class StringDictionary:
    _LANG_DEFAULT = ""
    _LANG_DE_DE = "de_de"
    _TYPE_GENERAL_STRINGS = 0
    _TYPE_WORLD_STRINGS = 1
    _TYPE_MINION_STRINGS = 2

    _FILE = ['generalstrings.json', 'worldstrings.json', 'minionstrings.json']

    ##
    # Used to initialise a StringDictionary with a language from a json file.
    # @param locale the language string. It can be chosen from StringDictionary._LANG_****.
    # @param dictType Type of the StringDictionary.
    @classmethod
    def setLanguage(cls, locale=_LANG_DEFAULT, dictType=_TYPE_GENERAL_STRINGS):
        path = pathes.DIR_RESOURCES_STRINGS
        if locale != StringDictionary._LANG_DEFAULT:
            path = os.path.join(path, locale)
        path = os.path.join(path, StringDictionary._FILE[dictType])
        if os.path.exists(path):
            data = json.load(open(path))
            for key in data:
                value= data[key]
                setattr(cls, key,value
                        )

    ##
    #   Saves StringDictionary or one of its child classes to a given file. The output should
    #   be a .json file but any ascii-file can be used. Output will be saved in sorted order (a>b)
    #   and only saves the class attributes the class ownes at savetime.
    #   @param filePath The full filepath e.g. "C:/temp/test_output.json"
    @classmethod
    def saveAsJSON(cls, filePath=os.path.join(pathes.DIR_RESOURCES,"dev_stringOutput.json")):
        output = {}
        for att in cls.__dict__:
            if att[:1] != "_":
                value = cls.__dict__.get(att)
                if isinstance(value, (str, int, float)):
                    output[att] = value
        with open(filePath, "w") as f:
            json.dump(output, f, indent=2, sort_keys=True)

    @classmethod
    def saveAllFilesForLanguage(cls, language="xx_xx"):
        """
        Saves a copy of all StringDictionarys like GStrings, MStrings and WStrings in a subfolder for editing.
        :param language: the subfolder where the strings are saved e.g. de_de. default is xx_xx
        """
        path = os.path.join(pathes.DIR_RESOURCES_STRINGS, language)
        if not os.path.exists(path):
            os.mkdir(path)
        # saving GStrings
        filePath = os.path.join(path, StringDictionary._FILE[StringDictionary._TYPE_GENERAL_STRINGS])
        from code.core.strings.GStrings import GStrings
        GStrings.saveAsJSON(filePath)
        # saving MStrings
        filePath = os.path.join(path, StringDictionary._FILE[StringDictionary._TYPE_MINION_STRINGS])
        from code.core.strings.MStrings import MStrings
        MStrings.saveAsJSON(filePath)
        # saving WStrings
        filePath = os.path.join(path, StringDictionary._FILE[StringDictionary._TYPE_WORLD_STRINGS])
        from code.core.strings.WStrings import WStrings
        WStrings.saveAsJSON(filePath)
