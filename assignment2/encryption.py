import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from PIL import Image, UnidentifiedImageError

KEY = bytes.fromhex("770A8A65DA156D24EE2A093277530142")
BLOCK_SIZE = 16

def encrypt(key: bytes, input_data: bytes, type: int) -> bytes:
    """Encrypts the data using AES encryption

    Args:
        key (bytes): The key to be used for encryption
        input_data (bytes): The data to be encrpted
        type (int): The AES mode to use. Supports ECB, CBC and CFB

    Raises:
        ValueError: Raised if unsupported type for AES mode is given

    Returns:
        bytes: The encrypted Data
    """

    if type == AES.MODE_ECB or type == AES.MODE_CBC:
        cipher = AES.new(key, type)
        # Using pad so that the data is block aligned for ECB and padded to 16 bytes for CBC
        ciphertext = cipher.encrypt(pad(input_data, BLOCK_SIZE))
        return ciphertext
        
    if type == AES.MODE_CFB:
        # Use segment_size= for the CFB cipher,
        # cipher = AES.new(key, AES.MODE_CFB, segment_size=BLOCK_SIZE)
        cipher = AES.new(key, AES.MODE_CFB)
        ciphertext = cipher.encrypt(input_data)
        return ciphertext
    
    raise ValueError(f"Type: {type} is not supported")

def encrypt_image(input_filename: str, output_filename: str, type: int) -> None:
    """Encrypt the input with the AES type and outputs to a file

    Args:
        input_filename (str): The input filename for the image
        output_filename (str): The output filename for the encrypted image
        type (int): The AES mode, supports ECB, CBC and CFB
    """

    # Read in the image, taking the format of the filename suffix
    try:
        plain_image = Image.open(input_filename)
    except FileNotFoundError:
        print(f'The file "{input_filename}" could not be found')
        exit(2)
    except UnidentifiedImageError:
        print(f"Couldn't identify image type for {input_filename} or file has incorrect suffix")
        exit(2)

    # Encrypt the image
    plain_text = plain_image.tobytes()
    cipher_text = encrypt(KEY, plain_text, type)
    
    # Output the encrypted image, taking the format of the filename suffix
    cipher_image = Image.frombytes(plain_image.mode, (plain_image.width, plain_image.height), cipher_text)
    cipher_image.save(output_filename)


if __name__ == '__main__':

    # Get the input file from command arguments
    if len(sys.argv) < 2:
        print(f'Usage: python3 {sys.argv[0]} <input_image>')
        exit(1)
    
    input_file = sys.argv[1]

    # Sets the encryption modes that the file will be encrypted with
    encryption_modes = [
        ('CBC', AES.MODE_CBC),
        ('CFB', AES.MODE_CFB),
        ('ECB', AES.MODE_ECB),
    ]

    # Encrypt the image with the encryption mode and output
    for name, type in encryption_modes:
        print(f'Encrypting with {name}')
        # Output file is based on input filename with a different suffix
        # I.e., Adds the encryption mode name and the suffix .jpg
        # If input fileame was image.bmp, an output would be image-CBC.jpg
        (file_name, _) = os.path.splitext(input_file)
        output_file = f'{file_name}_{name}.jpg'
        # Load image, encrypt it and output
        encrypt_image(input_file, output_file, type)
