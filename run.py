import pandas as pd

df = pd.read_csv('data/COD-all.csv')
datasets = df[['package_id','organisation_name','package_title','package_has_admin_boundary_tag','package_tag_list','package_has_cod_tag','package_author','package_caveats','package_dataset_date','package_total_res_downloads','package_methodology','package_creator','package_notes','package_num_resources','package_tracking_summary_total','package_dataset_source','package_locations_list']]

downloads = pd.read_csv('data/COD-Downloads.csv')
downloadStats = pd.merge(left=downloads, right=datasets, how='left', left_on='dataset_name', right_on='package_title')

views = pd.read_csv('data/COD-pageviews.csv')
viewStats = pd.merge(left=views, right=datasets, how='left', left_on='dataset_name', right_on='package_title')


downloadStats.to_csv('data/downloadStats.csv')
viewStats.to_csv('data/viewStats.csv')
