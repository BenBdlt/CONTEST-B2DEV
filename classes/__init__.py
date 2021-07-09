import hashlib
import json
from time import time

class BlockChain(object):
    def __init__(self):
        self.current_transactions = []
        self.chain = []

        # Create the genesis block
        self.new_block(previous_hash='1')

    def new_block(self, previous_hash):

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block
    
    def new_transaction(self, sender, recipient, amount):

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

class Block():
    def __init__(self, index, transactions, data, parent_hash):
        self.index = index
        self.timestamp = transactions
        self.data = data
        self.previous_hash = parent_hash
        self.hash = self.hashing()
    
    def check_hash(self):
        key = hashlib.sha256()
        key.update(str(self.index).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.previous_hash).encode('utf-8'))
        return key.hexdigest()

    def add_transaction():
        pass

    def get_transaction():
        pass

    def get_weight(self):
        return len(self.blocks)-1

    def save():
        pass

    def load():
        pass

class Chain():
    def __init__(self):
        self.blocks = [self.get_genesis_block()]
    
    def generate_hash(self): 
        return Block(0, time.datetime.utcnow(), 'Genesis', 'arbitrary')

    def verify_hash(self, verbose=True): 
        verif = True
        for i in range(1,len(self.blocks)):
            if self.blocks[i].index != i:
                verif = False
                if verbose:
                    print(f'Wrong block index{i}.')
            if self.blocks[i-1].hash != self.blocks[i].previous_hash:
                verif = False
                if verbose:
                    print(f'Wrong previous hash{i}.')
            if self.blocks[i].hash != self.blocks[i].hashing():
                verif = False
                if verbose:
                    print(f'Wrong hash {i}.')
        return verif
    
    def add_block(self, data):
        self.blocks.append(Block(len(self.blocks), time.datetime.utcnow(), data, self.blocks[len(self.blocks)-1].hash))
    
    def get_block():
        pass

    def add_transaction():
        pass
    
class Wallet():
    def __init__(self, index, balance, history):
        self.index = index
        self.balance = balance
        self.history = history
        history = []

    def add_balance(count, balance):
        balance = balance + count

    def sub_balance(count, balance):
        
        balance = balance - count

    def send(history, count, index):
        history.append(count, index, time.datetime.utcnow())
