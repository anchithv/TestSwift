#-------------------------------------------------
# Import sys module for setting run arguments
#-------------------------------------------------

import sys
import os

#Default LIB path
LIB_PATH = '/appl/ebiconfig/generic/TestGeneratorFramework/TestGeneratorFramework-1.1/TestGeneratorFramework/distribution/lib/'


# Arguments for TGF ( !IMPORTANT )
sys.argv = sys.argv + ["-i", "Interlocking_data", "-c", "Command_table"]
print("This file is running with argument(s) : %s" % sys.argv)


print("Path for TGF")
print("Default: %s\n" % LIB_PATH)
print("Please select TGF path\nDefault select 1 , Relative local select 2, Custom select 3")
while(True):
	userInput = input("Select : ")
	if userInput == "3":
		print("\nuse custom path")
		print("must use ABSOLUTE path")
		LIB_PATH = input("enter path : ")
		sys.path.append(LIB_PATH)
		os.environ['TGF_HOME'] = LIB_PATH
		print("custom path added\n")
		break
	elif userInput == "2":
		print("use relative local path")
		LIB_PATH = os.path.join(os.path.dirname(__file__), 'TestGeneratorFramework\\distribution\\lib')
		sys.path.append(LIB_PATH)
		os.environ['TGF_HOME'] = LIB_PATH
		break
	elif userInput == "1":
		print("use default path")
		sys.path.append(LIB_PATH)
		os.environ['TGF_HOME'] = LIB_PATH
		print("\n")
		break
	else:
		print("Typing error please try again")
		print("Please select TGF path\nDefault select 1 , Custom select 2")
		continue
print('Selected path: {}'.format(LIB_PATH))
#-------------------------------------------------
# Import TGF main framework
#-------------------------------------------------
try:
	import TestGeneratorFramework.distribution.lib.Tgf as tgf
except:
	try:
		import Tgf as tgf
	except:
		print("Error cannot import TGF.\nPlease check path\n")