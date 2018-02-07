import hashlib, json, sys
import random
random.seed(0)

def makeTransaction(maxValue=3):
    #This will create valid transactions between (1,maxValue)

    sign = int(random.getrandbits(1))*2-1
    #This will randomly choose -1 or 1

    amount = random.randint(1,maxValue)
    alicePays = sign * amount
    bobPays = -1 * alicePays

    return {u'Alice':alicePays,u'Bob':bobPays}-8')).hexdigest()
