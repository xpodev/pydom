import sys

package_name = "pydom"

print(f"\033[91mWARNING: This package has been renamed to '{package_name}'. Please install it using:\033[0m")
print(f"\033[92m    pip install {package_name}\033[0m")
sys.exit(1)  # Stop the installation