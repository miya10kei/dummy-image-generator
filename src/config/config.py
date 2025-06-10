"""
カード生成に必要な設定を定義するモジュール
"""

# 運転免許証の設定
DRIVER_LICENSE_CONFIG = {
    "name": {"position": (100, 26), "font_size": 20},
    "address": {"position": (90, 90), "font_size": 20},
    "birth_year": {"position": (440, 26), "font_size": 20},
    "birth_month": {"position": (530, 26), "font_size": 20},
    "birth_day": {"position": (590, 26), "font_size": 20},
    "expired_year": {"position": (122, 150), "font_size": 25},
    "expired_year_western": {"position": (35, 150), "font_size": 25},
    "expired_month": {"position": (235, 150), "font_size": 25},
    "expired_day": {"position": (287, 150), "font_size": 25},
}

# マイナンバーカードの設定
INDIVIDUAL_NUMBER_CONFIG = {
    "name": {"position": (50, 22), "font_size": 16},
    "address": {"position": (50, 53), "font_size": 16},
    "birth_year": {"position": (182, 104), "font_size": 13},
    "birth_month": {"position": (238.5, 104), "font_size": 13},
    "birth_day": {"position": (265, 104), "font_size": 13},
    "sex": {"position": (470, 75), "font_size": 13},
    "expired_year": {"position": (314, 103), "font_size": 13},
    "expired_month": {"position": (370, 103), "font_size": 13},
    "expired_day": {"position": (400, 103), "font_size": 13},
}

# テンプレート画像とフォントのパス
TEMPLATE_PATHS = {
    "driver_license": "templates/driver_license_template.png",
    "individual_number": "templates/individual_number_card_template.png",
    "font": "fonts/NotoSansJP-Regular.ttf",
}
