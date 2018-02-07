blockSizeLimit = 5 # Arbitrary number of transactions per block-
                  # this is chosen by the block miner, and can vary between blocks!

while len(txnBuffer) > 0:
    bufferStartSize= len(txnBuffer)

    ## Gather a set of valid transactions for inclusion
    txnList = []
    while (len(txnBuffer) > 0 and len(txnList) < blockSizeLimit):
        newTxn = txnBuffer.pop()
        validTxn = isValidTxn(newTxn,state) #returns false is transaction is invalid

        if validTxn:
            txnList.append(newTxn)
            state = updateState(newTxn,state)
        else:
            print("ignored Transaction")
            sys.stdout.flush()
            continue  # This was an invalid transaction; ignore it and move on

    # Make the Block
    myBlock = makeBlock(txnList,chain)
    chain.append(myBlock)
