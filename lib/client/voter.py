
#this is the voting modual. 
#all local calls to multichain will be done here
#and called from the votepage. simple enough.

from jsonrpc import ServiceProxy

class chaincommands():
	def getNewWallet(rpc):
		client = ServiceProxy(rpc)
		newWallet = client.getnewaddress()
		return newWallet
	
	def getVotesFromWallet(rpc,addr): #dont need good for testing
		client = ServiceProxy(rpc)
		transcArray = client.getaddressbalances(addr)
		return transcArray[0]["qty"]
	
	def	issuecoin():
		client = ServiceProxy(rpc)
		isucoin = client.issue address name|params qty (units=1) (native-amount=0) ({"custom-field-1":"x",...})
		return isucoin
	
	def connectchain():
		client = ServiceProxy(rpc)
		cnxtchain = client.multichaind test@172.31.21.118:2777 -daemon
		return cnxtchain
		
	def send():	
		client=sendassettoaddress(rpc)
		sendtoadd=client.address asset qty
		(native-amount=min-per-output)
		(comment='') (comment-to='')
		
		

"""
test@172.31.21.118:2777 -daemon

import argparse
import chain
parser = argparse.ArgumentParser()
connstr = "http://jenn:password@127.0.0.1:2776"
su (enter root password)

cd /tmp
wget http://www.multichain.com/download/multichain-1.0-alpha-19.tar.gz
tar -xvzf multichain-1.0-alpha-19.tar.gz
cd multichain-1.0-alpha-19
mv multichaind multichain-cli multichain-util /usr/local/bin (to make easily accessible on the command line)

exit (to return to your regular user)

genisis node: 
 test@172.31.21.118:2777

to use in command line: mv multichaind multichain-cli multichain-util /usr/local/bin
"""