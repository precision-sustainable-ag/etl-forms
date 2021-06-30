data = [
    {
        "cols_from_form": [
            {
                "kobo_name": "code",
                "db_names": ["code"],
                "tests": ["not_null", "check_reqex ^[A-Z0-9]{3}$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "fresh_wt_group/fresh_wt_a1",
                "db_names": ["fresh_wt_a"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "fresh_wt_group/fresh_wt_b1",
                "db_names": ["fresh_wt_b"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "empty_bag_group/bag_a1",
                "db_names": ["bag_wt_a"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "empty_bag_group/bag_b1",
                "db_names": ["bag_wt_b"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "You_have_finished_wi_vest_for_PSA_On_Farm/sub1_legume",
                "db_names": ["legumes_40"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "WONT BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
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
                "kobo_name": "code",
                "db_names": ["code"],
                "tests": ["not_null", "check_reqex ^[A-Z0-9]{3}$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "fresh_wt2_group/fresh_wt_a2",
                "db_names": ["fresh_wt_a"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "fresh_wt2_group/fresh_wt_b2",
                "db_names": ["fresh_wt_b"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "bag_2_group/bag_a2",
                "db_names": ["bag_wt_a"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "bag_2_group/bag_b2",
                "db_names": ["bag_wt_b"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "You_have_finished_wi_vest_for_PSA_On_Farm/sub2_legume",
                "db_names": ["legumes_40"],
                "tests": ["not_null"],
            },
            {
                "kobo_name": "WONT BE FOUND",
                "db_names": ["notes"],
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "extra_cols": [
            {"name": "subplot", "value": 1}
        ],
    },
]