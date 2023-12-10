# folder-tree-generator

This Python script generates a text file representing the directory structure and files for a given root folder.

You can see a sample file `tree123.txt`

## Usage

To use this script, call it from the command line passing the root path as an argument:

```
  python main.py "D:/Music/OPEDs"
```
Alternatively, it will prompt for you to input the path if one is not provided.
```
python main.py
```
The script generates an output text file named `tree{total_files}.txt` of the given root dir, saved to the same folder as the main script.

## Features
- Simple, easy & handy
- Sorts files and folders alphabetically at each level
- Handles any depth of nested folders
- Provides count of total files mapped
