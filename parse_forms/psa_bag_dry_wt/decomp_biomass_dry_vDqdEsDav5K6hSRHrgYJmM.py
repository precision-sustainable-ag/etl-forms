data = [
    {
        "cols_from_form": [
            {
                "kobo_name": "dry_wt_group/decomp_bag",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "dry_wt_group/dry_wt",
                "db_names": ["dry_biomass_wt"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["dry_wt_group/decomp_bag", "dry_wt_group/dry_wt"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        # {'code': 'SRT', 'subplot': '2', 'subsample': 'A', 'time': '0', 'empty_bag_wt': '146.92', 'notes': None, 'submitted_by': 'al_psa'}
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "dry_wt_group_001/decomp_bag_001",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "dry_wt_group_001/dry_wt_001",
                "db_names": ["dry_biomass_wt"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["dry_wt_group_001/decomp_bag_001", "dry_wt_group_001/dry_wt_001"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "dry_wt_group_002/decomp_bag_002",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "dry_wt_group_002/dry_wt_002",
                "db_names": ["dry_biomass_wt"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["dry_wt_group_002/decomp_bag_002", "dry_wt_group_002/dry_wt_002"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "dry_wt_group_003/decomp_bag_003",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "dry_wt_group_003/dry_wt_003",
                "db_names": ["dry_biomass_wt"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["dry_wt_group_003/decomp_bag_003", "dry_wt_group_003/dry_wt_003"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "dry_wt_group_004/decomp_bag_004",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "dry_wt_group_004/dry_wt_004",
                "db_names": ["dry_biomass_wt"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["dry_wt_group_004/decomp_bag_004", "dry_wt_group_004/dry_wt_004"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "dry_wt_group_005/decomp_bag_005",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "dry_wt_group_005/dry_wt_005",
                "db_names": ["dry_biomass_wt"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["dry_wt_group_005/decomp_bag_005", "dry_wt_group_005/dry_wt_005"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "dry_wt_group_006/decomp_bag_006",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "dry_wt_group_006/dry_wt_006",
                "db_names": ["dry_biomass_wt"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["dry_wt_group_006/decomp_bag_006", "dry_wt_group_006/dry_wt_006"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
    {
        "cols_from_form": [
            {
                "kobo_name": "dry_wt_group_007/decomp_bag_007",
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "dry_wt_group_007/dry_wt_007",
                "db_names": ["dry_biomass_wt"],
            },
            {
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "completeness_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"],
        "completeness_errs": ["dry_wt_group_007/decomp_bag_007", "dry_wt_group_007/dry_wt_007"],
        "completeness_err_message": "Barcode is malformed or missing dry biomass weight",
        "all_cols": ["code", "subplot", "subsample", "time", "dry_biomass_wt"]
    },
]
