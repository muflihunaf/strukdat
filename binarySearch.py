
def binarySearchRekursif(data, bil, start=0, end=None,hasil = []):
    if end is None:
        end = len(data) - 1
        print('Data: ', data)
        print('key:', bil)
    if start > end:
        return False

    mid = (start + end) // 2
    print('mid',mid,start,end)
    if bil == data[mid]:
        hasil.append(mid)
        if data[mid+1] == bil:
            return binarySearchRekursif(data, bil, mid-1,end,hasil)
        return mid
    if bil < data[mid]:
        return binarySearchRekursif(data, bil, start, mid - 1)
    return binarySearchRekursif(data, bil, mid + 1, end)


# print(binarySearchRekursif([2, 3, 4,5,6,6,6,6,7,7, 8,8,8], 8))
a = str(54**2)
h = int(a[1:3])
print(h)
print(80/5)
