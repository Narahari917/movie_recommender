# 🎬 Movie Recommender System

A content-based movie recommendation system built with Python and Streamlit. Select any movie from the TMDB dataset and instantly get 5 similar recommendations — complete with posters fetched live from the TMDB API.

---

## 🔍 Overview

This project uses **content-based filtering** with **cosine similarity** to find movies similar to a user's selection. The similarity matrix is precomputed from TMDB movie metadata (genres, cast, crew, keywords, overview) and serialized for fast lookup at runtime. The Streamlit frontend makes the system fully interactive with a dropdown selector and one-click recommendations.

---

## 🏗️ Project Structure

```
movie_recommender/
├── app.py                      # Streamlit web app — UI and recommendation logic
├── movie_recommender.ipynb     # Data processing, feature engineering, similarity matrix generation
├── files/
│   ├── movies_list.pickle      # Serialized movie titles and IDs
│   └── similarity.pickle       # Precomputed cosine similarity matrix
├── setup.py                    # Package setup
├── requirements.txt            # Dependencies
└── README.md
```

---

## ⚙️ Tech Stack

- **Language:** Python
- **Web App:** Streamlit
- **ML / Similarity:** scikit-learn (cosine similarity), NumPy, Pandas
- **Data Processing:** Jupyter Notebook
- **Model Serialization:** Pickle
- **External API:** TMDB API (for movie poster fetching)
- **Dataset:** [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) via Kaggle

---

## 🧠 How It Works

**Notebook (`movie_recommender.ipynb`):**
1. Loads and merges TMDB movies and credits datasets
2. Extracts and preprocesses key features: genres, keywords, cast, crew, overview
3. Combines features into a single text tag per movie
4. Vectorizes tags using CountVectorizer and computes a cosine similarity matrix
5. Serializes the movie list and similarity matrix as `.pickle` files

**App (`app.py`):**
1. Loads the precomputed `movies_list.pickle` and `similarity.pickle` at startup
2. User selects a movie from a dropdown of all available titles
3. On clicking "Show Recommendations", the app finds the top 5 most similar movies by cosine similarity score
4. Fetches and displays movie posters for each recommendation via the TMDB API

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Narahari917/movie_recommender.git
cd movie_recommender
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Get a TMDB API key

Sign up at [https://www.themoviedb.org/](https://www.themoviedb.org/) and generate a free API key. Add it to `app.py` in the `fetch_poster()` function.

### 4. Generate the pickle files

Open and run all cells in `movie_recommender.ipynb` to produce `files/movies_list.pickle` and `files/similarity.pickle`.

> You will need to download the TMDB dataset from Kaggle first:
> [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

### 5. Launch the Streamlit app

```bash
streamlit run app.py
```

Open the URL shown in the terminal (typically `http://localhost:8501`) to use the recommender.

---

## 📊 System Details

| Component | Details |
|---|---|
| Approach | Content-based filtering |
| Similarity Metric | Cosine similarity |
| Feature Source | Genres, keywords, cast, crew, overview |
| Vectorization | CountVectorizer (bag of words) |
| Recommendations | Top 5 most similar movies |
| Poster Source | TMDB API |

---

## 🔮 Future Improvements

- Add collaborative filtering for user-personalized recommendations
- Integrate user ratings for hybrid recommendation approach
- Deploy to Streamlit Cloud or Hugging Face Spaces for public access
- Add genre and year filters to refine recommendations
- Cache TMDB API responses to reduce latency

---

## 👨‍💻 Author

**Narahari Kommi**
[LinkedIn](https://www.linkedin.com/in/naraharikommi/) | [GitHub](https://github.com/Narahari917)
