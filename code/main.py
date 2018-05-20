
from code.developers.testing.tests.TestStringDictionary import TestStringDictionary


def runTests():
    print("#### STARTING ####")
    print("++++ TESTING  ++++")

    allTests = []
    allTests.append(TestStringDictionary("StringDictionary"))

    for test in allTests:
        test.run()


    print("++++ TEST END ++++")
    print("####  ENDING  ####")

runTests()