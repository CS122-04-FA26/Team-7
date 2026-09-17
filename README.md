# Netflix Genre Analyzer
 
**Team Fantastic Four** · CS 122, Fall 2026
 
A Python program that explores how genres relate to each other in Netflix's catalog
and recommends titles based on a user's genre preferences.
 
## Team Members
 
- Isaac Lin
- Zhanxiang He
- Justin Tan
- Ryan Cartwright
## Project Overview
 
Most Netflix titles are tagged with several genres at once, but it's hard to see how
those genres relate to each other. Our project answers two questions:
 
1. Which genre combinations appear together most often on Netflix
   (for example, dramas + romance vs. comedies + romance)?
2. How can those relationships help a viewer find something to watch?
### Planned Features
 
- **Genre combination analysis:** find the most common genre pairings in the catalog
- **Movies vs. TV shows:** compare genre patterns between the two content types
- **Visualizations:** charts of the top genre combinations
- **Recommendations:** suggest titles that match the genres a user selects
## Dataset
 
This project uses the **Netflix Movies and TV Shows** dataset from Kaggle.
 
- **Link:** https://www.kaggle.com/datasets/shivamb/netflix-shows
- **License:** CC0: Public Domain
- **Size:** 8,807 rows, 12 columns, ~3.24 MB
Each row is one movie or TV show available on Netflix as of 2021, with its type, title,
director, cast, country, date added, release year, rating, duration, genres
(`listed_in`), and a short description. The `listed_in` column is the core of this
project, since most titles list more than one genre.
 
The data file is **not** stored in this repository. See
[`data/README.md`](data/README.md) for download instructions.
 
## Setup
 
### 1. Clone the repository
 
```bash
git clone git@github.com:CS122-04-FA26/fantasticfour-netflix-shows.git
cd fantasticfour-netflix-shows
```
 
### 2. Install dependencies
 
**Option A: using [uv](https://docs.astral.sh/uv/)** (recommended)
 
```bash
uv sync
```
 
**Option B: using pip**
 
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
 
### 3. Download the dataset
 
Follow the steps in [`data/README.md`](data/README.md) and place the file at
`data/netflix_titles.csv`.
 
### 4. Check that the data loads
 
```bash
uv run python src/load_data.py
# or, with pip: python src/load_data.py
```
 
You should see `(8807, 12)` followed by the first few rows of the dataset.
 
## Project Structure
 
```
fantasticfour-netflix-shows/
├── data/               # dataset download instructions (data file not committed)
│   └── README.md
├── notebooks/          # exploratory analysis notebooks
├── src/                # Python source code
│   └── load_data.py    # loads the Netflix dataset
├── .gitignore
├── pyproject.toml      # project dependencies (uv)
├── uv.lock
├── requirements.txt    # project dependencies (pip)
└── README.md
```