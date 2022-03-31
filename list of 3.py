# program to find 007 in the given list
def spy(arr):
    return '007' in ''.join(str(i) for i in arr)
data = [1,2,4,0,0,7,3]
print(spy(data))
