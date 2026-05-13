import subprocess

notebooks = [
    "3_Deep_NN/4_1_Composing_Networks.ipynb",
    "2_Shallow_Networks/3_1_Shallow_Networks_I.ipynb",
    "5_Fitting/6_2_Gradient_Descent.ipynb",
    "5_Fitting/6_1_Line_Search.ipynb",
    "5_Fitting/6_5_Adam.ipynb",
    "5_Fitting/6_3_Stochastic_Gradient_Descent.ipynb",
    "5_Fitting/6_4_Momentum.ipynb",
    "6_Backpropagation/7_2_Backpropagation.ipynb"
]

for nb in notebooks:
    print(f"Running {nb}...")
    try:
        subprocess.run(
            ["uv", "run", "python3", "-m", "jupyter", "nbconvert", "--execute", "--inplace", nb],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"  SUCCESS: {nb}")
    except subprocess.CalledProcessError as e:
        print(f"  FAILED: {nb}")
        print(f"  ERROR: {e.stderr.strip().split(chr(10))[-10:]}")
