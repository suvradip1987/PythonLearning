
samplelis1= [1,2,3]
samplelis2= [4,5,6]
samplelis3= [7,8,9]

originalList = [samplelis1,samplelis2,samplelis3]

copiedList= originalList.copy()

print('Before Changes')

print('original list')
print(originalList)
print('copied list')
print(copiedList)

originalList.append('5')
originalList[0][0] = 'x'

print('After Changes')
print('original list')
print(originalList)
print('copied list')
print(copiedList)