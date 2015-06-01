#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#--------------------------------------------------------------
#
# naviappfeedback
#               -- API for navigation app feedback 
#
# config.py: Configurations.
#
#--------------------------------------------------------------
#
# Date:     2015-05-14
#
# Author:   gewu@baidu.com
#
#
CONFIG = {
        "mongo": {
            "host": "10.48.23.144",
            "port": 27017,
        },

        #################
        #
        # API params
        #################
        "naviappfeedback": {
            "api"  :   "ugc_id, administrative_division_id, user_flag_data, siwei_link1_id,"\
                       "siwei_link2_id, siwei_link1_list, siwei_link2_list, current_path_list,"\
                       "current_track_list, influence_surface, repeat_num, linename, create_time,"\
                       "user_name, contact, user_field",
            
            "field":   "dispatch_status, commit_time, province, city",

            "check":   "ugc_id, administrative_division_id, user_flag_data, siwei_link1_id, siwei_link1_list",

            "city_area": ["", "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海",\
                          "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东",\
                          "广西", "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃", "青海",\
                          "宁夏", "新疆", "香港", "澳门"
                         ]
        }
}


        
