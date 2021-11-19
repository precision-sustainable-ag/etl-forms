info = {
    "gps_corners__gps": {    
        "values_from_table": ["latitude", "longitude"],
        "unique_cols": ["code", "subplot", "treatment", "corner_index"],
        "mode": "update",
    },
    "wsensor_install__water_sensor_install": {
        "all_rows": ["subplot", "code", "gateway_serial_no", "bare_node_serial_no", "cover_node_serial_no", "time_begin", "bare_lon", "bare_lat", "cover_lon", "cover_lat"],
        "mode": "insert",
    },
    "decomp_biomass_fresh__decomp_bag_pre_wt": {
        "values_from_table": ["empty_bag_wt"],
        "unique_cols": ["code", "subplot", "subsample", "time"],
        "mode": "update",
    },
    "decomp_biomass_fresh__biomass_decomp_bag": {
        "values_from_table": ["fresh_biomass_wt"],
        "unique_cols": ["code", "subplot", "subsample", "time"],
        "mode": "update",
    },
    "decomp_biomass_dry__decomp_bag_dry_wt": {
        "values_from_table": ["dry_biomass_wt"],
        "unique_cols": ["code", "subplot", "subsample", "time"],
        "mode": "update",
    },
    "decomp_biomass_dry__decomp_bag_collect": {
        "values_from_table": ["recovery_date"],
        "unique_cols": ["code", "subplot", "subsample", "time"],
        "mode": "update",
    },
    "biomass_in_field__biomass_decomp_bag": {
        "values_from_table": ["fresh_wt_a", "fresh_wt_b", "bag_wt_a", "bag_wt_b", "legumes_40"],
        "unique_cols": ["code", "subplot"],
        "mode": "update",
    },
    "social_sciences_survey__farm_history_survey": {
        "all_rows": [
            "submitted_at",
            "producer_id",
            "crop_acres", 
            "farm_crop_rotation", 
            "cover_crop_acres", 
            "cover_crop_acres_terminated", 
            "cover_crop_acres_typical",
            "first_year_cover_crop", 
            "every_year", 
            "cover_crop_rotation", 
            "favorite_winter_cover_crop", 
            "insured_acres", 
            "removed_insurance", 
            "if_yes_remove_insurance_note", 
            "claim_cover_crop", 
            "if_yes_claim_note", 
            "tilled_acres",
            "farm_tillage_type", 
            "tillage_it_depends", 
            "previous_tillage", 
            "years_since_tillage",
            "tilled_acres_cover_crop", 
            "tillage_type_cover_crop", 
            "tillage_cover_crop_it_depends", 
            "previous_tillage_cover_crop",
            "years_since_tillage_cover_crop",
            "info_sources", 
            "dst_use", 
            "software_use", 
            "devices_use",
            "yield_monitor",
            "sharing_comfort_yield_monitor", 
            "percent_rented", 
            "why_participating",
        ],
        "mode": "insert",
    },
    "farm_history__farm_history_survey": {
        "values_from_table": [
            "previous_cash_crop", 
            "cc_planting_method", 
            "cc_termination_method", 
            "cc_planting_date", 
            "cc_total_rate",
            "total_n_previous_crop",
            "post_harvest_fertility",
            "cash_crop_variety",
            "cash_crop_maturity_group",
        ],
        "unique_cols": ["code"],
        "mode": "update",
    },
    "biomass_in_field__biomass_decomp_bag": {
        "values_from_table": ["fresh_wt_a", "fresh_wt_b", "bag_wt_a", "bag_wt_b", "legumes_40"],
        "unique_cols": ["code", "subplot"],
        "mode": "update",
    },
}