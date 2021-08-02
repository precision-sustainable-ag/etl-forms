data = [
    {
        "cols_from_form": [
            {
                "kobo_name": "farm_info_group/code",
                "db_names": ["code"],
                "tests": ["not_null", "check_regex ^[A-Z0-9]{3}$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "barcode_gateway",
                "db_names": ["gateway_serial_no"],
            },
            {
                "kobo_name": "group_uv9yg82/bare_node_rep1",
                "db_names": ["bare_node_serial_no"],
            },
            {
                "kobo_name": "group_uv9yg82/cover_crop_node_rep1",
                "db_names": ["cover_node_serial_no"],
            },
            {
                "kobo_name": "farm_info_group/date_install",
                "db_names": ["time_begin"],
                "datatype": "date",
            },
            {
                "kobo_name": "Any_issues_to_report_about_your_sensors",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
            {
                "kobo_name": "group_uv9yg82/gps_bare_node_rep1",
                "db_names": ["bare_lat", "bare_lon"],
                "separator": " ",
                "indices": [0,1],       
            },
            {
                "kobo_name": "group_uv9yg82/gps_cover_crop_node_rep1",
                "db_names": ["cover_lat", "cover_lon"],
                "separator": " ",
                "indices": [0,1],       
            },
        ],
        "extra_cols": [
            {"name": "subplot", "value": 1}
        ],
        "completeness_cols": ["bare_node_serial_no", "cover_node_serial_no"],
        "all_cols": ["code", "subplot", "gateway_serial_no", "bare_node_serial_no", "cover_node_serial_no", "time_begin", "bare_lon", "bare_lat", "cover_lon", "cover_lat"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "farm_info_group/code",
                "db_names": ["code"],
                "tests": ["not_null", "check_regex ^[A-Z0-9]{3}$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            # {
            #     "kobo_name": "In_which_subplot_are_ur_sensors_installed",
            #     "db_names": ["subplot"],
            #     "separator": "_",
            #     "indices": [1],
            #     "tests": None,
            #     "conversions": [],
            # },
            {
                "kobo_name": "barcode_gateway",
                "db_names": ["gateway_serial_no"],
            },
            {
                "kobo_name": "group_uv9yg82/bare_node_rep2",
                "db_names": ["bare_node_serial_no"],
            },
            {
                "kobo_name": "group_uv9yg82/cover_crop_node_rep2",
                "db_names": ["cover_node_serial_no"],
            },
            {
                "kobo_name": "farm_info_group/date_install",
                "db_names": ["time_begin"],
                "datatype": "date",
            },
            {
                "kobo_name": "Any_issues_to_report_about_your_sensors",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
            {
                "kobo_name": "group_uv9yg82/gps_bare_node_rep2",
                "db_names": ["bare_lat", "bare_lon"],
                "separator": " ",
                "indices": [0,1],        
            },
            {
                "kobo_name": "group_uv9yg82/gps_cover_crop_node_rep2",
                "db_names": ["cover_lat", "cover_lon"],
                "separator": " ",
                "indices": [0,1],        
            },
        ],
        "extra_cols": [
            {"name": "subplot", "value": 2}
        ],
        "completeness_cols": ["bare_node_serial_no", "cover_node_serial_no"],
        "all_cols": ["code", "subplot", "gateway_serial_no", "bare_node_serial_no", "cover_node_serial_no", "time_begin", "bare_lon", "bare_lat", "cover_lon", "cover_lat"]
    },
]