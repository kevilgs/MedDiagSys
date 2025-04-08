import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


# Load datasets
df_comb = pd.read_csv(r'C:\Users\Kevil\Downloads\MDS\data\dis_sym_dataset_comb.csv')
df_norm = pd.read_csv(r'C:\Users\Kevil\Downloads\MDS\data\dis_sym_dataset_norm.csv')

# Print column names to check what's actually in the datasets
print("df_comb columns:", df_comb.columns.tolist())
print("df_norm columns:", df_norm.columns.tolist())

# Based on the column names from the print statement, set the disease column name
# Common variations might be 'label_dis', 'label-dis', 'Disease', etc.
# Let's assume it's 'label_dis' for now - update this based on the printed column names
disease_column = 'label_dis'  # Update this after seeing the printed columns

# Prepare df_comb for merging
df_comb_melted = df_comb.melt(id_vars=[disease_column], var_name='Symptom', value_name='Present')
df_comb_filtered = df_comb_melted[df_comb_melted['Present'] == 1].copy()
df_comb_filtered['Disease'] = df_comb_filtered[disease_column]

# Prepare df_norm for merging
df_norm_melted = df_norm.melt(id_vars=[disease_column], var_name='Symptom', value_name='Present')
df_norm_filtered = df_norm_melted[df_norm_melted['Present'] == 1].copy()
df_norm_filtered['Disease'] = df_norm_filtered[disease_column]

# Combine both datasets
combined_df = pd.concat([df_comb_filtered[['Symptom','Disease']], df_norm_filtered[['Symptom', 'Disease']]], ignore_index=True)

# Filter out classes with fewer than a certain number of samples
class_distribution = combined_df['Disease'].value_counts()
min_samples = 5
classes_to_keep = class_distribution[class_distribution >= min_samples].index
filtered_df = combined_df[combined_df['Disease'].isin(classes_to_keep)].copy()

# Encode symptoms and diseases
symptom_encoder = LabelEncoder()
disease_encoder = LabelEncoder()

filtered_df['Symptom_Encoded'] = symptom_encoder.fit_transform(filtered_df['Symptom'])
filtered_df['Disease_Encoded'] = disease_encoder.fit_transform(filtered_df['Disease'])

# Create feature matrix X and target vector y
X = pd.get_dummies(filtered_df['Symptom_Encoded'])
y = filtered_df['Disease_Encoded']

# Optional: Limit the number of features for testing
X = X.iloc[:, :100]  # Only keep the first 100 features for quicker testing

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)  # Reduced test size

# Function to evaluate model
def evaluate_model(model, X_train, y_train, X_test, y_test, model_name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{model_name} Accuracy: {accuracy:.4f}")

# Initialize and evaluate models
evaluate_model(MultinomialNB(), X_train, y_train, X_test, y_test, "Naive Bayes")
evaluate_model(DecisionTreeClassifier(class_weight='balanced', random_state=42), X_train, y_train, X_test, y_test, "Decision Tree")
evaluate_model(RandomForestClassifier(class_weight='balanced', random_state=42), X_train, y_train, X_test, y_test, "Random Forest")
evaluate_model(LogisticRegression(max_iter=500, random_state=42), X_train, y_train, X_test, y_test, "Logistic Regression")