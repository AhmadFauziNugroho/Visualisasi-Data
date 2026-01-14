import pandas as pd

original_file = './158.-Data-Rincian-APBD-2020.xlsx'
df_original = pd.read_excel(original_file, skiprows=2)

df_original.columns = ['Kodepemda', 'Namapemda', 'standarutama', 'standarjenis', 'Namaakunobjek', 'Nilaianggaran']

df_original['Nilaianggaran'] = pd.to_numeric(df_original['Nilaianggaran'], errors='coerce')

df_original = df_original.dropna(subset=['Nilaianggaran'])

jawa_barat_pemda = [
    'Provinsi Jawa Barat', 'Kab. Bandung', 'Kab. Bekasi', 'Kab. Bogor',
    'Kab. Ciamis', 'Kab. Cianjur', 'Kab. Cirebon', 'Kab. Garut', 'Kab. Indramayu',
    'Kab. Karawang', 'Kab. Kuningan', 'Kab. Majalengka', 'Kab. Purwakarta',
    'Kab. Subang', 'Kab. Sukabumi', 'Kab. Sumedang', 'Kab. Tasikmalaya',
    'Kota Bandung', 'Kota Bekasi', 'Kota Bogor', 'Kota Cirebon', 'Kota Depok',
    'Kota Sukabumi', 'Kota Tasikmalaya', 'Kota Cimahi', 'Kota Banjar',
    'Kab. Bandung Barat', 'Kab. Pangandaran'
]

df_cleaned = df_original[df_original['Namapemda'].isin(jawa_barat_pemda)].copy()

output_file = './Data_APBD_2020_Jawa_Barat_Cleaned.xlsx'
df_cleaned.to_excel(output_file, index=False)

print(f"Cleaned data saved to {output_file}")
print(f"Number of rows in cleaned data: {len(df_cleaned)}")
print(f"Unique Namapemda in cleaned data: {df_cleaned['Namapemda'].unique().tolist()}")