data = [
    {
        "cols_from_form": [
            {
                "kobo_name": "code",
                "db_names": ["code"],
                "tests": ["not_null", "check_regex ^[A-Z0-9]{3}$|^-999$"],
                "conversions": ["strip_whitespace", "to_uppercase"],
            },
            {
                "kobo_name": "termination_date",
                "db_names": ["cc_termination_date"],
                "datatype": "date",
            },
            {
                "kobo_name": "group_cc_growth_species/growth_stage_grains",
                "db_names": ["growth_stage_grains"],
                "multi_select": {
                    "tillering": "Tillering",
                    "stem_extenstion": "Stem Extension",
                    "heading_flowering": "Heading and Flowering",
                    "ripening": "Ripening (grain forming from milk to kernel)",
                },
            },
            {
                "kobo_name": "group_cc_growth_species/growth_stage_legumes",
                "db_names": ["growth_stage_legumes"],
                "multi_select": {
                    "decay_winterkilled": "Decay (winterkilled)",
                    "vegetative": "Vegetative",
                    "flowering": "Flowering",
                    "podfill": "Podfill / Mature",
                },
            },
            {
                "kobo_name": "group_cc_growth_species/growth_stage_brassicas",
                "db_names": ["growth_stage_brassicas"],
                "multi_select": {
                    "decay_winterkilled": "Decay (winterkilled)",
                    "vegetative": "Vegetative",
                    "flowering": "Flowering",
                    "ripening": "Ripening / Mature",
                },
            },
            {
                "kobo_name": "_submitted_by",
                "db_names": ["submitted_by"],
            },
        ],
        "all_cols": ["cc_termination_date", "growth_stage_grains", "growth_stage_legumes", "growth_stage_brassicas"]
    },
]
