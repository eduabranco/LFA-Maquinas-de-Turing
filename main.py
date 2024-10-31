from q1 import mt_q1
from q2 import mt_q2
from q3 import mt_q3
from q4a import mt_q4a
from q4b import mt_q4b
from q4c import mt_q4c
from q4d import mt_q4d

class test():
    def q1():
        print(mt_q1([0,0,1,1]))
        print(mt_q1([1,1,1,1,0,1]))
        print(mt_q1([1,1,1,1,1,1,1]))
        print(mt_q1([0]))
        print(mt_q1([1]))
        input("Teste Q1 realizado. Aperte [ENTER] para prosseguir.")
        
    def q2():
        print(mt_q2([]))
        print(mt_q2([1]))
        print(mt_q2([1, 1]))
        print(mt_q2([1, 1, 1]))
        print(mt_q2([1, 1, 1, 1]))
        print(mt_q2([1, 1, 1, 1, 1, 1, 1]))
        input("Teste Q2 realizado. Aperte [ENTER] para prosseguir.")

    def q3():
        print(mt_q3([0]))
        print(mt_q3([1, 0]))
        print(mt_q3([0, 1]))
        print(mt_q3([1, 0, 1]))
        print(mt_q3([1, 1, 0, 1, 1]))
        print(mt_q3([1, 1, 0, 1, 1, 1]))
        print(mt_q3([1, 1, 1, 1, 1, 0, 1, 1]))
        input("Teste Q3 realizado. Aperte [ENTER] para prosseguir.")

    def q4a():
        print(mt_q4a(['#']))
        print(mt_q4a([0, 1, '#', 1, 0]))
        print(mt_q4a(['#', 1, '#', 1, 0]))
        print(mt_q4a([0, 1, '#', 0, 1]))
        print(mt_q4a([0, 1, '#', 1, 0, 0]))
        input("Teste Q4 Letra A realizado. Aperte [ENTER] para prosseguir.")
            
    def q4b():
        print(mt_q4b(['a','a','b','b','c','c']))
        print(mt_q4b(['a','a','b','b','c']))
        print(mt_q4b(['a','a','b','c','c']))
        print(mt_q4b(['a','b','b','c']))
        print(mt_q4b(['a','b','b','c','c','c']))
        input("Teste Q4 Letra B realizado. Aperte [ENTER] para prosseguir.")

    def q4c():
        print(mt_q4c(['a','b','c','c']))
        print(mt_q4c(['a','b', 'b','c','c', 'c']))
        print(mt_q4c(['a','b','c','c', 'c']))
        print(mt_q4c(['a', 'a','c','c']))
        print(mt_q4c(['a', 'a','b','c']))
        input("Teste Q4 Letra C realizado. Aperte [ENTER] para prosseguir.")

    def q4d():
        print(mt_q4d([]))
        print(mt_q4d(['a','b','c']))
        print(mt_q4d(['a','a','b', 'c']))
        print(mt_q4d(['a','b','b','c']))
        print(mt_q4d(['a','c','b','c']))
        input("Teste Q4 Letra D realizado. Aperte [ENTER] para prosseguir.")


test.q1()
test.q2()
test.q3()
test.q4a()
test.q4b()
test.q4c()
test.q4d()