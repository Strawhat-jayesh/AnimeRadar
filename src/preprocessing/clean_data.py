import ast
df['genres'] = df['genres'].apply(ast.literal_eval)