import codecs
import sys
import os.path
import glob
import setuptools


with open("README.rst", "r") as fh:
    long_description = fh.read()


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            return line.split('"')[1]
    else:
        raise RuntimeError("Unable to find version string.")


def get_package_name():
    for root, dirs, files in os.walk(os.getcwd()):
        if '__init__.py' in files:
            return os.path.basename(root)
    raise ValueError("No package is found")


package_name = get_package_name()
project_name = package_name.replace("_", "-")
version_name = get_version(os.path.join(package_name, "__init__.py"))


# Get a list of all files in the templates directory
templates_files = glob.glob(f"{package_name}/templates/**/*", recursive=True)
templates_files += glob.glob(f"{package_name}/templates/**/.*", recursive=True)
templates_files = [f for f in templates_files if os.path.isfile(f)]
package_data_files = [os.path.relpath(f, f"{package_name}") for f in templates_files]


def get_short_description(full_description: str):
    old_line = ""
    for line in full_description.splitlines():
        if old_line.startswith("==="):
            return line.strip()
        old_line = line
    return project_name  # By default, short description is package name


# Generate manifest file to including packages
with open("MANIFEST.in", "w") as f:
    f.write(f"recursive-include {package_name}/templates *")


short_description = get_short_description(long_description)
requirements = [line.strip() for line in read("requirements.txt").splitlines() if line.strip()]


setuptools.setup(
    name=project_name,
    version=version_name,
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    license_files=('LICENSE',),
    package_data={
        package_name:
            package_data_files,
    },
    install_requires=requirements,
    python_requires='>=3.9',
)
