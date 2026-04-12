import os
import cv2
from core.remover import remove_watermark

INPUT_DIR = "../data/input"
OUTPUT_DIR = "../data/output"


def process_images():
    if not os.path.exists(INPUT_DIR):
        print(f"[ERROR] Input folder not found: {INPUT_DIR}")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    files = os.listdir(INPUT_DIR)
    if not files:
        print("[INFO] No images found in input folder.")
        return

    for file in files:
        input_path = os.path.join(INPUT_DIR, file)
        output_path = os.path.join(OUTPUT_DIR, f"cleaned_{file}")

        if not file.lower().endswith((".png", ".jpg", ".jpeg")):
            print(f"[SKIP] Not an image: {file}")
            continue

        print(f"[PROCESSING] {file}")

        image = cv2.imread(input_path)
        if image is None:
            print(f"[ERROR] Failed to read: {file}")
            continue

        result = remove_watermark(image)

        cv2.imwrite(output_path, result)
        print(f"[SAVED] {output_path}")


if __name__ == "__main__":
    process_images()
