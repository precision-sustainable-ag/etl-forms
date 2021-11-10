data = [
    {
        "entry_to_iterate": "group_code_field_history",
        "cols_from_form": [
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
                "kobo_name": "WON'T BE FOUND",
                "db_names": ["notes"],
            },
        ],  
        "all_cols": [
            "previous_cash_crop", 
            "cc_planting_method", 
            "cc_termination_method", 
            "cc_planting_date", 
            "cc_total_rate",
        ],
    }
]