# Txt2PNG (t2p)
Txt2PNG is exactly what it sounds like; it can compress text files or code into images, and it can decompress those images back into identical text files.
## Description

This is a Python script that can be used to compress and decompress files using images. The script uses the PIL (Python Imaging Library) module to convert the file data to an image and back to the original data.

## Usage

To use this script, follow these steps:

1. Clone or download the repository to your local machine.
2. Make sure you have the required modules installed (Pillow).
3. Open a terminal window and navigate to the directory where the script is located.
4. Run the script by typing `python image_compression.py` and pressing Enter.
5. Follow the prompts to enter the input and output file paths, and whether to compress or decompress the file.

Note: You may need to install the required module using pip by running `pip install Pillow`.

## Code Explanation

The script contains two functions, `compress_file` and `decompress_file`, which take two arguments each: the input file path and the output file path.

`compress_file` reads the input file as binary data and converts it to a list of hex values. It then calculates the size of the image needed to store the data, creates a new PIL Image object, and fills it with the hex values. The image is then saved to the output file.

`decompress_file` opens the input image using PIL and retrieves the pixel data. It converts the pixel data to bytes and saves it to the output file.

The `__main__` block of the script prompts the user for input to determine whether to compress or decompress the file, and then prompts for the input and output file paths. The appropriate function is then called based on the user's input.

## Example

Here's an example of how to use the script to compress and decompress a file:

```
$ python t2p.py
Enter 'c' to compress or 'd' to decompress: c
Enter input file path: test_file.txt
Enter output file path: test_file.png
File compressed successfully. Image saved as test_file.png

$ python t2p.py
Enter 'c' to compress or 'd' to decompress: d
Enter input file path: test_file.png
Enter output file path: test_file_decompressed.txt
File decompressed successfully. Data saved as test_file_decompressed.txt
```
