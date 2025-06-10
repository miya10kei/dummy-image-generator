import os
import csv
import argparse
import re
from typing import Any, Dict, Tuple

from PIL import Image, ImageDraw, ImageFont


def format_name_for_driver_license(name: str) -> str:
    """
    運転免許証用の姓名フォーマット
    全角スペースで区切られた姓名を各文字の間に全角スペースを挿入し、
    姓と名の間に全角スペース2つを挿入した形式に変換する

    Args:
        name (str): 変換前の名前（「姓　名」形式）

    Returns:
        str: 変換後の名前（各文字の間に全角スペースを挿入、姓と名の間に全角スペース2つを挿入）
    """
    # 全角スペースで分割
    parts = name.split("　")
    # 各部分の文字の間に全角スペースを挿入
    formatted_parts = ["　".join(part) for part in parts]
    # 姓と名の間に全角スペース2つを挿入
    return "　　".join(formatted_parts)


def format_name_for_individual_number_card(name: str) -> str:
    """
    マイナンバーカード用の姓名フォーマット
    全角スペースで区切られた姓名を姓と名の間に全角スペース1つを挿入した形式に変換する

    Args:
        name (str): 変換前の名前（「姓　名」形式）

    Returns:
        str: 変換後の名前（姓と名の間に全角スペース1つを挿入）
    """
    # 全角スペースで分割
    parts = name.split("　")
    # 姓と名の間に全角スペース1つを挿入
    return "　".join(parts)


def get_filename(name: str, card_type: str) -> str:
    """
    姓名からファイル名を生成する

    Args:
        name (str): 全角スペースで区切られた姓名
        card_type (str): カードの種類（"運転免許証" または "Individual Number Card"）

    Returns:
        str: ファイル名（「姓名_カード種類.png」形式）
    """
    # 全角スペースを削除
    return f"{name.replace('　', '')}_{card_type}.png"


def convert_to_western_year(year: str) -> str:
    """
    和暦を西暦に変換する

    Args:
        year (str): 和暦（例：令和10年）

    Returns:
        str: 西暦（4桁の文字列）
    """
    # 年号と年数を抽出
    match = re.match(r'(令和|平成|昭和|大正|明治)(\d+)', year)
    if not match:
        return year

    era, year_num = match.groups()
    year_num = int(year_num)

    # 年号に応じて西暦に変換
    if era == "令和":
        return str(year_num + 2018)
    elif era == "平成":
        return str(year_num + 1988)
    elif era == "昭和":
        return str(year_num + 1925)
    elif era == "大正":
        return str(year_num + 1911)
    elif era == "明治":
        return str(year_num + 1867)
    else:
        return year


class CardGenerator:
    def __init__(self, template_path: str, font_path: str):
        """
        カード生成クラスの初期化

        Args:
            template_path (str): テンプレート画像のパス
            font_path (str): フォントファイルのパス
        """
        self.template = Image.open(template_path)
        self.font_path = font_path
        self.draw = ImageDraw.Draw(self.template)

    def add_text(
        self, text: str, position: Tuple[int, int], font_size: int, color: Tuple[int, int, int] = (0, 0, 0)
    ):
        """
        画像にテキストを追加

        Args:
            text (str): 追加するテキスト
            position (Tuple[int, int]): テキストの位置（x, y）
            font_size (int): フォントサイズ
            color (Tuple[int, int, int]): テキストの色（RGB）
        """
        font = ImageFont.truetype(self.font_path, font_size)
        self.draw.text(position, text, font=font, fill=color)


class DriverLicenseGenerator(CardGenerator):
    def generate_license(self, data: Dict[str, Any], output_path: str):
        """
        運転免許証を生成

        Args:
            data (Dict[str, str]): 運転免許証のデータ
            output_path (str): 出力先のパス
        """
        config = data["config"]

        # 氏名
        self.add_text(
            data["name"],
            config["name"]["position"],
            config["name"]["font_size"]
        )

        # 住所
        self.add_text(
            data["address"],
            config["address"]["position"],
            config["address"]["font_size"]
        )

        # 生年月日
        self.add_text(
            data["birth_date"]["year"],
            config["birth_year"]["position"],
            config["birth_year"]["font_size"]
        )
        self.add_text(
            data["birth_date"]["month"],
            config["birth_month"]["position"],
            config["birth_month"]["font_size"]
        )
        self.add_text(
            data["birth_date"]["day"],
            config["birth_day"]["position"],
            config["birth_day"]["font_size"]
        )

        # 有効期限（和暦）
        self.add_text(
            data["expired_date"]["year"],
            config["expired_year"]["position"],
            config["expired_year"]["font_size"]
        )
        # 有効期限（西暦）
        self.add_text(
            data["expired_date"]["western_year"],
            config["expired_year_western"]["position"],
            config["expired_year_western"]["font_size"]
        )
        self.add_text(
            data["expired_date"]["month"],
            config["expired_month"]["position"],
            config["expired_month"]["font_size"]
        )
        self.add_text(
            data["expired_date"]["day"],
            config["expired_day"]["position"],
            config["expired_day"]["font_size"]
        )

        # 画像を保存
        self.template.save(output_path)


