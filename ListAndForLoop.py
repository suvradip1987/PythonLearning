# below is the way we can create Lists.

countrylist = ['in', 'uk', 'usa', 12]
countrylist.append('PK')
countrylist.remove('uk')

newlist = countrylist.copy()
newlist.append(12)
newlist.extend(countrylist)

for item in newlist:
    print(item)
    print(type(item))

if 'uk' in countrylist:
    print('Uk is present in the list')
