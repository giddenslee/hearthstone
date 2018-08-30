import copy
class A:
    a = [-1]
    const = "111"
    def __init__(self):
        self.a = [0]
        self.b = None
    def set_b(self, b):
        self.b = b
    def set_a(self, b):
        self.a.append(b)

if __name__ == '__main__':
    aa = A()
    bb = A()
    aa.set_a(bb)
    print(aa.a)     #[0, <bb>]
    aa.set_b(bb)
    print(aa.b.a)   #[0]
    bb.set_a(-1)
    print(aa.b.a)   #[0, -1]
    print(bb.a)     #[0, -1]
    bb.set_b(bb)    # link on itself
    
    print("***copy_test***")
    c = copy.copy(aa)
    d = copy.deepcopy(aa)


    print(c.a)      #[0, <bb>]
    print(d.a)      #[0, <bb'>], bb' value == bb
    print(id(c.a)==id(aa.a))

    print(d.a[1].a) #[0, -1]
    print(bb.a)     #[0, -1]

    print(d.a[1].b) #<bb'>
    print(bb.b)     #<bb>
    
    