from time import time

from glob import glob
from pathlib import Path
from rust_glob import glob as rglob

PATH = "/home/cmaureir/dev/"

print("glob")
s = time()
print("Files:", len(glob(f"{PATH}**")))
glob_t0 = time()-s
print("Time:", glob_t0)
print()
print("glob (recursive)")
s = time()
print("Files:", len(glob(f"{PATH}**", recursive=True)))
glob_tr = time()-s
print("Time:", glob_tr)
print("-"*100)
print("pathlib")
s = time()
print("Files:", len(list(Path(PATH).glob("*"))))
print("Time:", time()-s)
print()
print("pathlib (recursive)")
s = time()
print("Files:", len(list(Path(PATH).rglob("*"))))
print("Time:", time()-s)
print("-"*100)
print("rust_glob")
s = time()
print("Files:", len(rglob(PATH)))
print("Time:", time()-s)
print()
print("rust_glob (recursive)")
s = time()
print("Files:", len(rglob(PATH, recursive=True)))
print("Time:", time()-s)
