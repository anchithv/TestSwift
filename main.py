#-------------------------------------------------
# Import init
#-------------------------------------------------

from TGF_init import tgf

#-------------------------------------------------
# Custom code
#-------------------------------------------------

tgf.TestStorage.tempStorageClear()

testSuiteName="CBI-XX-TEST_SET_ROUTE"
testCaseName=""

cbiArea = tgf.TestEnvironment.getCBIArea()

# Create file and write file header
tgf.TestWriter.createXMLFile("CBI-05-2001.xml")
tgf.TestWriter.writeFileHeader()

# Define function tag and testsuite tag of XML
tgf.TestWriter.writeFunctionHeader("SET_ROUTE")
tgf.TestWriter.writeTestsuiteHeader(testSuiteName)

direction = "01"
repeatAction = "0"
action = "1"

testCaseId = "{}_{}_00{}_0{}".format(testSuiteName, direction, action, repeatAction)

tgf.TestWriter.writeTestcaseHeader(testCaseId, testCaseName)

testId = "{}".format(testCaseId)

tgf.TestStorage.setId(testId)
tgf.TestStorage.setComment("This TC is TESTING for Set Route command")

# SetupEvents
tgf.TestStorage.addSetupEvent(event='ilsCheckpointRead\t1\tRSA_R3_RATP')
tgf.TestStorage.addSetupEvent(event='execGo\t1')

# TestEvents
target = 'LTSUN570T LTSUN558T'
dict_keys = tgf.tf.getRefToDataStorage().dictComponents.keys()
set_route_command = [key for key in dict_keys if target in key]

if len(set_route_command)==0:
	print('There is no command TR {}'.format(target))
	tgf.sys.exit(0)

set_route_command = set_route_command[0]

tgf.TestStorage.addTestEvent(event='cosCmdFspu\t{}\t{}'.format(cbiArea, set_route_command))

# ExpectedResults
for trackName in sorted(tgf.InterlockingData.getLogicalNamesofType('LTRACK')):
	if trackName in target.split():
		tgf.TestStorage.addResult("illGet\t{}\t{}\t{}".format(cbiArea, trackName, 'DUMMY_DICT'))

tgf.TestWriter.writeSubtestObj()
tgf.TestWriter.writeTestcaseFooter()
tgf.TestWriter.writeTestsuiteFooter()
tgf.TestWriter.writeFunctionFooter()

tgf.TestWriter.writeFileFooter()
tgf.TestWriter.closeXMLFile()

#--------------------------------------------------------