import pandas as pd

df = pd.read_csv('data/COD-all.csv')
datasets = df[['package_id','package_name','package_has_admin_boundary_tag','package_tag_list','package_has_cod_tag','package_author','package_caveats','package_dataset_date','package_total_res_downloads','package_methodology','package_title','package_creator','organisation_name','package_notes','package_num_resources','package_tracking_summary_total','package_dataset_source','package_locations_list']]

dowloads = pd.read_csv('data/COD-Downloads.csv')
views = pd.read_csv('data/COD-pageviews.csv')
stats = pd.merge(left=dowloads, right=views, how='left', on='dataset_name')

fullstats = pd.merge(left=stats, right=datasets, how='left', left_on='dataset_name', right_on='package_title')
fullstats.to_csv('data/stats.csv')

# df2 = [dowloads, views]
# pagesStats = pd.concat(df2)
# pagesStats.to_csv('data/stats.csv')
