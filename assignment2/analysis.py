from collections import Counter
import sys


def calculate_factor(e_value: int, t_value: int) -> int:
    """Calculates the factor for creating a letter mapping based on the value for e and t

    Args:
        e_value (int): the value for the letter e based on statistical analysis
        t_value (int): the value for the letter t based on statistical analysis

    Returns:
        int: An integer for the multiplication factor of the letter mapping
    """
    return (t_value - e_value) / (ord('t') - ord('e'))


def generate_letter_mapping(letter: str, factor: int, offset: int) -> int:
    """Generates a number mapping to the given letter

    Args:
        letter (str): the letter to map
        factor (int): the factor for the mapping pattern
        offset (int): the offset for the mapping pattern

    Returns:
        int: the mapped value
    """
    ascii_num = ord(letter.lower()) # Normalise all letters to lowercase values
    normalised = ascii_num - ord('a')
    return normalised * factor + offset
    

def generate_matrix(e_number = 28, factor = 2) -> dict:
    """Generates a dict of letters and their mapped values

    Args:
        e_number (int, optional): The value for e based on statistical analysis. Defaults to 28.
        factor (int, optional): The factor for the mapping pattern. Defaults to 2.

    Returns:
        dict: The letter mappings
    """
    # From statistical analysis for ciphertext3.txt, the letter e was 28 and the letter t was 58.
    # There is a difference of 30 between 28 and 58, and the difference between e and t in the alphabet is 15.
    # Thus, 30/15 = 2, so each letter corresponds to each even number relative to e being 28 (i.e. 30 is f)
    offset = e_number - (4 * factor)
    matrix = {}
    for i in range(26):
        letter = chr(i + ord("a"))
        matrix[generate_letter_mapping(letter, 2, offset)] = letter
    return matrix


def decrypt(ciphertext: str, substitution_matrix: dict) -> str:
    """Decrypts the ciphertext using the substitution matrix

    Args:
        ciphertext (str): The text to decrypt
        substitution_matrix (dict): The key mapping used for decryption

    Returns:
        str: The decrypted plain text
    """

    print(f"Substitution Matrix:\n{substitution_matrix}")
    cipher_split = ciphertext.split()
    output = ""
    for number in cipher_split:
        try:
            output += substitution_matrix.get(int(number))
        except TypeError:
            print(f"Error getting value in matrix from {number}")

    return output


if __name__ == "__main__":
    
    # Get the input file from command arguments
    if len(sys.argv) < 2:
        print(f'Usage: python3 {sys.argv[0]} <input_file>')
        exit(1)
        
    filename = sys.argv[1]
    
    try:
        # load all the numbers into a list
        with open(filename, "r") as f:
            numbers = f.readline().split()
    except FileNotFoundError:
        print(f"Couldn't find input file {filename}")
        exit(1)

    # Count each letter into a list of tuples and sort by the most frequent numbers
    sorted_counts = sorted(Counter(numbers).items(), key=lambda item: item[1], reverse=True)
    print("Frequency of Numbers:")
    for number, count in sorted_counts:
        print(f"{number}: {count}")

    e_value = int(sorted_counts[0][0])  # Most frequent value
    t_value = int(sorted_counts[1][0])  # Second most frequent value
    factor = calculate_factor(e_value, t_value)
    print(f"E value: {e_value} | T value: {t_value} | Factor: {factor} ")
    substitution_matrix = generate_matrix(e_value, factor)

    # Decrypt the cipher text
    with open(filename) as file:
        while True:
            line = file.readline()
            if line == "": break
            output = decrypt(line, substitution_matrix)
            print(output)