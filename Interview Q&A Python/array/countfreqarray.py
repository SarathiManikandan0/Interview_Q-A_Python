#Count frequency of each element in the array

def countFreq(arr, n):
    visited = [False] * n
    for i in range(n):
        if (visited[i] == True):
            continue
        count = 1
        for j in range(i + 1, n):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1
        print(arr[i], count)


if __name__ == "__main__":
    arr = [10,5,10,15,10,5]
    n = len(arr)
    countFreq(arr, n)