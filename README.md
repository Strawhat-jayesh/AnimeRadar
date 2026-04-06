# AnimeRadar

AnimeRadar is a data-driven project designed to help users discover high-quality seasonal anime and identify hidden gems beyond early hype.  
The system collects anime data using the Jikan API (MyAnimeList API), cleans and processes the dataset, and applies a weighted ranking algorithm to analyze seasonal trends.

Course: DATA 601  
Project: Final Project – AnimeRadar

---

# Project Goal

Every anime season releases 40–60 new titles, making it difficult for viewers to identify high-quality content early. Many platforms rely on raw user ratings which can be biased or unreliable during early release periods.

AnimeRadar aims to:
- Collect seasonal anime data
- Clean and process the dataset
- Apply a weighted ranking formula
- Analyze seasonal trends
- Identify top shows and hidden gems

---
---

# Git Workflow Rules

⚠️ **IMPORTANT: Do NOT commit directly to the `main` branch**

All team members must:

1. Pull the latest changes

```
git pull origin main
```

2. Create your own branch

```
git checkout -b your-name-feature
```

Example:

```
git checkout -b jayesh-api-integration
```

3. Work on your tasks

4. Push your branch

```
git push origin your-name-feature
```

5. Create a **Pull Request** before merging into `main`.

This prevents code conflicts and keeps the repository organized.

---

# Project Tasks

## 1. API Integration
Collect anime data using the Jikan API.

Tasks:
- Connect to Jikan API
- Fetch seasonal anime data
- Extract relevant fields
- Store raw JSON files
- Convert JSON to DataFrame
- Save raw data in `data/raw`

Responsible:
Jayesh

---

## 2. Data Preprocessing
Clean and transform the dataset.

Tasks:
- Handle missing values
- Remove unreleased anime
- Normalize genre labels
- Filter incomplete data
- Export cleaned dataset

Responsible:
Jayesh + Ree

---

## 3. Ranking Algorithm
Implement weighted ranking formula.

Tasks:
- Implement weighted ranking system
- Balance ratings and vote counts
- Generate top anime list

Responsible:
Sai + Apoorva

---

## 4. Hidden Gem Detection
Identify underrated anime.

Tasks:
- Detect high-rated but low-popularity anime
- Implement filtering logic

Responsible:
Sai + Jarred 

---

## 5. Statistical Analysis
Analyze trends and relationships in data.

Tasks:
- Calculate mean, median, standard deviation
- Analyze correlation between ratings and popularity
- Perform trend analysis over seasons

Responsible:
Ree + Apoorva

---

## 6. Visualization
Create charts and visual outputs.

Tasks:
- Top anime charts
- Genre trend graphs
- Rating vs popularity scatter plots

Responsible:
Jayesh.
---

# Technologies Used

Python  
Pandas  
Matplotlib / Seaborn  
Jikan API (MyAnimeList API)

---

# Data Source

Jikan API  
https://jikan.moe

---
