def consicutive_odds(arr):
    for i in range(len(arr) - 2):
        if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
            print(arr[i],arr[i+1],arr[i+2])
            return True
    return False
print(consicutive_odds([1,2,34,3,4,5,7,23,12]))