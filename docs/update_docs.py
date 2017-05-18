import subprocess


with open('sources/tools.md', 'w') as f:
    subprocess.call(['python', 'argparse_to_md.py', '../tools/'], stdout=f)

subprocess.call(['python', 'ipynb2markdown.py', '--ipynb',
                 'sources/workflow/80698_mol2.ipynb'])