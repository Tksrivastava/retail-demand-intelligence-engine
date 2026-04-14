import pandas as pd
from typing import Final
from pathlib import Path
from core.logging import LoggerFactory
from core.utils import FetchFromKaggle, CustomerEligibilityFilter


logger_factory = LoggerFactory()
logger = logger_factory.get_logger(__name__)


FILE_PATH: Final[Path] = Path(__file__).resolve().parent.parent
DATASET_PATH: Final[Path] = FILE_PATH / "dataset" / "shop-sales-data.csv"
FILTERED_DATASET_PATH: Final[Path] = FILE_PATH / "dataset" / "filtered-sales-data.csv"


if __name__ == "__main__":
    logger.info("Starting shop filtration pipeline")

    logger.info(f"Loading raw transactional data from {DATASET_PATH}", )
    df = pd.read_csv(DATASET_PATH)

    logger.info(f"Raw data loaded | rows={df.shape[0]} | cols={df.shape[1]}")

    logger.info("Applying customer eligibility criteria")
    eligibility_filter = CustomerEligibilityFilter(
        year_col="year",
        month_col="month",
        customer_id_col="shop_id",
        min_tenure_years=1,
        min_avg_active_months_per_year=6
    )
    eligible_customers = eligibility_filter.filter_customers(df=df)
    df = df.loc[df["shop_id"].isin(eligible_customers)].copy()
    logger.info(f"Filtered raw data | rows={df.shape[0]} | cols={df.shape[1]}")

    logger.info(f"Saving filtered dataset to {FILTERED_DATASET_PATH}")
    df.to_csv(FILTERED_DATASET_PATH, index=False)