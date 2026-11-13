"""food-picture-01 entry program (Python 3.13, standard library only).

entry.png beside this file holds the picture (JPEG bytes in a file named
entry.png); this program copies it, byte for byte, to the output
directory. The grader runs it with no MAKEFUN_OUTPUT_DIR set on a
read-only filesystem whose only writable mount is /output, so the
default below must stay "/output", never a relative path.
"""

import os

CHUNK_SIZE = 64 * 1024


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        for chunk in iter(lambda: fin.read(CHUNK_SIZE), b""):
            fout.write(chunk)
        fout.flush()
        os.fsync(fout.fileno())


if __name__ == "__main__":
    main()
