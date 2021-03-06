"""
놈 정렬 (gnome sort)
- 앞으로 이동하며 잘못 정렬된 값을 찾은 후, 올바른 위치로 값을 교환하며 다시 뒤로 이동
- 최선의 경우, 시간복잡도는 O(n)
- 평균과 최악의 경우, O(n*n)
"""


def gnome_sort(seq):
    i = 0
    # print(i, seq)
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
        # print(i, seq)
    return seq


def test_gnome_sort():
    seq = [5, 3, 2, 4]
    assert(gnome_sort(seq) == sorted(seq))
    print("테스트 통과!")


if __name__ == "__main__":
    test_gnome_sort()

