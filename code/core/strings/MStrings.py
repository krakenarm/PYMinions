from code.core.strings.StringDictionary import StringDictionary


class MStrings(StringDictionary):
    MINION = "minion"
    MINIONS = "minions"
    FEELING = "feeling"
    FEELINGS = "feelings"


    ##
    #   @see StringDictionary.setLanguage
    @classmethod
    def setLanguage(cls, locale=StringDictionary._LANG_DEFAULT, dictType=None):
        super().setLanguage(locale, StringDictionary._TYPE_MINION_STRINGS)