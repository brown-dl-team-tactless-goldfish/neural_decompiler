def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # print "nums = ", nums

    if nums == [] or k == 0:
        return []

    dic = {}
    # dic_2 = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1

        # dic_2[dic[num]] = num
    # print "dic = ", dic

    # return

    dic_2 = {}
    for item in dic.items():
        # print "item = ", item
        key, val = item[0], item[1]
        # print "key = ", key, " val = ", val

        if val not in dic_2:
            dic_2[val] = [key]
        else:
            dic_2[val].append(key)

    # print "dic_2 = ", dic_2


    keys = sorted(dic_2.keys(), reverse=True)
    # print "keys = ", keys
    res = []
    i = 0
    while len(res) < k:
        key = keys[i]

        # print "key = ", key
        for val in dic_2[key]:
            # print "val = ", val
            if len(res) < k:
                res.append(val)
        i += 1

    # print "end res = ", res

    return res