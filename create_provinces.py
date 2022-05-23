import pandas as pd


data_source = 'ward_data.csv'

ward_data = pd.read_csv(data_source)

# The CSV is in the given format.
# province_id, district_name, location_name, ward_no

# Create provinces
provinces = ward_data.groupby('province_id')
# Write to file.
for province_index, province_data in provinces:
    province_id = province_data.iloc[0]['province_id']
    print(province_id)
