data = [
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_001/barcode_bag_001"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["decomp_bag_collect_date"],
                "db_names": ["recovery_date"],
                "datatype": "date",
                "tests": ["not_null"],
            },
            {
                "kobo_names": ["WON'T BE FOUND"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time"],
        "completeness_errs": ["`group_001/barcode_bag_001` is malformed"],
        # {'code': 'SRT', 'subplot': '2', 'subsample': 'A', 'time': '0', 'empty_bag_wt': '146.92', 'notes': None, 'submitted_by': 'al_psa'}
        "all_cols": ["code", "subplot", "subsample", "time"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_002/barcode_bag_002"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["decomp_bag_collect_date"],
                "db_names": ["recovery_date"],
                "datatype": "date",
                "tests": ["not_null"],
            },
            {
                "kobo_names": ["WON'T BE FOUND"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time"],
        "completeness_errs": ["`group_002/barcode_bag_002` is malformed"],
        "all_cols": ["code", "subplot", "subsample", "time"],
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_003/barcode_bag_003"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["decomp_bag_collect_date"],
                "db_names": ["recovery_date"],
                "datatype": "date",
                "tests": ["not_null"],
            },
            {
                "kobo_names": ["WON'T BE FOUND"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time"],
        "completeness_errs": ["`group_003/barcode_bag_003` is malformed"],
        "all_cols": ["code", "subplot", "subsample", "time"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_004/barcode_bag_004"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["decomp_bag_collect_date"],
                "db_names": ["recovery_date"],
                "datatype": "date",
                "tests": ["not_null"],
            },
            {
                "kobo_names": ["WON'T BE FOUND"],
                "db_names": ["notes"],
            },
            {
                "kobo_names": ["_submitted_by"],
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time"],
        "completeness_errs": ["`group_004/barcode_bag_004` is malformed"],
        "all_cols": ["code", "subplot", "subsample", "time"]
    },
]
