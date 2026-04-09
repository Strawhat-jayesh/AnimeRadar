rating_threshold = 8.0
popularity_threshold = df['members'].quantile(0.3)

hidden_gems = df[
    (df['score'] >= rating_threshold) &
    (df['members'] <= popularity_threshold)
]

hidden_gems = hidden_gems.sort_values(by='score', ascending=False)

top_hidden_gems = hidden_gems.head(10)

top_hidden_gems[['title','score','members']]
