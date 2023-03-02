import subprocess

subprocess.run("python3 ABS_process.py & python3 Hydraulic_modulator.py & python3 Gateway.py", shell=True)