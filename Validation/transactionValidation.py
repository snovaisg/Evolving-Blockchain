def isValidTxn(txn,state):
    # Assume that the transaction is a dictionary keyed by account names

    #check the the sum of the repositories is 0
    if sum(txn.values()) is not 0:
        return False

    #Check that the transaction does not causa an overdraft
    for key in txn.keys():
        if key in state.keys():
            accBalance = state[key]
        else:
            accBalance = 0
        if (accBalance + txn[key]) < 0:
            return False

    return True
