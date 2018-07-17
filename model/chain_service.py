from model.block import Block, BlockHeader, BlockBody


class ChainService(object):
    def __init__(self):
        self.block_chain = []
        self.current_transactions = []
        self.__create_genesis_block()

    @property
    def last_block(self):
        return self.block_chain[-1]

    def new_block(self, proof, previous_hash=None):
        block = Block(
            BlockHeader(
                index=len(self.block_chain) + 1,
                proof=proof,
                previous_hash=previous_hash or self.last_block.hash_block()
            ),
            BlockBody(transactions=self.current_transactions)
        )
        self.block_chain.append(block)
        self.current_transactions = []
        return block

    def new_transaction(self, sender=None, recipient=None, amount=None):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block.block_header.index + 1

    def __create_genesis_block(self):
        self.new_block(previous_hash=1, proof=100)