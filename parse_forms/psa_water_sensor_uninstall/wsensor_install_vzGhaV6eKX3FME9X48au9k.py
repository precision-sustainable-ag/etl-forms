data = [
    {
        "cols_from_form": [
            {
                "kobo_names": ["code"],
                "db_names": ["code"],
                "tests": ["not_null", "check_regex  ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["gateway"],
                "db_names": ["gateway_serial_no"],
                "tests": ["check_regex  ^210[0-9]{5}$|^-999$"],
            },
            {
                "kobo_names": ["group_uv9yg82/bare_node_rep1"],
                "db_names": ["bare_node_serial_no"],
                "tests": ["not_null", "check_regex  ^180[0-9]{5}$|^-999$"],
            },
            {
                "kobo_names": ["group_uv9yg82/cover_crop_node_rep1"],
                "db_names": ["cover_node_serial_no"],
                "tests": ["not_null", "check_regex  ^180[0-9]{5}$|^-999$"],
            },
            {
                "kobo_names": ["date_uninstall"],
                "db_names": ["time_end"],
                "datatype": "date",
            },
            {
                "kobo_names": ["issues_gateway", "group_uv9yg82/issues_rep1", "group_uv9yg82/issues_rep2", "issues_sensors"],
                "joiner": " ",
                "add_keys": True,
                "db_names": ["notes_uninstall"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "extra_cols": [
            {"name": "subplot", "value": 1}
        ],
        "completeness_cols": ["bare_node_serial_no", "cover_node_serial_no"],
        "all_cols": ["code", "subplot", "gateway_serial_no", "bare_node_serial_no", "cover_node_serial_no", "time_end"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["code"],
                "db_names": ["code"],
                "tests": ["not_null", "check_regex  ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["gateway"],
                "db_names": ["gateway_serial_no"],
                "tests": ["check_regex  ^210[0-9]{5}$|^-999$"],
            },
            {
                "kobo_names": ["group_uv9yg82/bare_node_rep2"],
                "db_names": ["bare_node_serial_no"],
                "tests": ["not_null", "check_regex  ^180[0-9]{5}$|^-999$"],
            },
            {
                "kobo_names": ["group_uv9yg82/cover_crop_node_rep2"],
                "db_names": ["cover_node_serial_no"],
                "tests": ["not_null", "check_regex  ^180[0-9]{5}$|^-999$"],
            },
            {
                "kobo_names": ["date_uninstall"],
                "db_names": ["time_end"],
                "datatype": "date",
            },
            {
                "kobo_names": ["issues_gateway", "group_uv9yg82/issues_rep1", "group_uv9yg82/issues_rep2", "issues_sensors"],
                "joiner": " ",
                "add_keys": True,
                "db_names": ["notes_uninstall"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "extra_cols": [
            {"name": "subplot", "value": 2}
        ],
        "completeness_cols": ["bare_node_serial_no", "cover_node_serial_no"],
        "all_cols": ["code", "subplot", "gateway_serial_no", "bare_node_serial_no", "cover_node_serial_no", "time_end"]
    },
]
