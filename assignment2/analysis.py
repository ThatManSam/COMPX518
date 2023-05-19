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

def generate_letter_mapping(letter: str, factor: int, offset: int):
    ascii_num = ord(letter.lower())
    normalised = ascii_num - ord('a')
    return normalised * factor + offset
    

def generate_matrix(e_number = 28, factor = 2):
    # From stats analysis, the letter e was 28 and the letter t was 58.
    # There is a difference of 30 between 28 and 58, and the difference between e and t in the alphabet is 15.
    # Thus, 30/15 = 2, so each letter corresponds to each even number relative to e being 28 (i.e. 30 is f)
    offset = e_number - (4 * factor)
    matrix = {}
    for i in range(26):
        letter = chr(i + ord("a"))
        matrix[generate_letter_mapping(letter, 2, offset)] = letter
    return matrix

def decrypt(ciphertext: str):
    substitution_matrix = generate_matrix(28)

    print(substitution_matrix)
    cipher_split = ciphertext.split()
    output = ""
    for number in cipher_split:
        output += substitution_matrix.get(int(number))

    return output


if __name__ == "__main__":
    filename = "./ciphertext3.txt"
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