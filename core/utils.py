import os
from typing import Final
from pathlib import Path
from core.logging import LoggerFactory

logger_factory = LoggerFactory()
logger = logger_factory.get_logger(__name__)


class FetchFromKaggle:
    def __init__(self, save_path: Final[Path], kaggle_dataset: str):
        from kaggle.api.kaggle_api_extended import KaggleApi

        self.logger = logger
        self.api = KaggleApi()

        self.logger.info("Authenticating with Kaggle API")
        self.api.authenticate()

        self.save_path = save_path / "dataset"
        self._create_download_path()

        self.kaggle_dataset = kaggle_dataset

        self.logger.info(
            "Kaggle connection established. Download path: %s", self.save_path
        )

    def _create_download_path(self) -> None:
        os.makedirs(self.save_path, exist_ok=True)
        self.logger.debug("Dataset directory ensured at %s", self.save_path)

    def download(self) -> None:
        dataset_name = self.kaggle_dataset
        if not dataset_name:
            raise ValueError("KAGGLE_DATASET not found in environment variables")

        self.logger.info("Starting dataset download: %s", dataset_name)

        self.api.dataset_download_files(
            dataset=dataset_name,
            path=self.save_path,
            unzip=True,
            force=True,
        )

        self.logger.info("Dataset downloaded and extracted successfully")
