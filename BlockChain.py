import hashlib
from Block import Block



Fisrt_Block = Block(0 , "first transaction")


def gethash(words):
    return hashlib.md5(words.encode('utf-8')).hexdigest()



Fisrt_Block = Block(0 , "first transaction")

ledger = []
ledger.append(Fisrt_Block.blockHash)
Block2 = Block(Fisrt_Block.blockHash, "2 transaction")
ledger.append(Block2.blockHash)

Block3= Block(Block2.blockHash, "3 transaction")
ledger.append(Block3.blockHash)

Block4 = Block(Block3.blockHash, "4 transaction")
ledger.append(Block4.blockHash)

Block5 = Block(Block4.blockHash, "5 transaction")
ledger.append(Block5.blockHash)

Block6 = Block(Block5.blockHash, "6 transaction")
ledger.append(Block6.blockHash)

Block7 = Block(Block6.blockHash, "7 transaction")
ledger.append(Block7.blockHash)

Block8 = Block(Block7.blockHash, "8 transaction")
ledger.append(Block8.blockHash)

Block9 = Block(Block8.blockHash, "9 transaction")
ledger.append(Block9.blockHash)

Block10 = Block(Block9.blockHash, "10 transaction")
ledger.append(Block10.blockHash)

Block11 = Block(Block10.blockHash, "11 transaction")
ledger.append(Block11.blockHash)

Block12 = Block(Block11.blockHash, "12 transaction")
ledger.append(Block12.blockHash)

Block13 = Block(Block12.blockHash, "13 transaction")
ledger.append(Block13.blockHash)



for n in ledger:
    print(n)


