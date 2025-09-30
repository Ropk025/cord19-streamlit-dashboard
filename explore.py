import pandas as pd

# Load only the first 5000 rows to avoid memory error
df = pd.read_csv('data/metadata.csv', low_memory=False, nrows=5000)

print("✅ Sample loaded successfully!")
print("📊 Shape of the dataset:", df.shape)
print(df.head())
print("\n🔍 Missing values per column:")
print(df.isnull().sum().sort_values(ascending=False))
print("\n📋 Column info:")
print(df.info())
print("\n🔍 Missing values per column:")
print(df.isnull().sum().sort_values(ascending=False))
print("\n🧪 Sample titles and publish dates:")
print(df[['title', 'publish_time']].head())
# Drop columns with 100% missing values
df.drop(columns=['who_covidence_id', 'arxiv_id', 's2_id', 'mag_id'], inplace=True)

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract publication year
df['year'] = df['publish_time'].dt.year

# Create abstract word count column
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(str(x).split()) if pd.notnull(x) else 0)

# Preview cleaned data
print("\n🧼 Cleaned dataset preview:")
print(df[['title', 'publish_time', 'year', 'abstract_word_count']].head())

# Save cleaned sample for reuse
df.to_csv('data/metadata_cleaned.csv', index=False)
print("\n✅ Cleaned dataset saved as metadata_cleaned.csv")
df.to_csv('data/metadata_sample.csv', index=False)



