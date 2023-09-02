d = [2,3,4,5]
s = [ (d[i] + d[i + 1] + d[i - 1]) for i in range(len(d) - 1)]
s.append(d[-1] + d[-2] + d[0])
print(s)
print(max(s))
