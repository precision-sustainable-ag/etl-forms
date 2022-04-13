data = [
    {
        "entry_to_iterate": "group_code_field_history",
        "cols_from_form": [
            {
                "kobo_names": ["group_code_field_history/code"],
                "db_names": ["code"],
                "tests": ["not_null", "check_regex  ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_names": ["group_code_field_history/previous_crop"],
                "db_names": ["previous_cash_crop"],
                "multi_select": {
                    "corn": "Corn",
                    "soybean": "Soybeans",
                    "cotton": "Cotton",
                    "wheat_winter": "Winter Wheat",
                    "wheat_spring": "Spring Wheat",
                    "silage_corn": "Silage Corn",
                    "grain_sorghum": "Grain Sorghum",
                    "tobacco": "Tobacco",
                    "oats": "Oats",
                    "barley": "Barley",
                    "peanut": "Peanut",
                    "fallow": "Fallow",
                    "pasture": "Pasture",
                    "livestock": "Livestock",
                    "summer_cover_c": "Summer Cover Crop",
                    "hort": "Horticultural",
                    "other": "Other",
                },
            },
            {
                "kobo_names": ["group_code_field_history/cover_crop_planting_method"],
                "db_names": ["cc_planting_method"],
                "multi_select": {
                    "drilled": "Drilled",
                    "broadcast": "Broadcast",
                    "aerial_seeded": "Aerial Seeding",
                    "other": "Other",
                },
            },
            {
                "kobo_names": ["group_code_field_history/cover_crop_termination"],
                "db_names": ["cc_termination_method"],
                "multi_select": {
                    "herbicide": "Herbicide",
                    "mechanical": "Mechanical",
                    "combination_termination": "Herbicide + Mechanical",
                },
            },
            {
                "kobo_names": ["group_code_field_history/cover_crop_plant_date"],
                "db_names": ["cc_planting_date"],
                "datatype": "date",
            },
            {
                "kobo_names": ["group_code_field_history/cover_crop_rate_total"],
                "db_names": ["cc_total_rate"],
                "datatype": "int",
            },
            {
                "kobo_names": ["group_code_field_history/previous_fert"],
                "db_names": ["total_n_previous_crop"],
            },
            {
                "kobo_names": ["group_code_field_history/cover_crop_litter"],
                "db_names": ["post_harvest_fertility"],
                "multi_select": {
                    "no": 0,
                    "yes": 1
                },
            },
            {
                "kobo_names": ["group_code_field_history/crop_variety"],
                "db_names": ["cash_crop_variety"],
            },
            {
                "kobo_names": ["group_code_field_history/crop_maturity"],
                "db_names": ["cash_crop_maturity_group"],
            },
            {
                "kobo_names": ["group_code_field_history/crop"],
                "db_names": ["next_cash_crop"],
                "multi_select": {
                    "soybean": "Soybeans",
                    "cotton": "Cotton",
                    "corn": "Corn"
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
            "next_cash_crop",
        ],
    }
]
