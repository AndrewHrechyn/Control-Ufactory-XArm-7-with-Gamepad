import pyyaml

def load_config(path):
    with open(path, "r") as f:
        return pyyaml.load(f, Loader=pyyaml.Loader)

def save_config(config, path):
    with open(path, "w") as f:
        pyyaml.dump(config, f)
    print(f"Config saved to {path}")
