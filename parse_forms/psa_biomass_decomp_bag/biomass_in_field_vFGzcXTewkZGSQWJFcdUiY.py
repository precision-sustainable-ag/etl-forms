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
                "kobo_names": ["Fresh_Weights_Rep_1/fresh_wt_a1"],
                "db_names": ["fresh_wt_a"],
            },
            {
                "kobo_names": ["Fresh_Weights_Rep_1/fresh_wt_b1"],
                "db_names": ["fresh_wt_b"],
            },
            {
                "kobo_names": ["Fresh_Weights_Rep_1/bag_a1"],
                "db_names": ["bag_wt_a"],
            },
            {
                "kobo_names": ["Fresh_Weights_Rep_1/bag_b1"],
                "db_names": ["bag_wt_b"],
            },
            {
                "kobo_names": ["group_cc_growth_species/sub1_legume"],
                "db_names": ["legumes_40"],
                "tests": ["not_null"],
                "multi_select": {
                    "less_than_40_legume": 0,
                    "more_than_40_legume": 1
                },
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
        "extra_cols": [
            {"name": "subplot", "value": 1}
        ],
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
                "kobo_names": ["fresh_wt2_group/fresh_wt_a2"],
                "db_names": ["fresh_wt_a"],
            },
            {
                "kobo_names": ["fresh_wt2_group/fresh_wt_b2"],
                "db_names": ["fresh_wt_b"],
            },
            {
                "kobo_names": ["bag_2_group/bag_a2"],
                "db_names": ["bag_wt_a"],
            },
            {
                "kobo_names": ["bag_2_group/bag_b2"],
                "db_names": ["bag_wt_b"],
            },
            {
                "kobo_names": ["group_cc_growth_species/sub2_legume"],
                "db_names": ["legumes_40"],
                "tests": ["not_null"],
                "multi_select": {
                    "less_than_40_legume": 0,
                    "more_than_40_legume": 1
                },
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
        "extra_cols": [
            {"name": "subplot", "value": 2}
        ],
    },
]
