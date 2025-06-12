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

# 履歴事項全部証明書（ページごと）の設定
CERTIFICATE_OF_REGISTERED_MATTERS_CONFIGS = {
    "page1": {
        "company_name": {"x": 495, "y": 620, "font_size": 26},
        "company_address": {"x": 495, "y": 830, "font_size": 26},
        "corporate_number": {"x": 495, "y": 425, "font_size": 26},
    },
    "page2": {
        "representative_name": {"x": 710, "y": 1250, "font_size": 26},
    },
    "page3": {
        "issue_year": {"x": 440, "y": 1730, "font_size": 26},
        "issue_month": {"x": 570, "y": 1730, "font_size": 26},
        "issue_day": {"x": 670, "y": 1730, "font_size": 26},
    },
}

# テンプレート画像とフォントのパス
TEMPLATE_PATHS = {
    "driver_license": "templates/driver_license_template.png",
    "individual_number": "templates/individual_number_card_template.png",
    "font": "fonts/NotoSansJP-Regular.ttf",
    "certificate_of_registered_matters_1": "templates/certificate_of_registered_matters_template_1.png",
    "certificate_of_registered_matters_2": "templates/certificate_of_registered_matters_template_2.png",
    "certificate_of_registered_matters_3": "templates/certificate_of_registered_matters_template_3.png",
}
