import sys
from pathlib import Path

DIR_SYMBOL = "📂 "
FILE_SYMBOL = "📄 "
INDENT = 3 * " "

def generate_tree(root_dir: Path, depth=0) -> str:
    files_count = 0
    tree_str = f"{INDENT * depth}{DIR_SYMBOL}{root_dir.name}\n"

    for path in sorted(root_dir.iterdir()):
        if path.is_dir():
            subtree, subtree_files = generate_tree(path, depth + 1)
            tree_str += subtree
            files_count += subtree_files
        else:
            tree_str += f"{INDENT * (depth + 1)}{FILE_SYMBOL}{path.name}\n"
            files_count += 1

    return tree_str, files_count

def main(root_path):
    print(f"Generating tree for {root_path}")
    tree_str, files_num = generate_tree(root_path)
    output_file = f"tree{files_num}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(tree_str)
        
    print(f"Tree file Generated for {root_path}")

if __name__ == "__main__":
    root_path = (sys.argv[1]) if len(sys.argv) > 1 else input("Enter the Path: ") or None

    if root_path is not None:
        root_path = root_path.strip('"')
        main(Path(root_path))
    else:
        print("No path specified to generate.")
