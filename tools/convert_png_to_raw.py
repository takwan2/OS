from PIL import Image
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: convert_png_to_raw.py input.png output.raw")
        return

    in_path, out_path = sys.argv[1], sys.argv[2]

    img = Image.open(in_path).convert("RGBA")
    with open(out_path, "wb") as f:
        f.write(img.width.to_bytes(4, "little"))
        f.write(img.height.to_bytes(4, "little"))
        f.write(img.tobytes())  # RGBA bytes

if __name__ == "__main__":
    main()
