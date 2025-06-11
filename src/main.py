import os
import csv
import argparse

from config.config import DRIVER_LICENSE_CONFIG, INDIVIDUAL_NUMBER_CONFIG, TEMPLATE_PATHS
from generators.generators import DriverLicenseGenerator, IndividualNumberCardGenerator
from utils.utils import (
    format_name_for_driver_license,
    format_name_for_individual_number_card,
    get_filename,
    convert_to_western_year,
)


def main():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="運転免許証とマイナンバーカードを生成します")
    parser.add_argument("csv_file", help="データを含むCSVファイルのパス")
    args = parser.parse_args()

    # 出力ディレクトリの作成
    os.makedirs("output", exist_ok=True)

    # CSVファイルからデータを読み込む
    with open(args.csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            base_data = {
                "name": format_name_for_driver_license(name),
                "address": row["address"],
                "birth_date": {"year": row["birth_year"], "month": row["birth_month"], "day": row["birth_day"]},
                "sex": row["sex"],
                "expired_date": {
                    "year": row["expired_year"],
                    "western_year": convert_to_western_year(row["expired_year"]),
                    "month": row["expired_month"],
                    "day": row["expired_day"],
                },
            }

            # 運転免許証用のデータを準備
            driver_license_data = base_data.copy()
            driver_license_data["config"] = DRIVER_LICENSE_CONFIG

            # 運転免許証の生成
            driver_license_generator = DriverLicenseGenerator(TEMPLATE_PATHS["driver_license"], TEMPLATE_PATHS["font"])
            driver_license_path = os.path.join("output", get_filename(name, "運転免許証"))
            driver_license_generator.generate_license(driver_license_data, driver_license_path)
            print(f"運転免許証生成完了: {driver_license_path}")

            # マイナンバーカード用のデータを準備
            individual_number_data = base_data.copy()
            individual_number_data["name"] = format_name_for_individual_number_card(name)
            individual_number_data["config"] = INDIVIDUAL_NUMBER_CONFIG

            # マイナンバーカードの生成
            individual_number_generator = IndividualNumberCardGenerator(
                TEMPLATE_PATHS["individual_number"], TEMPLATE_PATHS["font"]
            )
            individual_number_path = os.path.join("output", get_filename(name, "マイナンバーカード"))
            individual_number_generator.generate_card(individual_number_data, individual_number_path)
            print(f"マイナンバーカード生成完了: {individual_number_path}")


if __name__ == "__main__":
    main()
