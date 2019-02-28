from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as td:
    dir_path = Path(td)

    for i in range(5):
        p = (dir_path / str(i))
        p.mkdir()
        stat = p.stat()
        print(f'[{i:02d}] ctime: {stat.st_ctime}, mtime: {stat.st_mtime}, atime: {stat.st_atime}, ')

    for i in range(5, 10):
        p = (dir_path / str(i))
        p.touch()
        stat = p.stat()
        print(f'[{i:02d}] ctime: {stat.st_ctime}, mtime: {stat.st_mtime}, atime: {stat.st_atime}, ')
