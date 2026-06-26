def normalize_instagram(data):
    return {
        "platform": "Instagram",
        "influencer_name": data.get("Influencer insta name"),
        "account_name": data.get("instagram name"),
        "category": data.get("category_1"),
        "audience_country": data.get("Audience country(mostly)"),
        "subscribers": data.get("Followers"),
        "avg_views": None,
        "avg_likes": None,
        "avg_comments": None,
        "avg_shares": None,
        "engagement": data.get("Authentic engagement")
    }


def normalize_youtube(data):
    return {
        "platform": "YouTube",
        "influencer_name": data.get("youtuber name"),
        "account_name": data.get("channel name"),
        "category": data.get("Category"),
        "audience_country": data.get("Audience Country"),
        "subscribers": data.get("Subscribers"),
        "avg_views": data.get("avg views"),
        "avg_likes": data.get("avg likes"),
        "avg_comments": data.get("avg comments"),
        "avg_shares": None,
        "engagement": None
    }


def normalize_tiktok(data):
    return {
        "platform": "TikTok",
        "influencer_name": data.get("Tiktoker name"),
        "account_name": data.get("Tiktok name"),
        "category": None,
        "audience_country": None,
        "subscribers": data.get("Subscribers count"),
        "avg_views": data.get("Views avg."),
        "avg_likes": data.get("Likes avg."),
        "avg_comments": data.get("Comments avg."),
        "avg_shares": data.get("Shares avg."),
        "engagement": None
    }