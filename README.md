# tracker-data-viewer
This repositiory contains a Marimo notebook/app for viewing the tracker and power data from Solar Data Prize site 9068

## Quick start

1. Clone this repository to your computer
2. In a fresh virtual environment, install the packages in [requirements.txt](./requirements.txt)
3. Download two files from the [Solar Data Prize S3 bucket for site 9068](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=pvdaq%2F2023-solar-data-prize%2F9068_OEDI%2Fdata%2F)
  - `9068_ac_power_data.csv`
  - `9068_tracker_data.csv`
4. Put these files in the cloned repository on your computer
5. From the command line in the root of the repository, run `marimo run 9068_data_viewer.py`
