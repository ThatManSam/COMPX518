

# Part 1 | MD5 Collisions

## 1.1
Prefix File | Text
> This is the prefix text in the prefix file!

Prefix File | Hex
> 54 68 69 73 20 69 73 20 74 68 65 20 70 72 65 66 69 78 20 74 65 78 74 20 69 6E 20 74 68 65 20 70 72 65 66 69 78 20 66 69 6C 65 21

Out1 | Hex
> 54 68 69 73 20 69 73 20 74 68 65 20 70 72 65 66 69 78 20 74 65 78 74 20 69 6E 20 74 68 65 20 70 72 65 66 69 78 20 66 69 6C 65 21 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11 D8 D7 37 5D A4 C8 BD 9A 1D 8A 37 01 CF C3 AD 6E 8E 27 C9 32 67 B9 48 35 0E 7A 4A 47 32 B1 80 70 DD B3 EB E2 EC 0D A7 0F 66 D3 14 88 7D B5 1E 21 FA CF 51 6B 56 AE CC C1 6F F8 96 BA C9 BB 26 BF 47 2B 94 B3 1A 73 43 2A 3F AE 1D 3F 44 3D 8E 92 52 95 96 00 04 F1 DD 02 75 A5 A7 CD C4 29 8C 15 78 7E CA 49 B7 7F A5 02 7D 09 AA 89 78 F9 5E BE 0C 08 2D CE D2 13 9D AF D6 CA 7E B2 FD 88 1B

Out2 | Hex
> 54 68 69 73 20 69 73 20 74 68 65 20 70 72 65 66 69 78 20 74 65 78 74 20 69 6E 20 74 68 65 20 70 72 65 66 69 78 20 66 69 6C 65 21 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 11 D8 D7 37 5D A4 C8 BD 9A 1D 8A 37 01 CF C3 AD 6E 8E 27 49 32 67 B9 48 35 0E 7A 4A 47 32 B1 80 70 DD B3 EB E2 EC 0D A7 0F 66 D3 14 88 FD B5 1E 21 FA CF 51 6B 56 AE CC C1 6F F8 16 BA C9 BB 26 BF 47 2B 94 B3 1A 73 43 2A 3F AE 1D 3F 44 3D 8E 92 52 95 16 00 04 F1 DD 02 75 A5 A7 CD C4 29 8C 15 78 7E CA 49 B7 7F A5 02 7D 09 AA 89 F8 F8 5E BE 0C 08 2D CE D2 13 9D AF D6 CA FE B2 FD 88 1B

## 1.2 Questions
### 1.2.1 How many new bytes does the tool generate?
9 * 16 + 5 = 149 bytes  
The md5sollgen tool added 149 bytes to the end of the prefix file. The prefix file was 43 bytes long, so the total is 192 bytes
To break down what was added, 21 bytes of `00` were added to the message to pad it be a 64 byte long block, then two more blocks of 64 were added after.

### 1.2.2 What happens when the prefix is 64 bytes long or not
When the prefix is 64 bytes long the tool added 128 bytes. Since the message was already a 64 byte long block the tool didn't need to pad the message with `00` bytes. So only the two blocks of 64 blocks needed to be added to each file.

# Part 2 | Threat Modelling

