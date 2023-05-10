import os
import math
from PIL import Image

def compress_file(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()
        hex_data = [data[i:i + 3] for i in range(0, len(data), 3)]

    size = int(math.ceil(math.sqrt(len(hex_data))))
    img = Image.new('RGB', (size, size), color=(0, 0, 0))

    for i, hex_val in enumerate(hex_data):
        x, y = i % size, i // size
        color = tuple(int(hex_val[j:j+1].hex(), 16) if j < len(hex_val) else 0 for j in range(3))
        img.putpixel((x, y), color)

    img.save(output_file)

def decompress_file(input_file, output_file):
    img = Image.open(input_file)
    width, height = img.size
    data = bytearray()

    for y in range(height):
        for x in range(width):
            color = img.getpixel((x, y))
            for channel in color:
                data.append(channel)

    original_size = os.path.getsize(input_file)
    with open(output_file, "wb") as f:
        f.write(data[:original_size])

if __name__ == "__main__":
    choice = input("Enter 'c' to compress or 'd' to decompress: ").lower()
    input_file = input("Enter input file path: ")
    output_file = input("Enter output file path: ")

    if choice == "c":
        compress_file(input_file, output_file)
        print(f"File compressed successfully. Image saved as {output_file}")
    elif choice == "d":
        decompress_file(input_file, output_file)
        print(f"File decompressed successfully. Data saved as {output_file}")
    else:
        print("Invalid choice. Please enter 'c' or 'd'.")
