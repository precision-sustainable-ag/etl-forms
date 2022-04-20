data = [
    {
        "entry_to_iterate": "group_cj5fy08",
        "top_level_cols": [
            {
                "key": "begin_group_WpWlBMQcF/zero_moisture",
                "db_name": "oven_dried"
            }
        ],
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_cj5fy08/barcode_soy"],
                "db_names": ["code", "treatment", "subplot", "row"],
                "separator": "-",
                "indices": [1, 2, 3, 4],
                "tests": ["check_regex  Y-[A-Z0-9]{3}-[CB]-[12]-(R1|R2)$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_cj5fy08/grain_wt_g_002"],
                "conversions": ["divide_by  1000"],
                "db_names": ["fresh_harvest_wt"],
            },
            {
                "kobo_names": ["group_cj5fy08/moisture_1_002"],
                "db_names": ["moisture_1"],
            },
            {
                "kobo_names": ["group_cj5fy08/test_wt_1_002"],
                "db_names": ["grain_test_1"],
            },
            {
                "kobo_names": ["group_cj5fy08/moisture_2_002"],
                "db_names": ["moisture_2"],
            },
            {
                "kobo_names": ["group_cj5fy08/test_wt_2_002"],
                "db_names": ["grain_test_2"],
            },
            {
                "kobo_names": ["group_cj5fy08/repeat_text_001_001"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "treatment", "subplot", "row", "fresh_harvest_wt"],
        "completeness_errs": ["`group_ng29s00/barcode_corn` is malformed or missing group_cj5fy08/barcode_soy"],
        "all_cols": [
            "code",
            "fresh_harvest_wt",
            "moisture_1",
            "grain_test_1",
            "moisture_2",
            "grain_test_2",
            "oven_dried",
        ],
    }
]
