from code.core.strings.StringDictionary import StringDictionary


class GStrings(StringDictionary):
    OK = "ok"
    OKAY = "okay"
    CANCEL = "cancel"

    ##
    #   @see StringDictionary.setLanguage
    @classmethod
    def setLanguage(cls, locale=StringDictionary._LANG_DEFAULT, dictType=None):
        super().setLanguage(locale, StringDictionary._TYPE_GENERAL_STRINGS)