import pkg_resources

# Read the requirements file correctly before parsing
with open("requirements.txt", "r") as f:
    content = f.read().splitlines()

requirements = [pkg_resources.Requirement.parse(r) for r in content if r and not r.startswith("#")]

missing = [str(req) for req in requirements if not pkg_resources.working_set.find(req)]

if missing:
    print("❌ Missing packages:", missing)
else:
    print("✅ All packages are installed correctly.")

import subprocess, sys

if missing:
    print("❌ Missing packages:", missing)
    subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
else:
    print("✅ All packages are installed correctly.")
