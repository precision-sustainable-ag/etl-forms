data = [
    {
        "cols_from_form": [
            {
                "kobo_names": ["farm_info_group/code"],
                "db_names": ["code"],
                "tests": ["not_null", "check_regex  ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["farm_info_group/crop_planting_date"],
                "db_names": ["cash_crop_planting_date"],
                "tests": ["not_null"],
                "datatype": "date",
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
        "all_cols": ["code", "cash_crop_planting_date"]
    },
]
