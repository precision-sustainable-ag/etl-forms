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
                "kobo_names": ["intro_group/biomass_only"],
                "db_names": ["biomass_only"],
                "tests": ["check_if_value_equals  biomass_only"],
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
            {"name": "in_field_biomass", "value": 1},
            {"name": "decomp_biomass", "value": 0},
        ],
        "all_cols": ["code", "biomass_only"],
    },
]
