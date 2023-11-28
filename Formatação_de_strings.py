a = 'a'
b = 'b'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f}'

formato = string.format(nome1=a, nome2=b, nome3=c)

formato1 = 'nome1=a={0} nome2=b={1} nome3=c={2}'.format(a, b, c)

print(formato)
print(formato1)


