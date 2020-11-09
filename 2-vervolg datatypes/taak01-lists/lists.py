maanden = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'july', 'september', 'augustus', 'oktober', 'november', 'december']

maanden[6] = "juli"

print(type(maanden))
print(len(maanden))
print(maanden[6])
print(maanden[0:12])

print('\n')

for alles in maanden:
    print(alles, len(alles))
