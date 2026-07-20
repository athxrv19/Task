from pathlib import Path
import hashlib


def file_hash(path, chunk_size=8192):
    sha1 = hashlib.sha1()

    with open(path, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            sha1.update(chunk)

    return sha1.hexdigest()


def find_duplicates(folder):
    hashes = {}

    for file in Path(folder).rglob("*"):
        if file.is_file():
            h = file_hash(file)
            hashes.setdefault(h, []).append(file)

    total_saved = 0

    for files in hashes.values():
        if len(files) > 1:
            print("=" * 50)
            print("Duplicate Files:")

            for f in files:
                print(f)

            size = files[0].stat().st_size
            recoverable = size * (len(files) - 1)

            total_saved += recoverable

            print(f"Recoverable: {recoverable} bytes\n")

    print("=" * 50)
    # Convert bytes to Megabytes (1 MB = 1024 * 1024 bytes)
    total_saved_mb = total_saved / (1024 * 1024)
    print(f"Total Recoverable Space: {total_saved_mb:.2f} MB ({total_saved} bytes)")


if __name__ == "__main__":
    folder = input("Enter folder path: ")
    find_duplicates(folder)