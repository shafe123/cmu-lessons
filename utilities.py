from json import load, dump

def clear_code_blocks(input_notebook_path: str, output_notebook_path: str = ""):
    with open(input_notebook_path, 'r') as in_file:
        nb = load(in_file)
    
    for index, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "code":
            nb["cells"][index]["source"] = [] 

    if not output_notebook_path:
        output_notebook_path = f"{input_notebook_path.replace('.ipynb', '')}_blank.ipynb"
    with open(output_notebook_path, 'w') as out_file:
        dump(nb, out_file, indent=1)

# clear_code_blocks('other_examples/loops_strings.ipynb')