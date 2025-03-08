import subprocess

try:
    # Listar archivos en directorio actual
    result = subprocess.run(
        "dir",
        shell=True,
        capture_output=True,
        text=True,
        check=True
    )
    print("Command output:\n", result.stdout)
except subprocess.CalledProcessError as e:
    print("An error occurred while running the command:", e)


import subprocess

try:
    result = subprocess.run(
        "echo Hello, World!",
        shell=True,
        capture_output=True,
        text=True,
        check=True
    )
    print("Output:", result.stdout.strip())
except subprocess.CalledProcessError as e:
    print("An error occurred:", e)