class IndividualNumberCardGenerator(CardGenerator):
    def generate_card(self, data: Dict[str, Any], output_path: str):
        """
        マイナンバーカードを生成

        Args:
            data (Dict[str, str]): マイナンバーカードのデータ
            output_path (str): 出力先のパス
        """
        config = data["config"]

        # 氏名
        self.add_text(
            data["name"],
            config["name"]["position"],
            config["name"]["font_size"]
        )

        # 住所
        self.add_text(
            data["address"],
            config["address"]["position"],
            config["address"]["font_size"]
        )

        # 生年月日
        self.add_text(
            data["birth_date"]["year"],
            config["birth_year"]["position"],
            config["birth_year"]["font_size"]
        )
        self.add_text(
            data["birth_date"]["month"],
            config["birth_month"]["position"],
            config["birth_month"]["font_size"]
        )
        self.add_text(
            data["birth_date"]["day"],
            config["birth_day"]["position"],
            config["birth_day"]["font_size"]
        )

        # 性別
        self.add_text(
            data["sex"],
            config["sex"]["position"],
            config["sex"]["font_size"]
        )

        # 有効期限
        self.add_text(
            data["expired_date"]["year"],
            config["expired_year"]["position"],
            config["expired_year"]["font_size"]
        )
        self.add_text(
            data["expired_date"]["month"],
            config["expired_month"]["position"],
            config["expired_month"]["font_size"]
        )
        self.add_text(
            data["expired_date"]["day"],
            config["expired_day"]["position"],
            config["expired_day"]["font_size"]
        )

        # 画像を保存
        self.template.save(output_path)


def main():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description='運転免許証とマイナンバーカードを生成します')
    parser.add_argument('csv_file', help='データを含むCSVファイルのパス')
    args = parser.parse_args()

    # テンプレート画像とフォントのパスを設定
    driver_license_template = "templates/driver_license_template.png"
    individual_number_template = "templates/individual_number_card_template.png"
    font_path = "fonts/NotoSansJP-Regular.ttf"

    # 出力ディレクトリの作成
    os.makedirs("output", exist_ok=True)

    # 運転免許証の設定
    driver_license_config = {
        "name": {"position": (100, 26), "font_size": 20},
        "address": {"position": (90, 90), "font_size": 20},
        "birth_year": {"position": (440, 26), "font_size": 20},
        "birth_month": {"position": (530, 26), "font_size": 20},
        "birth_day": {"position": (590, 26), "font_size": 20},
        "expired_year_western": {"position": (35, 150), "font_size": 25},
        "expired_year": {"position": (122, 150), "font_size": 25},
        "expired_month": {"position": (235, 150), "font_size": 25},
        "expired_day": {"position": (287, 150), "font_size": 25}
    }

    # マイナンバーカードの設定
    individual_number_config = {
        "name": {"position": (50, 22), "font_size": 16},
        "address": {"position": (50, 53), "font_size": 16},
        "birth_year": {"position": (182, 104), "font_size": 13},
        "birth_month": {"position": (238.5, 104), "font_size": 13},
        "birth_day": {"position": (265, 104), "font_size": 13},
        "sex": {"position": (470, 75), "font_size": 13},
        "expired_year": {"position": (314, 103), "font_size": 13},
        "expired_month": {"position": (370, 103), "font_size": 13},
        "expired_day": {"position": (400, 103), "font_size": 13}
    }

    # CSVファイルからデータを読み込む
    with open(args.csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            base_data = {
                "name": format_name_for_driver_license(name),
                "address": row["address"],
                "birth_date": {
                    "year": row["birth_year"],
                    "month": row["birth_month"],
                    "day": row["birth_day"]
                },
                "sex": row["sex"],
                "expired_date": {
                    "year": row["expired_year"],
                    "western_year": convert_to_western_year(row["expired_year"]),
                    "month": row["expired_month"],
                    "day": row["expired_day"]
                }
            }

            # 運転免許証用のデータを準備
            driver_license_data = base_data.copy()
            driver_license_data["config"] = driver_license_config

            # 運転免許証の生成
            driver_license_generator = DriverLicenseGenerator(driver_license_template, font_path)
            driver_license_path = os.path.join("output", get_filename(name, "運転免許証"))
            driver_license_generator.generate_license(driver_license_data, driver_license_path)
            print(f"運転免許証生成完了: {driver_license_path}")

            # マイナンバーカード用のデータを準備
            individual_number_data = base_data.copy()
            individual_number_data["name"] = format_name_for_individual_number_card(name)
            individual_number_data["config"] = individual_number_config

            # マイナンバーカードの生成
            individual_number_generator = IndividualNumberCardGenerator(individual_number_template, font_path)
            individual_number_path = os.path.join("output", get_filename(name, "Individual Number Card"))
            individual_number_generator.generate_card(individual_number_data, individual_number_path)
            print(f"マイナンバーカード生成完了: {individual_number_path}")


if __name__ == "__main__":
    main()
