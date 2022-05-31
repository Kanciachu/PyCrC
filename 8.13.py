def build_profile(first,last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile("Albert", "Einstein",
                             location="Princeton",
                             field="Physics")

user_profile1 = build_profile("antoni", "wanot",
                              location="kutno",
                              field="computer science",
                              rank="student" )

print(f"{user_profile} \n {user_profile1}")