name = "brain"
age = 10


def is_num(input):
    try:
        int(input)
        it_is = True
    except ValueError:
        it_is = False
    return it_is


def is_str(input):
    try:
        str(input)
        it_is = True
    except ValueError:
        it_is = False
    return it_is


def print_user_data(name, age):
    print(name, age)


def ask_for_name():
    return input("what is your name: ")


def ask_for_age():
    return input("what is your age :")


def pull_data():
    global name, age
    name = ask_for_name()
    age = ask_for_age()


def calc_user_decades():
    global age, name
    decades = str(float(age) / float(10))
    text = "Okay {} looks like you are {} and have lived for {} decades"
    print(text.format(name, age, decades))


def run():
    pull_data()
    if is_num(age) & is_str(name):
        calc_user_decades()
    else:
        print(
            "oops, looks like either your try again. make sure age is a number and name is text."
        )


run()
