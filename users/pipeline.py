from django.utils import timezone


def get_username(strategy, details, backend, response, user=None, *args, **kwargs):
    username = None
    if backend.name == 'weibo':
        username = 'weibo' + response.get('uid')
    elif backend.name == 'twitter':
        username = 'twitter' + response.get('id_str')
    elif backend.name == 'qq':
        username = 'qq123'
    return {'username': username}


def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'weibo':
        if not user.profile.gender:
            gender = response.get('gender')
            if gender == "m":
                user.profile.gender = 1
            elif gender == "f":
                user.profile.gender = 2
            else:
                user.profile.gender = 3
        if not user.email:
            user.email = str(response.get('id')) + '@weibo.com'
        if not user.profile.photo:
            user.profile.photo = response.get('avatar_large')
        if not user.profile.bio:
            user.profile.bio = response.get('description')
        if not user.profile.location:
            user.profile.location = response.get('location')
        if not user.profile.birthday:
            user.profile.birthday = timezone.now()
        if not user.profile.website:
            user.profile.website = response.get('url')
        user.save()
    elif backend.name == 'twitter':
        if not user.profile.gender:
            gender = response.get('gender')
            if gender == "m":
                user.profile.gender = 1
            elif gender == "f":
                user.profile.gender = 2
            else:
                user.profile.gender = 3
        if not user.email:
            user.email = str(response.get('id')) + '@twitter.com'
        if not user.profile.photo:
            user.profile.photo = response.get('profile_image_url')
        if not user.profile.bio:
            user.profile.bio = response.get('description')
        if not user.profile.location:
            user.profile.location = response.get('location')
        if not user.profile.birthday:
            user.profile.birthday = timezone.now()
        if not user.profile.website:
            user.profile.website = response.get('url')
        user.save()
    elif backend.name == 'qq':
        print('*' * 80)
        print(response)
    else:
        pass

weibo_info = {u'bi_followers_count': 358,
              u'domain': u'suchcool',
              u'avatar_large': u'http://tva1.sinaimg.cn/crop.0.0.199.199.180/65fbff97gw1emui0bsvaej205k05kweq.jpg',    # <<<<<<
              u'uid': u'1711013783',      # <<<<<<
              u'verified_source': u'',
              u'ptype': 0,
              u'avatar_hd': u'http://tva1.sinaimg.cn/crop.0.0.199.199.1024/65fbff97gw1emui0bsvaej205k05kweq.jpg',
              u'block_word': 0,
              u'cover_image_phone': u'http://ww2.sinaimg.cn/crop.0.0.640.640.640/a1d3feabjw1ecat8op0e1j20hs0hswgu.jpg',
              u'statuses_count': 1790,
              u'id': 1711013783,
              u'verified_reason_url': u'',
              u'city': u'2',
              u'verified': False,
              u'credit_score': 80,
              u'insecurity': {u'sexual_content': False},
              u'block_app': 0,
              u'expires_in': 157679999,
              u'follow_me': False,
              u'verified_reason': u'',
              u'remind_in': u'157679999',
              u'location': u'\u798f\u5efa \u53a6\u95e8',    # <<<<<<
              u'followers_count': 1226,
              u'verified_trade': u'',
              u'mbtype': 2,
              u'verified_source_url': u'',
              u'profile_url': u'13205012',
              u'status': {u'reposts_count': 0,
                          u'biz_feature': 4294967300,
                          u'truncated': False,
                          u'text': u'\u5206\u4eab\u56fe\u7247',
                          u'more_info_type': 0,
                          u'visible': {u'type': 0, u'list_id': 0},
                          u'in_reply_to_status_id': u'',
                          u'bmiddle_pic': u'http://wx3.sinaimg.cn/bmiddle/65fbff97gy1fi91q02ruxj20ku0bojsa.jpg',
                          u'text_tag_tips': [], u'id': 4137459094395599,
                          u'thumbnail_pic': u'http://wx3.sinaimg.cn/thumbnail/65fbff97gy1fi91q02ruxj20ku0bojsa.jpg',
                          u'mblog_vip_type': 0,
                          u'mid': u'4137459094395599',
                          u'userType': 0,
                          u'source': u'<a href="http://app.weibo.com/t/feed/2J8wRB" rel="nofollow">iPhone 7</a>',
                          u'attitudes_count': 0,
                          u'in_reply_to_screen_name': u'',
                          u'pic_urls': [{u'thumbnail_pic': u'http://wx3.sinaimg.cn/thumbnail/65fbff97gy1fi91q02ruxj20ku0bojsa.jpg'}],
                          u'comment_manage_info': {u'comment_permission_type': -1},
                          u'positive_recom_flag': 0,
                          u'annotations': [{u'client_mblogid': u'iPhone-D926851F-0F0F-46E1-9BD3-71986291B68A'}, {u'mapi_request': True}],
                          u'in_reply_to_user_id': u'', u'darwin_tags': [],
                          u'favorited': False,
                          u'original_pic': u'http://wx3.sinaimg.cn/large/65fbff97gy1fi91q02ruxj20ku0bojsa.jpg',
                          u'source_allowclick': 0,
                          u'idstr': u'4137459094395599',
                          u'source_type': 1,
                          u'hot_weibo_tags': [],
                          u'geo': None,
                          u'isLongText': False,
                          u'gif_ids': u'',
                          u'textLength': 8,
                          u'hasActionTypeCard': 0,
                          u'is_paid': False,
                          u'mlevel': 0,
                          u'is_show_bulletin': 2,
                          u'comments_count': 0,
                          u'created_at': u'Sat Aug 05 18:56:21 +0800 2017'},
              u'avatargj_id': u'gj_vip_091',
              u'star': 0,
              u'description': u'\u60f3\u8fc7\u6ca1\u6709\u5fd8\u8bb0// \u5018\u82e5\u7ea2\u5c18\u4ea6\u7eb7\u98de\uff0c\u4f55\u5fc5\u82e6\u7b11\u505a\u6b22\u989c\u3002\uff1f',
              u'friends_count': 458,
              u'online_status': 0,
              u'mbrank': 1,
              u'idstr': u'1711013783',
              u'profile_image_url': u'http://tva1.sinaimg.cn/crop.0.0.199.199.50/65fbff97gw1emui0bsvaej205k05kweq.jpg',
              u'isRealName': u'true',
              u'following': False,
              u'allow_all_act_msg': False,
              u'screen_name': u'\u8717\u725b\u8fc7\u6c99\u6f20_',
              u'vclub_member': 0,
              u'allow_all_comment': True,
              u'geo_enabled': True,
              u'class': 1,
              u'name': u'\u8717\u725b\u8fc7\u6c99\u6f20_',
              u'lang': u'zh-cn',
              u'weihao': u'13205012',
              u'remark': u'',
              u'favourites_count': 0,
              u'like': False,
              u'access_token': u'2.00VqOnrB0vevFma9bd00df46_FcfBD',
              u'province': u'35',
              u'created_at': u'Mon Apr 19 09:53:47 +0800 2010',
              u'url': u'http://blog.sina.com.cn/suchcool',
              u'user_ability': 0,
              u'story_read_state': -1,
              u'verified_type': 220,
              u'gender': u'm',
              u'like_me': False,
              u'pagefriends_count': 0,
              u'urank': 23}
