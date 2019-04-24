class A(object):
    def test(self):
        self.l = ['xie', 'tang', 'li', 'haung']
        print(self.l.pop())

    def tested(self):
        print(self.l)
        print(self.l.pop())


a = A()
a.test()
a.tested()
