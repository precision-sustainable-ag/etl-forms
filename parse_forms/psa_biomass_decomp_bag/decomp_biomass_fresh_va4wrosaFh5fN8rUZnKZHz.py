data = [
    {
        "ignore_empty_forms": True,
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
                "kobo_names": ["group_000/fresh_bag_wt_grams_000"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_000/barcode_bag_000", "group_000/fresh_bag_wt_grams_000"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
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
                "kobo_names": ["group_001/fresh_bag_wt_grams_001"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_001/barcode_bag_001", "group_001/fresh_bag_wt_grams_001"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
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
                "kobo_names": ["group_002/fresh_bag_wt_grams_002"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_002/barcode_bag_002", "group_002/fresh_bag_wt_grams_002"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
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
                "kobo_names": ["group_003/fresh_bag_wt_grams_003"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_003/barcode_bag_003", "group_003/fresh_bag_wt_grams_003"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
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
                "kobo_names": ["group_004/fresh_bag_wt_grams_004"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_004/barcode_bag_004", "group_004/fresh_bag_wt_grams_004"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
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
                "kobo_names": ["group_005/fresh_bag_wt_grams_005"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_005/barcode_bag_005", "group_005/fresh_bag_wt_grams_005"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
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
                "kobo_names": ["group_006/fresh_bag_wt_grams_006"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_006/barcode_bag_006", "group_006/fresh_bag_wt_grams_006"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
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
                "kobo_names": ["group_007/fresh_bag_wt_grams_007"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_007/barcode_bag_007", "group_007/fresh_bag_wt_grams_007"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_008/barcode_bag_008"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_008/fresh_bag_wt_grams_008"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_008/barcode_bag_008", "group_008/fresh_bag_wt_grams_008"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_009/barcode_bag_009"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_009/fresh_bag_wt_grams_009"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_009/barcode_bag_009", "group_009/fresh_bag_wt_grams_009"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_010/barcode_bag_010"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_010/fresh_bag_wt_grams_010"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_010/barcode_bag_010", "group_010/fresh_bag_wt_grams_010"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_011/barcode_bag_011"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_011/fresh_bag_wt_grams_011"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_011/barcode_bag_011", "group_011/fresh_bag_wt_grams_011"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_012/barcode_bag_012"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_012/fresh_bag_wt_grams_012"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_012/barcode_bag_012", "group_sub2_012/fresh_bag_wt_grams_012"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_013/barcode_bag_013"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_013/fresh_bag_wt_grams_013"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_013/barcode_bag_013", "group_sub2_013/fresh_bag_wt_grams_013"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_014/barcode_bag_014"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_014/fresh_bag_wt_grams_014"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_014/barcode_bag_014", "group_sub2_014/fresh_bag_wt_grams_014"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_015/barcode_bag_015"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_015/fresh_bag_wt_grams_015"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_015/barcode_bag_015", "group_sub2_015/fresh_bag_wt_grams_015"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_016/barcode_bag_016"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_016/fresh_bag_wt_grams_016"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_016/barcode_bag_016", "group_sub2_016/fresh_bag_wt_grams_016"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_017/barcode_bag_017"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_017/fresh_bag_wt_grams_017"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_017/barcode_bag_017", "group_sub2_017/fresh_bag_wt_grams_017"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_018/barcode_bag_018"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_018/fresh_bag_wt_grams_018"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_018/barcode_bag_018", "group_sub2_018/fresh_bag_wt_grams_018"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_019/barcode_bag_019"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_019/fresh_bag_wt_grams_019"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_019/barcode_bag_019", "group_sub2_019/fresh_bag_wt_grams_019"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_020/barcode_bag_020"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_020/fresh_bag_wt_grams_020"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_020/barcode_bag_020", "group_sub2_020/fresh_bag_wt_grams_020"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_021/barcode_bag_021"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_021/fresh_bag_wt_grams_021"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_021/barcode_bag_021", "group_sub2_021/fresh_bag_wt_grams_021"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_022/barcode_bag_022"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_022/fresh_bag_wt_grams_022"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_022/barcode_bag_022", "group_sub2_022/fresh_bag_wt_grams_022"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
    {
        "ignore_empty_forms": True,
        "cols_from_form": [
            {
                "kobo_names": ["group_sub2_023/barcode_bag_023"],
                "db_names": ["code", "subplot", "subsample", "time"],
                "separator": "-",
                "indices": [0, 1, 2, 3],
                "tests": ["check_regex  ^[A-Z0-9]{3}-[12]-[AB]-[0-5]$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_sub2_023/fresh_bag_wt_grams_023"],
                "db_names": ["fresh_biomass_wt"],
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
        "completeness_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"],
        "completeness_errs": ["group_sub2_023/barcode_bag_023", "group_sub2_023/fresh_bag_wt_grams_023"],
        "completeness_err_message": "Barcode is malformed or missing fresh bag weight",
        "all_cols": ["code", "subplot", "subsample", "time", "fresh_biomass_wt"]
    },
]
