import collections


def count_numbers(filename):
    """Counts the number of occurrences of each number in a file.

    Args:
      filename: The path to the file to count.

    Returns:
      A dictionary mapping each number to the number of times it appears in the file.
    """
    with open(filename, "r") as f:
        numbers = f.readline().split()

    counts = collections.Counter(numbers)
    return counts


def sort_by_frequency(counts):
    """Sorts a dictionary of number counts by frequency.

    Args:
      counts: A dictionary mapping each number to the number of times it appears.

    Returns:
      A list of tuples, where each tuple contains a number and the number of times it appears.
    """
    sorted_counts = sorted(
        counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts


def decrypt(ciphertext: str):
    substitution_matrix = {
        28: "e",
        58: "t",
        20: "a",
        48: "o",
        36: "i",
        56: "n",
        54: "s",
        46: "r",
        42: "h",
        34: "d",
        24: "l",
        44: "u",
        30: "c",
        26: "m",
        22: "f",
        50: "y",
        32: "w",
        68: "g",
        60: "p",
        62: "b",
        40: "v",
        64: "k",
        70: "x",
        38: "q",
        52: "j",
    }

    cipher_split = ciphertext.split()
    output = ""
    for number in cipher_split:
        output += substitution_matrix.get(int(number))

    return output


if __name__ == "__main__":
    filename = "/home/js479/Documents/COMPX518/assignment2/ciphertext3.txt"
    # counts = count_numbers(filename)
    # sorted_counts = sort_by_frequency(counts)
    # for number, count in sorted_counts:
    #     print(f"{number}: {count}")

    with open(filename) as file:
        while True:
            line = file.readline()
            if line == "": break
            output = decrypt(line)
            print(output)