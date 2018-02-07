




def createGenesis():

    state = {u'Alice':50,u'Bob':50}
    genesisBlockTxns = [state]
    genesisBlockContents = {u'blockNumber':0, u'parentHash':None, u'txnCount':1, u'txns':genesisBlockTxns}
    genesisHash = hashMe( genesisBlockContents )
    genesisBlock = {u'hash': genesisHash, u'contents': genesisBlockContents}
    genesisBlockStr = json.dumps(genesisBlock,sort_keys=True)
    return genesisBlock
