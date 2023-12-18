## Algoritms
Daudzkriteriāls lēmumspieņemšanas algoritms ir parādīts blokshēmas veidā.

![algoritms](/algo.png "algoritms")

```math
x_{vid} = a^2+b^2
```
```python
def predict(d, v, pc, sp, sc):
    optimalAmount = 0

    # datu tipu konversija
    d = float(d)
    v = float(v)
    pc=float(pc)
    sp=float(sp)
    sc=float(sc)

    # aprēķina izmaksu mainīgos
    Cu = sp-pc
    Co = pc-sc

    # aprēķina kritisko attiecību
    CR = Cu/(Cu+Co)

    optimalAmount = norm.ppf(CR, loc=d, scale=v)

    optimalAmount=round(optimalAmount,0)

    return optimalAmount
 
```

