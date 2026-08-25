import heapq

def huffman_coding(chars, freq):
    heap = []

    for char, f in zip(chars, freq):
        heapq.heappush(heap, (f, char))

    while len(heap) > 1:
        f1, c1 = heapq.heappop(heap)
        f2, c2 = heapq.heappop(heap)

        heapq.heappush(heap, (f1 + f2, c1 + c2))

    print("Huffman Tree:", heap[0])


chars = ['A', 'B', 'C', 'D']
freq = [5, 9, 12, 13]

huffman_coding(chars, freq)
