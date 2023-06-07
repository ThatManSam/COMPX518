# COMPX518-23A | Assigment 2
> Student: Joel Shepherd  
> ID: 1535837

# Encryption Program (Python, encryption.py)
This is a python program that will take in a filename for an image, and will encrypt that image using an AES cipher using a CBC, CFB and ECB mode of operation.
Three files will be outputted, one for each mode of operation, and will be named like `<input_image>_<mode>.jpg`, eg. `Image-Assignment2_ECB.jpg`.
  
To run the encryption program, the packages in the `requirements.txt` file will need to be installed.

## Environment setup
To install the required packages, the following commands need to be run
```bash
python3 -m venv venv                # Create a virtual python3 environment
source venv/bin/activate            # Enter the virtual environment
pip install -r requirements.txt     # Install the requirements into the virual environment
```

## Command line usage
```bash
Usage: python3 encryption.py <input_image>
```

# Cryptanalysis (Python, analysis.py)
The statistical analysis of the cipher and decrypting it was done through a python script. The script takes a filename as an argument for the cipher text file to be decrypted.
There are no requirements other than python3 to run this script.

## Command line usage
```bash
Usage: python3 analysis.py <input_file>
```


