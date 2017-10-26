import hashlib

class Block(object):

    def __init__(self, PreviousHash, Transactions):
        self.PreviousHash = PreviousHash # initialization of the parameters
        self.Transactions = Transactions

        contents = [hashlib.md5(Transactions.encode('utf-8')).hexdigest(), PreviousHash]
        newcontents = ",".join(str(v) for v in contents )
        #print(newcontents)
        self.blockHash = hashlib.md5(newcontents.encode('utf-8')).hexdigest()

    def getPreviousHash():
        return PreviousHash

    def getTransaction():
        return Transactions
    
