def checkBlockValidity(block,parent,state):
    # We want to check the following conditions:
    # - Each of the transactions are valid updates to the system state
    # - Block hash is valid for the block contents
    # - Block number increments the parent block number by 1
    # - Accurately references the parent block's hash
    parentNumber = parent[u'contents'][u'blockNumber']
    parentHash = parent[u'hash']
    blockNumber = block[u'contents'][u'blockNumber']

    # Check transaction validity; throw an error if an invalid transaction was found.
    for txn in block[u'contents'][u'txns']:
        if isValidTxn(txn,state):
            state = updateState(txn,state)
        else:
            raise Exception('Invalid Transaction in block %s: %s'%(blockNumber,txn))

    checkBlockHash(block)

    if blockNumber != (parentNumber+1):
        raise Exception('Invalid Block number in block %s'%blockNumber)

    if block[u'contents']['parentHash'] != parentHash:
        raise Exception('ParentHash not accurate at block %s'%blockNumber)

    return state

def checkChain(chain):
    # Work through the chain from the genesis block (which gets special treatment),
    # checking that all transactions are internally valid,
    # that the transactions do not cause an overdraft,
    # and that the blocks are linked by their hashes.
    # This returns the state as a dictionary of accounts and balances,
    # or returns False if an error was detected


    ## Data input processing: Make sure that our chain is a list of dicts
    if type(chain)==str:
        try:
            chain = json.loads(chain)
            assert( type(chain)==list)
        except:  # This is a catch-all, admittedly crude
            return False
    elif type(chain)!=list:
        return False

    state = {}
    ## Prime the pump by checking the genesis block
    # We want to check the following conditions:
    # - Each of the transactions are valid updates to the system state
    # - Block hash is valid for the block contents

    for txn in chain[0]['contents']['txns']:
        state = updateState(txn,state)
    checkBlockHash(chain[0])
    parent = chain[0]

    ## Checking subsequent blocks: These additionally need to check
    #    - the reference to the parent block's hash
    #    - the validity of the block number
    for block in chain[1:]:
        state = checkBlockValidity(block,parent,state)
        parent = block

    return state

def checkBlockHash(block):
    #Raises an exception if hash does not match block contents

    expectedHash = hashMe(block[u'contents'])
    if block[u'hash'] != expectedHash:
        raise Exception ('Hash does not match contents of block %s'%block[u'contents'][u'blockNumber'])
    return
