import os
from PIL import Image
import argparse

def convert_tga_to_webp(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.tga'):
            # Construct full file paths
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.webp')

            try:
                # Open the TGA image
                with Image.open(input_path) as img:
                    # Convert and save as WebP
                    img.save(output_path, 'WEBP')
                print(f"Converted {filename} to WebP")
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Convert TGA images to WebP format.")
    parser.add_argument("Example:", help="python convert_tga_to_webp.py /path/to/input/directory /path/to/output/directory")
    parser.add_argument("input_dir", help="Input directory containing TGA files")
    parser.add_argument("output_dir", help="Output directory for WebP files")
    args = parser.parse_args()

    convert_tga_to_webp(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()