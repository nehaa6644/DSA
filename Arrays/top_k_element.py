def topKFrequent(nums, k):
    #Count frequency
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
# initializing the count for the number
            count[num] = 1

    # Sorting based on frequency in descending order
    sorted_nums = sorted(count, key=count.get, reverse=True)

    #Taking first k elements
    return sorted_nums[:k]


nums = list(map(int, input().split()))
k = int(input())

print(topKFrequent(nums, k))