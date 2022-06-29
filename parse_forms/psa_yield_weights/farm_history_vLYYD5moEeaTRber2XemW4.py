data = [
    {
        "cols_from_form": [
            {
                "kobo_names": ["group_000/code"],
                "db_names": ["code"],
                "tests": ["not_null", "check_regex  ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_000/date"],
                "db_names": ["cash_crop_harvest_date"],
                "datatype": "date",
            },
            {
                "kobo_names": ["begin_group_WpWlBMQcF/crop"],
                "db_names": ["next_cash_crop"],
                "multi_select": {
                    "corn": "Corn",
                    "soybean": "Soybeans",
                    "cotton": "Cotton",
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
        "all_cols": ["code", "cash_crop_harvest_date", "next_cash_crop"],
    },
]
