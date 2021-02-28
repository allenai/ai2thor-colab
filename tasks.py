from invoke import task


@task
def set_version(c, version):
    """Writes the version upon a release."""
    for filename in ["setup.py", "ai2thor_colab/__init__.py"]:
        with open(filename, "r") as f:
            file = f.read()
        file = file.replace("<REPLACE_WITH_VERSION>", version)
        with open(filename, "w") as f:
            f.write(file)
