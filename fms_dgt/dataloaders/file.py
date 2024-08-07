# Standard
from typing import Any, Dict
import json
import os

# Third Party
import yaml

# Local
from fms_dgt.base.dataloader import DATA_PATH_KEY
from fms_dgt.base.registry import register_dataloader
from fms_dgt.dataloaders.default import DefaultDataloader


@register_dataloader("file")
class FileDataloader(DefaultDataloader):
    """Class for all json datasets"""

    def __init__(self, data_path: str = None) -> None:

        assert f"{DATA_PATH_KEY} must be set in dataloader specification"
        if data_path.endswith(".json"):
            with open(data_path, "r") as f:
                data = json.load(f)
        elif data_path.endswith(".yaml"):
            with open(data_path, "r") as f:
                data = list(yaml.safe_load(f))

        assert type(data) == list, f"Data used for FileDataloader must be a list!"

        super().__init__(data=data)

    def __next__(self):
        return super().__next__()
