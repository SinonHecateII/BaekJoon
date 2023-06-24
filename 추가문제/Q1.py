def solve1(h : int, k : int, boxes : list):
    count_list = []

    boxes.sort()
    now = 0
    idx = 0

    while now < h - k:
        step = 0
        val = 0
        while idx != len(boxes):
            tmp = boxes[idx]
            tmp_step = tmp - now
            print(tmp)
            idx += 1

            if tmp_step > k:
                break
            val = tmp
            step = tmp_step

        if step > k:
            return -1
        if idx == len(boxes) and val + k < h:
            return -1

        idx -= 1
        now = val
        count_list.append(val)
        print(f"--------- {now}")

    print(count_list)
    return len(count_list)

boxes = [9, 8, 7, 6, 5, 4, 3, 2, 1]
h = 10
k = 1
print(solve1(h, k, boxes))