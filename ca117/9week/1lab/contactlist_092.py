#!/usr/bin/env python3

class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.name} {self.phone} {self.email}'

class Contactlist(object):

    def __init__(self):
        self.d = {}

    def add(self, other):
        self.d[other.name] = other

    def remove(self, name):
        del self.d[name]

    def get(self, name):
        return self.d.get(name, None)

    def __str__(self):
        header = "Contact list\n------------"
        contacts_str = [str(contact) for name, contact in sorted(self.d.items())]
        return f"{header}\n" + "\n".join(contacts_str)

def main():
    clist = Contactlist()

    c1 = Contact('Sue', '085-6442378', 'sue@eircom.net')
    clist.add(c1)

    c2 = Contact('Jimmy', '086-1223277', 'james@apple.com')
    clist.add(c2)

    c3 = Contact('Wendy', '086-9112645', 'wendy@physics.dcu.ie')
    clist.add(c3)

    c = clist.get('Wendy')
    assert(c is c3)

    clist.remove('Wendy')
    c = clist.get('Wendy')
    assert(c is None)

    c4 = Contact('Abbey', '087-7586344', 'abbey@gmail.com')
    clist.add(c4)

    print(clist)

if __name__ == '__main__':
    main()
