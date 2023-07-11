import toml

with open("pyproject.toml") as fd:
    data = toml.load(fd)


# replace equistore-core @ github with just the package name
assert len(data["project"]["dependencies"]) == 1
assert data["project"]["dependencies"][0].startswith(
    "equistore-core @ https://github.com/lab-cosmo/equistore"
)

data["project"]["dependencies"] = ["equistore-core"]


with open("pyproject.toml", "w") as fd:
    toml.dump(data, fd)
