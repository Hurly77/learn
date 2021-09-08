blockchain = []


def get_las_in_chain():
    return blockchain[-1]


def add_value(trans_amount, las_trans=[0]):
    blockchain.append([las_trans, float(trans_amount)])
    print(blockchain)


def get_user_input():
    return input("Your transation amount please or else I'll have to .... to....: ")


tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(tx_amount)
