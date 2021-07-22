info = {
    # "gps_corners__gps": {    
    #     "values_from_table": ["latitude", "longitude"],
    #     "unique_cols": ["code", "subplot", "treatment", "corner_index"],
    #     "all_rows": ["code", "subplot", "treatment", "corner_index", "latitude", "longitude"],
    #     "mode": "insert",
    #     "unicity_constraint": None,
    # },
    # "wsensor_install__water_sensor_install": {
    #     "values_from_table": ["time_begin", "bare_lon", "bare_lat", "cover_lon", "cover_lat"],
    #     "unique_cols": ["subplot", "code", "gateway_serial_no", "bare_node_serial_no", "cover_node_serial_no", "time_begin"],
    #     "all_rows": ["subplot", "code", "gateway_serial_no", "bare_node_serial_no", "cover_node_serial_no", "time_begin", "bare_lon", "bare_lat", "cover_lon", "cover_lat"],
    #     "mode": "insert",
    #     "unicity_constraint": "wsensor_install_subplot_code_gateway_serial_no_bare_node_se_key",
    # },
    # "decomp_biomass_fresh__decomp_bag_pre_wt": {
    #     "values_from_table": ["empty_bag_wt"],
    #     "unique_cols": ["code", "subplot", "subsample", "time"],
    #     "mode": "update",
    #     "unicity_constraint": "decomp_biomass_fresh_code_subplot_subsample_time_key",
    # },
    # "decomp_biomass_fresh__biomass_decomp_bag": {
    #     "values_from_table": ["fresh_biomass_wt"],
    #     "unique_cols": ["code", "subplot", "subsample", "time"],
    #     "mode": "update",
    #     "unicity_constraint": "decomp_biomass_fresh_code_subplot_subsample_time_key",
    # },
    # "decomp_biomass_dry__decomp_bag_dry_wt": {
    #     "values_from_table": ["dry_biomass_wt"],
    #     "unique_cols": ["code", "subplot", "subsample", "time"],
    #     "mode": "update",
    #     "unicity_constraint": "decomp_biomass_dry_code_subplot_subsample_time_key",
    # },
    "decomp_biomass_dry__decomp_bag_collect": {
        "values_from_table": ["recovery_date"],
        "unique_cols": ["code", "subplot", "subsample", "time"],
        "mode": "update",
        "unicity_constraint": "decomp_biomass_dry_code_subplot_subsample_time_key",
    },
    # "biomass_in_field__biomass_decomp_bag": {
    #     "values_from_table": ["fresh_wt_a", "fresh_wt_b", "bag_wt_a", "bag_wt_b", "legumes_40"],
    #     "unique_cols": ["code", "subplot"],
    #     "mode": "update",
    #     "unicity_constraint": "biomass_in_field_code_subplot_key",
    # },
}