import psa_gps.version_vFTrkLn3MMbs9wCLEBBh4s as psa_gps_v1

import psa_water_sensor_install.version_vuiiHRr2MJSGzFwSncyLP9 as psa_water_sensor_install_v1
import psa_water_sensor_install.version_vCK5tppVaNkkfWMhtddxEb as psa_water_sensor_install_v2

import psa_decomp_bag_pre_wt.version_vQnB8sJFc8JEhYJqXiYQRy as psa_decomp_bag_pre_wt_v1
import psa_decomp_bag_pre_wt.version_vZvVu9PdqRHLeeJGbGha3z as psa_decomp_bag_pre_wt_v2
import psa_decomp_bag_pre_wt.version_vgaKFRKRg54E2Z7fvayCxf as psa_decomp_bag_pre_wt_v3
import psa_decomp_bag_pre_wt.version_vzazAbS9satE4PXaGNKwBE as psa_decomp_bag_pre_wt_v4 

import psa_bag_dry_wt.version_vDqdEsDav5K6hSRHrgYJmM as psa_bag_dry_wt_v1

asset_names = {
    "psa gps": [
        {   
            "table_name": "gps",
            "table_keys": {
                "vFTrkLn3MMbs9wCLEBBh4s": psa_gps_v1.data,
            }
        }
    ],

    "psa water sensor install": [
        {   
            "table_name": "wsensor_install",
            "table_keys": {
                "vuiiHRr2MJSGzFwSncyLP9": psa_water_sensor_install_v1.data,
                "vCK5tppVaNkkfWMhtddxEb": psa_water_sensor_install_v2.data,
            }
        }
    ],

    "psa decomp bag pre wt": [
        {   
            "table_name": "decomp_biomass_fresh__decomp_bag_pre_wt",
            "table_keys": {
                "vQnB8sJFc8JEhYJqXiYQRy": psa_decomp_bag_pre_wt_v1.data,
                "vZvVu9PdqRHLeeJGbGha3z": psa_decomp_bag_pre_wt_v2.data,
                "vgaKFRKRg54E2Z7fvayCxf": psa_decomp_bag_pre_wt_v3.data,
                "vzazAbS9satE4PXaGNKwBE": psa_decomp_bag_pre_wt_v4.data,                
            }
        }
    ],

    "psa decomp bag dry wt": [
        {   
            "table_name": "decomp_biomass_dry__decomp_bag_dry_wt",
            "table_keys": {
                "vDqdEsDav5K6hSRHrgYJmM": psa_bag_dry_wt_v1.data
            }
        }
    ],

    # "psa decomp bag collect": [
    #     {   
    #         "table_name": "decomp_biomass_dry__decomp_bag_collect",
    #         "table_keys": {
    #             "vQnB8sJFc8JEhYJqXiYQRy": psa_water_sensor_install_v1.data
    #         }
    #     }
    # ],

    # "psa biomass decomp bag": [
    #     {   
    #         "table_name": "biomass_in_field__biomass_decomp_bag",
    #         "table_keys": {
    #             "vQnB8sJFc8JEhYJqXiYQRy": psa_water_sensor_install_v1.data
    #         }
    #     },
    #     {   
    #         "table_name": "decomp_biomass_fresh__biomass_decomp_bag ",
    #         "table_keys": {
    #             "vQnB8sJFc8JEhYJqXiYQRy": psa_water_sensor_install_v1.data
    #         }
    #     },
    # ],
}