twitter_info = {u'follow_request_sent': False,
                u'has_extended_profile': True,
                u'profile_use_background_image': True,
                u'default_profile_image': False,
                u'id': 857973824213536768,       # <<<<<<
                u'profile_background_image_url_https': None,
                u'verified': False,
                u'translator_type': u'none',
                u'profile_text_color': u'333333',
                u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/878820111745863680/_v5MG1RR_normal.jpg',
                u'profile_sidebar_fill_color': u'DDEEF6',
                u'entities': {u'description': {u'urls': []}},
                u'followers_count': 1,
                u'profile_sidebar_border_color': u'C0DEED',
                u'id_str': u'857973824213536768',
                u'profile_background_color': u'F5F8FA',
                u'listed_count': 0,
                u'is_translation_enabled': False,
                u'utc_offset': None,
                u'statuses_count': 0,
                u'description': u'',
                u'friends_count': 35,
                u'location': u'Xiamen',
                u'profile_link_color': u'1DA1F2',
                u'profile_image_url': u'http://pbs.twimg.com/profile_images/878820111745863680/_v5MG1RR_normal.jpg',
                u'following': False,
                u'geo_enabled': False,
                u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/857973824213536768/1493392363',
                u'profile_background_image_url': None,
                u'screen_name': u'changduchen',
                u'lang': u'en',
                u'profile_background_tile': False,
                u'favourites_count': 0,
                u'name': u'Chand',
                u'notifications': False,
                u'url': None,
                u'created_at': u'Fri Apr 28 15:04:34 +0000 2017',
                u'contributors_enabled': False,
                u'time_zone': None,
                'access_token': {u'oauth_token_secret': u'RzJjvGWMNIuHEkZJKzsdbWyyZL2wjwYUivveUzCRdbSBx',
                                 u'oauth_token': u'857973824213536768-bHnAgQcZqGLD06DN8Gw8qeD2eYxb7BI',
                                 u'x_auth_expires': u'0',
                                 u'user_id': u'857973824213536768',
                                 u'screen_name': u'changduchen'},
                u'protected': False,
                u'default_profile': True,
                u'is_translator': False}