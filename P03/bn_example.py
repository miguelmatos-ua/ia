from bayes_net import *

# Exemplo dos acetatos:

bn = BayesNet()

bn.add('r', [], 0.001)  # theaft
bn.add('t', [], 0.002)  # earthquake

bn.add('a', [('r', True), ('t', True)], 0.950)  # alarm
bn.add('a', [('r', True), ('t', False)], 0.940)
bn.add('a', [('r', False), ('t', True)], 0.290)
bn.add('a', [('r', False), ('t', False)], 0.001)

bn.add('j', [('a', True)], 0.900)  # john calls
bn.add('j', [('a', False)], 0.050)

bn.add('m', [('a', True)], 0.700)  # mary calls
bn.add('m', [('a', False)], 0.100)

conjunction = [('j', True), ('m', True), ('a', True), ('r', False), ('t', False)]

print("example)\nAll true: {}\n".format(bn.jointProb(conjunction)))

# ----- SOF -------

sof = BayesNet()

sof.add('wol', [], 0.6)
sof.add('wf', [('wol', True), ('nh', False)], 0.01)
sof.add('wf', [('wol', True), ('nh', True)], 0.02)
sof.add('wf', [('wol', False), ('nh', False)], 0.001)
sof.add('wf', [('wol', False), ('nh', True)], 0.011)

sof.add('aue', [('wol', False)], 0.001)
sof.add('aue', [('wol', True)], 0.9)

sof.add('uwp', [], 0.05)
sof.add('nh', [('uwp', True)], 0.25)
sof.add('nh', [('uwp', False)], 0.004)
sof.add('hmf', [('uwp', False), ('nh', True)], 0.1)
sof.add('hmf', [('uwp', False), ('nh', False)], 0.01)
sof.add('hmf', [('uwp', True)], 0.9)

alltrue = [('wol', True), ('nh', True), ('wf', True), ('hmf', True), ('aue', True), ('uwp', True)]
allfalse = [('wol', False), ('nh', False), ('wf', False), ('hmf', False), ('aue', False), ('uwp', False)]

print("1)\nAll true: {}".format(sof.jointProb(alltrue)))
print("All false: {}\n".format(sof.jointProb(allfalse)))

# ----- ex3 ---------

print("2)\nNeeding help, True: {}".format(sof.individual_prob('nh', True)))
print("Needing help, False: {}".format(sof.individual_prob('nh', False)))

print("\n------------------------------------------------\n")

conj1 = sof.conjuctions1(['a', 'b'])
conj2 = sof.conjuctions2(['a', 'b'])

print(conj1, "\n", conj2)

print("\n------------------ III.10 ----------------------\n")




