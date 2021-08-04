data = [
    {
        "cols_from_form": [
            {
                "kobo_name": "What_is_your_Farm_Code",
                "db_names": ["code"],
                "tests": ["not_null", "check_regex ^[A-Z0-9]{3}$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "In_which_subplot_are_ur_sensors_installed",
                "db_names": ["subplot"],
                "multi_select": {
                    "subplot_1": 1,
                    "subplot_2": 2
                }
            },
            {
                "kobo_name": "Scan_the_barcode_on_side_of_your_Gateway",
                "db_names": ["gateway_serial_no"],
                "tests": ["not_null", "check_regex ^210[0-9]{5}$"],
            },
            {
                "kobo_name": "Scan_your_bare_node",
                "db_names": ["bare_node_serial_no"],
                "tests": ["not_null", "check_regex ^180[0-9]{5}$"],
            },
            {
                "kobo_name": "Scan_your_cover_crop_node",
                "db_names": ["cover_node_serial_no"],
                "tests": ["not_null", "check_regex ^180[0-9]{5}$"],
            },
            {
                "kobo_name": "What_day_did_you_install_the_sensors",
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
                "kobo_name": "What_is_the_GPS_loca_on_of_your_bare_node",
                "db_names": ["bare_lat", "bare_lon"],
                "separator": " ",
                "indices": [0,1],      
            },
            {
                "kobo_name": "What_is_the_GPS_loca_your_cover_crop_node",
                "db_names": ["cover_lat", "cover_lon"],
                "separator": " ",
                "indices": [0,1],      
            },
        ],
        # "completeness_cols": ["bare_node_serial_no", "cover_node_serial_no"],
        "all_cols": ["code", "subplot", "gateway_serial_no", "bare_node_serial_no", "cover_node_serial_no", "time_begin", "bare_lon", "bare_lat", "cover_lon", "cover_lat"]
    }
]