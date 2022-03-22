from os.path import expanduser

#get home directory path and define important paths
#TODO: add support for providing them via runtime parameters
home = expanduser("~")
databasePath = home + "/.chia/mainnet/db/blockchain_v1_mainnet.sqlite"
logPath = home +  "/.chia/mainnet/log/debug.log"
logFile = open(logPath, "r")

#search log for info about malformed db
for line in logFile:
    if("full_node" in line and "database disk image is malformed" in line):
        
      #db is malformed, replace it with backup
      break 