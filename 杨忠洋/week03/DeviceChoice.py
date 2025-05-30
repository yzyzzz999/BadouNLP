import torch


def get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    else:
        return torch.device("cpu")
