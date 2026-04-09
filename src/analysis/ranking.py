df['final_score'] = (
    0.6 * df['score'] +
    0.25 * df['members_norm'] +
    0.15 * df['favorites_norm']
)

df[['title','score','members_norm','favorites_norm','final_score']].head()
