import psa_gps.psa_gps_vFTrkLn3MMbs9wCLEBBh4s as psa_gps_v1

import psa_water_sensor_install.wsensor_install_vuiiHRr2MJSGzFwSncyLP9 as wsensor_install_vuiiHRr2MJSGzFwSncyLP9_v1
import psa_water_sensor_install.wsensor_install_vCK5tppVaNkkfWMhtddxEb as wsensor_install_vCK5tppVaNkkfWMhtddxEb_v2

import psa_decomp_bag_pre_wt.decomp_biomass_fresh_vQnB8sJFc8JEhYJqXiYQRy as decomp_biomass_fresh_vQnB8sJFc8JEhYJqXiYQRy_v1
import psa_decomp_bag_pre_wt.decomp_biomass_fresh_vZvVu9PdqRHLeeJGbGha3z as decomp_biomass_fresh_vZvVu9PdqRHLeeJGbGha3z_v2
import psa_decomp_bag_pre_wt.decomp_biomass_fresh_vgaKFRKRg54E2Z7fvayCxf as decomp_biomass_fresh_vgaKFRKRg54E2Z7fvayCxf_v3
import psa_decomp_bag_pre_wt.decomp_biomass_fresh_vzazAbS9satE4PXaGNKwBE as decomp_biomass_fresh_vzazAbS9satE4PXaGNKwBE_v4 

import psa_bag_dry_wt.decomp_biomass_dry_vDqdEsDav5K6hSRHrgYJmM as decomp_biomass_dry_vDqdEsDav5K6hSRHrgYJmM_v1
import psa_bag_dry_wt.decomp_biomass_dry_vusvAjv42DfdfjKkFWm6H3 as decomp_biomass_dry_vusvAjv42DfdfjKkFWm6H3_v2

import psa_bag_collect.decomp_biomass_dry_v94kLXWMrZ8fZRpCFzSn4e as decomp_biomass_dry_v94kLXWMrZ8fZRpCFzSn4e_v1
import psa_bag_collect.decomp_biomass_dry_v5LVmcbGVhR3C3fkW9ZhHG as decomp_biomass_dry_v5LVmcbGVhR3C3fkW9ZhHG_v2

import psa_biomass_decomp_bag.biomass_in_field_vEchkcAone8S7y4eYhgru4 as biomass_in_field_vEchkcAone8S7y4eYhgru4_v1
import psa_biomass_decomp_bag.biomass_in_field_vyYD9Bt3WSjzKorvPhLvLh as biomass_in_field_vyYD9Bt3WSjzKorvPhLvLh_v2
import psa_biomass_decomp_bag.biomass_in_field_vcrycicDgojagKK5b7hTAP as biomass_in_field_vcrycicDgojagKK5b7hTAP_v3

import psa_biomass_decomp_bag.decomp_biomass_fresh_vEchkcAone8S7y4eYhgru4 as decomp_biomass_fresh_vEchkcAone8S7y4eYhgru4_v1
import psa_biomass_decomp_bag.decomp_biomass_fresh_vyYD9Bt3WSjzKorvPhLvLh as decomp_biomass_fresh_vyYD9Bt3WSjzKorvPhLvLh_v2
import psa_biomass_decomp_bag.decomp_biomass_fresh_vcrycicDgojagKK5b7hTAP as decomp_biomass_fresh_vcrycicDgojagKK5b7hTAP_v3

asset_names = {
    "psa gps": [
        {   
            "table_name": "gps",
            "table_keys": {
                "vFTrkLn3MMbs9wCLEBBh4s": psa_gps_v1.data,
            },
        },
    ],

    "psa water sensor install": [
        {   
            "table_name": "wsensor_install",
            "table_keys": {
                "vuiiHRr2MJSGzFwSncyLP9": wsensor_install_vuiiHRr2MJSGzFwSncyLP9_v1.data,
                "vCK5tppVaNkkfWMhtddxEb": wsensor_install_vCK5tppVaNkkfWMhtddxEb_v2.data,
            },
        },
    ],

    "psa decomp bag pre wt": [
        {   
            "table_name": "decomp_biomass_fresh__decomp_bag_pre_wt",
            "table_keys": {
                "vQnB8sJFc8JEhYJqXiYQRy": decomp_biomass_fresh_vQnB8sJFc8JEhYJqXiYQRy_v1.data,
                "vZvVu9PdqRHLeeJGbGha3z": decomp_biomass_fresh_vZvVu9PdqRHLeeJGbGha3z_v2.data,
                "vgaKFRKRg54E2Z7fvayCxf": decomp_biomass_fresh_vgaKFRKRg54E2Z7fvayCxf_v3.data,
                "vzazAbS9satE4PXaGNKwBE": decomp_biomass_fresh_vzazAbS9satE4PXaGNKwBE_v4.data,                
            },
        },
    ],

    "psa decomp bag dry wt": [
        {   
            "table_name": "decomp_biomass_dry__decomp_bag_dry_wt",
            "table_keys": {
                "vDqdEsDav5K6hSRHrgYJmM": decomp_biomass_dry_vDqdEsDav5K6hSRHrgYJmM_v1.data,
                "vusvAjv42DfdfjKkFWm6H3": decomp_biomass_dry_vusvAjv42DfdfjKkFWm6H3_v2.data,
            },
        },
    ],

    "psa decomp bag collect": [
        {   
            "table_name": "decomp_biomass_dry__decomp_bag_collect",
            "table_keys": {
                "v94kLXWMrZ8fZRpCFzSn4e": decomp_biomass_dry_v94kLXWMrZ8fZRpCFzSn4e_v1.data,
                "v5LVmcbGVhR3C3fkW9ZhHG": decomp_biomass_dry_v5LVmcbGVhR3C3fkW9ZhHG_v2.data,
            },
        },
    ],

    "psa biomass decomp bag": [
        {   
            "table_name": "biomass_in_field__biomass_decomp_bag",
            "table_keys": {
                "vEchkcAone8S7y4eYhgru4": biomass_in_field_vEchkcAone8S7y4eYhgru4_v1.data,
                "vyYD9Bt3WSjzKorvPhLvLh": biomass_in_field_vyYD9Bt3WSjzKorvPhLvLh_v2.data,
                "vcrycicDgojagKK5b7hTAP": biomass_in_field_vcrycicDgojagKK5b7hTAP_v3.data,
            },
        },
        {   
            "table_name": "decomp_biomass_fresh__biomass_decomp_bag",
            "table_keys": {
                "vEchkcAone8S7y4eYhgru4": decomp_biomass_fresh_vEchkcAone8S7y4eYhgru4_v1.data,
                "vyYD9Bt3WSjzKorvPhLvLh": decomp_biomass_fresh_vyYD9Bt3WSjzKorvPhLvLh_v2.data,
                "vcrycicDgojagKK5b7hTAP": decomp_biomass_fresh_vcrycicDgojagKK5b7hTAP_v3.data,
            },
        },
    ],
}