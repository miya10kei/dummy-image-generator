import os
from typing import Any, Dict, Tuple

from PIL import Image, ImageDraw, ImageFont


class DriverLicenseGenerator:
    def __init__(self, template_path: str, font_path: str):
        """
        運転免許証生成クラスの初期化

        Args:
            template_path (str): テンプレート画像のパス
            font_path (str): フォントファイルのパス
        """
        self.template = Image.open(template_path)
        self.font_path = font_path
        self.draw = ImageDraw.Draw(self.template)

    def add_text(
        self, text: str, position: Tuple[int, int], font_size: int = 20, color: Tuple[int, int, int] = (0, 0, 0)
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

    def generate_license(self, data: Dict[str, Any], output_path: str):
        """
        運転免許証を生成

        Args:
            data (Dict[str, str]): 運転免許証のデータ
            output_path (str): 出力先のパス
        """
        # 氏名
        self.add_text(data.get("name", ""), (120, 26))

        # 住所
        self.add_text(data.get("address", ""), (100, 90))

        # 生年月日
        self.add_text(data.get("birth_date", {}).get("year", ""), (435, 26))
        self.add_text(data.get("birth_date", {}).get("month", ""), (530, 26))
        self.add_text(data.get("birth_date", {}).get("day", ""), (590, 26))

        # 画像を保存
        self.template.save(output_path)


def main():
    # テンプレート画像とフォントのパスを設定
    template_path = "templates/driver_license_template.png"
    font_path = "fonts/NotoSansJP-Regular.ttf"

    # 出力ディレクトリの作成
    os.makedirs("output", exist_ok=True)

    # サンプルデータ
    data = {
        "name": "山　田　　太　郎",
        "address": "東京都渋谷区渋谷１−１−１",
        "birth_date": {"year": "昭和51", "month": "12", "day": "12"},
    }

    # 運転免許証の生成
    generator = DriverLicenseGenerator(template_path, font_path)
    generator.generate_license(data, "output/driver_license.png")


if __name__ == "__main__":
    main()
