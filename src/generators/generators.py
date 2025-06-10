from typing import Any, Dict, Tuple

from PIL import Image, ImageDraw, ImageFont


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