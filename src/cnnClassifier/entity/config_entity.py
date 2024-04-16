# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:45:44 2024

@author: mahesh.joshi
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path