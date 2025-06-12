from typing import Any, Dict, Tuple
import os

from PIL import Image, ImageDraw, ImageFont
from config.config import TEMPLATE_PATHS, CERTIFICATE_OF_REGISTERED_MATTERS_CONFIGS
from utils.utils import format_representative_name


class CardGenerator:
    def __init__(self, template_path: str = None, font_path: str = None):
        """
        カード生成クラスの初期化

        Args:
            template_path (str): テンプレート画像のパス
            font_path (str): フォントファイルのパス
        """
        self.template = Image.open(template_path) if template_path else None
        self.font_path = font_path
        self.draw = ImageDraw.Draw(self.template) if self.template else None

    def add_text(self, text: str, position: Tuple[int, int], font_size: int, color: Tuple[int, int, int] = (0, 0, 0)):
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
        self.add_text(data["name"], config["name"]["position"], config["name"]["font_size"])

        # 住所
        self.add_text(data["address"], config["address"]["position"], config["address"]["font_size"])

        # 生年月日
        self.add_text(data["birth_date"]["year"], config["birth_year"]["position"], config["birth_year"]["font_size"])
        self.add_text(
            data["birth_date"]["month"], config["birth_month"]["position"], config["birth_month"]["font_size"]
        )
        self.add_text(data["birth_date"]["day"], config["birth_day"]["position"], config["birth_day"]["font_size"])

        # 有効期限（和暦）
        self.add_text(
            data["expired_date"]["year"], config["expired_year"]["position"], config["expired_year"]["font_size"]
        )
        # 有効期限（西暦）
        self.add_text(
            data["expired_date"]["western_year"],
            config["expired_year_western"]["position"],
            config["expired_year_western"]["font_size"],
        )
        self.add_text(
            data["expired_date"]["month"], config["expired_month"]["position"], config["expired_month"]["font_size"]
        )
        self.add_text(
            data["expired_date"]["day"], config["expired_day"]["position"], config["expired_day"]["font_size"]
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
        self.add_text(data["name"], config["name"]["position"], config["name"]["font_size"])

        # 住所
        self.add_text(data["address"], config["address"]["position"], config["address"]["font_size"])

        # 生年月日
        self.add_text(data["birth_date"]["year"], config["birth_year"]["position"], config["birth_year"]["font_size"])
        self.add_text(
            data["birth_date"]["month"], config["birth_month"]["position"], config["birth_month"]["font_size"]
        )
        self.add_text(data["birth_date"]["day"], config["birth_day"]["position"], config["birth_day"]["font_size"])

        # 性別
        self.add_text(data["sex"], config["sex"]["position"], config["sex"]["font_size"])

        # 有効期限
        self.add_text(
            data["expired_date"]["year"], config["expired_year"]["position"], config["expired_year"]["font_size"]
        )
        self.add_text(
            data["expired_date"]["month"], config["expired_month"]["position"], config["expired_month"]["font_size"]
        )
        self.add_text(
            data["expired_date"]["day"], config["expired_day"]["position"], config["expired_day"]["font_size"]
        )

        # 画像を保存
        self.template.save(output_path)


class CertificateOfRegisteredMattersGenerator(CardGenerator):
    def __init__(self, font_path: str):
        super().__init__(None, font_path)

    def generate_certificates(self, data: Dict[str, Any], output_prefix: str):
        # 1ページ目
        self.template = Image.open(TEMPLATE_PATHS["certificate_of_registered_matters_1"])
        self.draw = ImageDraw.Draw(self.template)
        config1 = CERTIFICATE_OF_REGISTERED_MATTERS_CONFIGS["page1"]
        self.add_text(data["company_name"], (config1["company_name"]["x"], config1["company_name"]["y"]), config1["company_name"]["font_size"])
        self.add_text(data["company_address"], (config1["company_address"]["x"], config1["company_address"]["y"]), config1["company_address"]["font_size"])
        self.add_text(data["corporate_number"], (config1["corporate_number"]["x"], config1["corporate_number"]["y"]), config1["corporate_number"]["font_size"])
        self.template.save(f"{output_prefix}_1.png")

        # 2ページ目
        self.template = Image.open(TEMPLATE_PATHS["certificate_of_registered_matters_2"])
        self.draw = ImageDraw.Draw(self.template)
        config2 = CERTIFICATE_OF_REGISTERED_MATTERS_CONFIGS["page2"]
        formatted_representative_name = format_representative_name(data["representative_name"])
        self.add_text(formatted_representative_name, (config2["representative_name"]["x"], config2["representative_name"]["y"]), config2["representative_name"]["font_size"])
        self.template.save(f"{output_prefix}_2.png")

        # 3ページ目
        self.template = Image.open(TEMPLATE_PATHS["certificate_of_registered_matters_3"])
        self.draw = ImageDraw.Draw(self.template)
        config3 = CERTIFICATE_OF_REGISTERED_MATTERS_CONFIGS["page3"]
        # 発行年月日を個別に埋め込む
        self.add_text(data["issue_year"], (config3["issue_year"]["x"], config3["issue_year"]["y"]), config3["issue_year"]["font_size"])
        self.add_text(data["issue_month"], (config3["issue_month"]["x"], config3["issue_month"]["y"]), config3["issue_month"]["font_size"])
        self.add_text(data["issue_day"], (config3["issue_day"]["x"], config3["issue_day"]["y"]), config3["issue_day"]["font_size"])
        self.template.save(f"{output_prefix}_3.png")

        # PDFファイルの生成
        self._generate_pdf(output_prefix)

    def _generate_pdf(self, output_prefix: str):
        """
        生成された3つの画像ファイルを1つのPDFにまとめる

        Args:
            output_prefix (str): 出力ファイルのプレフィックス
        """
        # 画像ファイルのパス
        image_paths = [
            f"{output_prefix}_1.png",
            f"{output_prefix}_2.png",
            f"{output_prefix}_3.png"
        ]

        # 画像を開く
        images = [Image.open(path) for path in image_paths]

        # PDFファイルのパス
        pdf_path = f"{output_prefix}.pdf"

        # 最初の画像をRGBモードに変換（PDF生成に必要）
        images[0] = images[0].convert('RGB')

        # PDFファイルを生成
        images[0].save(
            pdf_path,
            save_all=True,
            append_images=[img.convert('RGB') for img in images[1:]],
            resolution=100.0
        )

        # 画像ファイルを閉じる
        for img in images:
            img.close()

        # 個別の画像ファイルを削除
        for path in image_paths:
            os.remove(path)
