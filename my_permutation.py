"""
An example of permutation in Python
All feedback are welcome
"""

all_permutations = []  # contains a list of permutations found

def permute(items_to_permute):
    """
    Recursive method to collect permutations
    :param items_to_permute: A list of items to permute
    """

    if not isinstance(items_to_permute, list):
        items_to_permute = [items_to_permute]

    if not items_to_permute in all_permutations:
        all_permutations.append(items_to_permute)

    if len(items_to_permute) > 1:
        for i in xrange(0, len(items_to_permute)):
            # iterate through each items, and shift it to the back of the list
            # eg if we have ABCD
            # first shift A to the back, eg BCD A
            # second shift B to the back, eg ACD B
            # third shift C to the back, eg ABD C
            # then permute each newly found combination
            # eg call permute on BCDA, ACDB, ABDC
            item_to_shift = items_to_permute[i]
            head = []
            tail = []
            if i != 0:
                head = items_to_permute[0:i]
            if i != len(items_to_permute):
                tail = items_to_permute[i+1:]
            new_combo = head + tail + [item_to_shift]
            if not new_combo in all_permutations:
                all_permutations.append(new_combo)
                permute(new_combo)


def main():
    """
    main method

    """
    permute(['A', 'B', 'C', 'D', 'E'])
    for combo in all_permutations:
        print combo
    print "%s permutations found " % len(all_permutations)


if __name__ == "__main__":
    main()