import toml

with open("pyproject.toml") as fd:
    data = toml.load(fd)


# replace metatensor-core @ github with just the package name
assert len(data["project"]["dependencies"]) == 1
assert data["project"]["dependencies"][0].startswith(
    "metatensor-core @ https://github.com/lab-cosmo/metatensor"
)

data["project"]["dependencies"] = ["metatensor-core"]


with open("pyproject.toml", "w") as fd:
    toml.dump(data, fd)
