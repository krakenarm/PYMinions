from code.core.strings.StringDictionary import StringDictionary


class WStrings(StringDictionary):
    WORLD = "world"
    BUILDING = "building"
    BUILDINGS = "buildings"
    ROOM = "room"
    ROOMS = "rooms"
    ENTITY = "entity"
    ENTITIES = "entities"

    ##
    #   @see StringDictionary.setLanguage
    @classmethod
    def setLanguage(cls, locale=StringDictionary._LANG_DEFAULT, dictType=None):
        super().setLanguage(locale, StringDictionary._TYPE_WORLD_STRINGS)