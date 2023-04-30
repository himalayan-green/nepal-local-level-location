import pandas as pd
import sys

provinces = pd.read_csv('provinces.csv')
districts = pd.read_csv('districts.csv')

if len(sys.argv) > 1 and sys.argv[1].lower() == 'nepali':
    local_level = pd.read_csv('local_level_nepali.csv')
else:
    local_level = pd.read_csv('local_level.csv')

def combine_data(rename_column=True):
    local_level_with_district = pd.merge(local_level,
                                         districts,
                                         on='district_id',
                                         how='left')
    local_level_with_district_and_province = pd.merge(
        local_level_with_district, provinces, on='province_id', how='left')
    local_level_with_district_and_province.drop(
        ['district_id', 'province_id'],
        axis=1,
        inplace=True,
    )
    if rename_column:
        local_level_with_district_and_province.rename(
            columns={
                'district_name': 'District',
                'province_name': 'Province',
                'local_level_name': 'Local Level',
                'local_level_id': 'S.N.'
            },
            inplace=True,
        )
    return local_level_with_district_and_province


def write_to_csv(combined):
    combined.to_csv('combined.csv', index=False)


def write_to_json(combined):
    # Write from dataframe to JSON
    combined.to_json('combined.json', orient='records')


if __name__ == '__main__':
    combined = combine_data(rename_column=False)
    write_to_csv(combined)
    write_to_json(combined)
