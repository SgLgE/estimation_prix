import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

data = {
    'poids': [0.5, 1.0, 1.5, 2.0, 2.5],
    'prix': [5, 10, 15, 20, 25]
}
df = pd.DataFrame(data)

X = df[['poids']]
y = df['prix']

model = LinearRegression()
model.fit(X, y)

save_path = os.path.join('estimation', 'model.pkl')

with open(save_path, 'wb') as f:
    pickle.dump(model, f)

print(f"✅ Modèle entraîné et sauvegardé sous {save_path}")
