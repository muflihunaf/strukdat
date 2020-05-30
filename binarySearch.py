
def binarySearchRekursif(data, bil, start=0, end=None,hasil = []):
    if end is None:
        end = len(data) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if bil == data[mid]:
        hasil.append(mid)
        if data[mid+1] == bil:
            return binarySearchRekursif(data, bil, mid-1, end,hasil)
        return hasil
    if bil < data[mid]:
        return binarySearchRekursif(data, bil, start, mid - 1)
    return binarySearchRekursif(data, bil, mid + 1, end)


print(binarySearchRekursif([2, 3, 4,5, 6,6,6,7, 8], 6))
