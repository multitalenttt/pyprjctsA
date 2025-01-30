from main import TAnd, TNot, TE, TOr, TNAnd, TNOr, TXor, TImp
# -*- coding: utf-8 -*-

print('A', 'B', 'S')
trigger1 = TOr()
trigger2 = TNot()
for in1 in 0,1:
    for in2 in 0,1:
        trigger1.In1 = in1
        trigger1.In2 = in2
        trigger2.In1 = trigger1.Res

        print(in1, in2, trigger2.Res)








