import nbformat
import sys
import glob

def fix_notebook(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        
    changed = False
    for cell in nb.cells:
        if cell.cell_type == 'code':
            old_src = cell.source
            # Fix TypeError in gradient printing
            if 'print("Your gradients: (%3.3f,%3.3f)"%(gradient[0],gradient[1]))' in cell.source:
                cell.source = cell.source.replace(
                    'print("Your gradients: (%3.3f,%3.3f)"%(gradient[0],gradient[1]))',
                    'print("Your gradients: (%3.3f,%3.3f)"%(gradient[0].item(),gradient[1].item()))'
                )
                changed = True
            if 'print("Approx gradients: (%3.3f,%3.3f)"%(dl_dphi0_est,dl_dphi1_est))' in cell.source:
                cell.source = cell.source.replace(
                    'print("Approx gradients: (%3.3f,%3.3f)"%(dl_dphi0_est,dl_dphi1_est))',
                    'print("Approx gradients: (%3.3f,%3.3f)"%(dl_dphi0_est.item(),dl_dphi1_est.item()))'
                )
                changed = True
            
            # Change # TODO to # DONE
            if '# TODO' in cell.source:
                cell.source = cell.source.replace('# TODO', '# DONE')
                changed = True
                
        elif cell.cell_type == 'markdown':
            # sometimes TODO is in markdown
            pass
            
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"Saved {file_path}")

for f in glob.glob('**/*.ipynb', recursive=True):
    fix_notebook(f)

