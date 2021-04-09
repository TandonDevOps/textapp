import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Read version number from env var?
# Keep it in a file?
setuptools.setup(
    name="textapp",
    version="0.0.1",
    author="Gene Callahan",
    author_email="gcallah@mac.com",
    description="Create simple but useful terminal menus.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TandonDevOps/textapp",
    packages=['textapp'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
