blockchain = []


def get_las_in_chain():
    return blockchain[-1]


def add_value(trans_amount, las_trans=[0]):
    blockchain.append([las_trans, float(trans_amount)])
    print(blockchain)


def get_user_input():
    return input("Your transaction amount: ")


tx_amount = get_user_input()
add_value(tx_amount)

isTrue = True

while isTrue:
    tx_amount = get_user_input()
    add_value(tx_amount)

    for block in blockchain:
        print("Out putting Block")
        print(block)
    isTrue = False

print("Done!")
