import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError ("List must contain nine numbers.")
  else:
    l = np.reshape(list, (3,3))
    lf = l.flatten()
    mc, vc, stdc, maxc, minc, sumc, mr, vr, stdr, maxr, minr, sumr = ([] for i in range(12))
    for column in l.T:
      mc.append(column.mean())
      vc.append(column.var())
      stdc.append(column.std())
      maxc.append(column.max())
      minc.append(column.min())
      sumc.append(column.sum())

    for row in l:
      mr.append(row.mean())
      vr.append(row.var())
      stdr.append(row.std())
      maxr.append(row.max())
      minr.append(row.min())
      sumr.append(row.sum())
      

    calculations = {
      'mean': [mc, mr, lf.mean()],
      'variance': [vc, vr, lf.var()],
      'standard deviation': [stdc, stdr, lf.std()],
      'max': [maxc, maxr, lf.max()],
      'min': [minc, minr, lf.min()],
      'sum': [sumc, sumr, lf.sum()]
    }
    return calculations