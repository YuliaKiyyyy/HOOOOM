"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
from pathlib import Path
from typing import Optional, Callable
import os


def universal_file_counter(
        dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    line_count = 0
    token_count = 0
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    if tokenizer is None:
                        line_count += len(f.readlines())
                    else:
                        tokens = tokenizer(f.read())
                        token_count += len(tokens)
    if tokenizer is None:
        return line_count
    else:
        return token_count