from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string. ascii_letters + string.digits + " "*3#+ string.punctuation#
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", email="", home="")] + [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 20), lastname=random_string("lastname", 25),
            nickname=random_string("nickname", 10), address=random_string("address", 10), home=random_string("home", 8),
            mobile=random_string("mobile", 8), work=random_string("work", 8), email=random_string("email", 8),
            email2=random_string("email2", 8), email3=random_string("email3", 8), phone2=random_string("phone2", 8))
    for i in range (n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))