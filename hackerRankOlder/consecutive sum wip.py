#!
def consecsum(arr,target):
  left = 0
  right = 0
  for i in range(len(arr)+1):
    
    if arr(i) > target:
      right +=1
    else:
      total = sum(arr[left..right])
  


print(consecsum([6,12,1,7,5,2,3], 14))