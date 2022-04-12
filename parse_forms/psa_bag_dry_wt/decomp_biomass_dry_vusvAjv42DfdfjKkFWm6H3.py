data = [
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_000/barcode_bag_000"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_000/dry_bag_wt_grams_000"],
                "db_names": ["dry_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["group_000/barcode_bag_000", "group_000/dry_bag_wt_grams_000"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        # {'code': 'SRT', 'subplot': '2', 'subsample': 'A', 'time': '0', 'empty_bag_wt': '146.92', 'notes': None, 'submitted_by': 'al_psa'}
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
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
                "kobo_names": ["group_001/dry_bag_wt_grams_001"],
                "db_names": ["dry_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["group_001/barcode_bag_001", "group_001/dry_bag_wt_grams_001"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
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
                "kobo_names": ["group_002/dry_bag_wt_grams_002"],
                "db_names": ["dry_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["group_002/barcode_bag_002", "group_002/dry_bag_wt_grams_002"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
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
                "kobo_names": ["group_003/dry_bag_wt_grams_003"],
                "db_names": ["dry_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["group_003/barcode_bag_003", "group_003/dry_bag_wt_grams_003"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
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
                "kobo_names": ["group_004/dry_bag_wt_grams_004"],
                "db_names": ["dry_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["group_004/barcode_bag_004", "group_004/dry_bag_wt_grams_004"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_005/barcode_bag_005"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_005/dry_bag_wt_grams_005"],
                "db_names": ["dry_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["group_005/barcode_bag_005", "group_005/dry_bag_wt_grams_005"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_006/barcode_bag_006"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_006/dry_bag_wt_grams_006"],
                "db_names": ["dry_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["group_006/barcode_bag_006", "group_006/dry_bag_wt_grams_006"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_007/barcode_bag_007"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_007/dry_bag_wt_grams_007"],
                "db_names": ["dry_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["group_007/barcode_bag_007", "group_007/dry_bag_wt_grams_007"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
]
