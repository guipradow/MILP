from pyscipopt import Model

model = Model('exemplo')

x = model.addVar('x', vtype='integer')
y = model.addVar('y')

model.setObjective(x + y, sense='maximize')

model.addCons(-x+2*y<=7)
model.addCons(2*x+y<=14)
model.addCons(2*x-y<=10)

model.optimize()

sol = model.getBestSol()

print(f'x: {sol[x]}')
print(f'y: {sol[y]}')
