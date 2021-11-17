data = [
    {
        "entry_to_iterate": "group_code_field_history",
        "cols_from_form": [
            {
                "kobo_name": "group_code_field_history/code",
                "db_names": ["code"],
                "tests": ["not_null", "check_regex ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "group_code_field_history/previous_crop",
                "db_names": ["previous_cash_crop"],
                "datatype": "date",
            },
            {
                "kobo_name": "group_code_field_history/cover_crop_planting_method",
                "db_names": ["cc_planting_method"],
            },
            {
                "kobo_name": "group_code_field_history/cover_crop_termination",
                "db_names": ["cc_termination_method"],
            },
            {
                "kobo_name": "group_code_field_history/cover_crop_plant_date",
                "db_names": ["cc_planting_date"],
                "datatype": "date",
            },
            {
                "kobo_name": "group_code_field_history/cover_crop_rate_total",
                "db_names": ["cc_total_rate"],
            },
            {
                "kobo_name": "group_code_field_history/previous_fert",
                "db_names": ["total_n_previous_crop"],
            },
            {
                "kobo_name": "group_code_field_history/cover_crop_litter",
                "db_names": ["post_harvest_fertility"],
                "multi_select": {
                    "no": 0,
                    "yes": 1
                },
            },
            {
                "kobo_name": "group_code_field_history/crop_variety",
                "db_names": ["cash_crop_variety"],
            },
            {
                "kobo_name": "group_code_field_history/crop_maturity",
                "db_names": ["cash_crop_maturity_group"],
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
        "all_cols": [
            "previous_cash_crop", 
            "cc_planting_method", 
            "cc_termination_method", 
            "cc_planting_date", 
            "cc_total_rate",
            "total_n_previous_crop",
            "post_harvest_fertility",
            "cash_crop_variety",
            "cash_crop_maturity_group",
        ],
    }
]