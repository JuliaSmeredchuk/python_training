from model.contact import Contact
import random
import string


testdata = [
    Contact(firstname="name1", middlename="test", lastname="test1", address="address1")
]


#def random_string(prefix, maxlen):
    #symbols = string. ascii_letters + string.digits + " "*3#+ string.punctuation#
    #return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [Contact(firstname="", lastname="", email="", home="")] + [
    #Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 20), lastname=random_string("lastname", 25),
            #nickname=random_string("nickname", 10), address=random_string("address", 10), home=random_string("home", 8),
            #mobile=random_string("mobile", 8), work=random_string("work", 8), email=random_string("email", 8),
            #email2=random_string("email2", 8), email3=random_string("email3", 8), phone2=random_string("phone2", 8))
    #for i in range (5)
#]
