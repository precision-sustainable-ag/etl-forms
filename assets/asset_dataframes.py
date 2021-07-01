import pandas as pd

empty_dataframe = pd.DataFrame()

asset_dataframes = {
    "psa gps": {    
        "gps__gps": empty_dataframe
    },
    "psa water sensor install": {
        "water_sensor_install__wsensor_install": empty_dataframe
    },
    "psa decomp bag pre wt": {
        "decomp_biomass_fresh__decomp_bag_pre_wt": empty_dataframe
    },
    "psa decomp bag dry wt": {
        "decomp_biomass_dry__decomp_bag_dry_wt": empty_dataframe
    },
    "psa decomp bag collect": {
        "decomp_biomass_dry__decomp_bag_collect": empty_dataframe
    },
    "psa biomass decomp bag": {
        "biomass_in_field__biomass_decomp_bag": empty_dataframe,
        "decomp_biomass_fresh__biomass_decomp_bag": empty_dataframe
    }
}