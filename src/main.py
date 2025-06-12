import os
import csv
import argparse
from typing import Dict, Any

from config.config import (
    DRIVER_LICENSE_CONFIG,
    INDIVIDUAL_NUMBER_CONFIG,
    CERTIFICATE_OF_REGISTERED_MATTERS_CONFIGS,
    TEMPLATE_PATHS,
)
from generators.generators import (
    DriverLicenseGenerator,
    IndividualNumberCardGenerator,
    CertificateOfRegisteredMattersGenerator,
)
from utils.utils import (
    format_name_for_driver_license,
    format_name_for_individual_number_card,
    get_filename,
    convert_to_western_year,
    format_month_day,
)


def process_driver_license_data(row: Dict[str, str]) -> Dict[str, Any]:
    """運転免許証用のデータを準備"""
    name = row["name"]
    return {
        "name": format_name_for_driver_license(name),
        "address": row["address"],
        "birth_date": {
            "year": row["birth_year"],
            "month": format_month_day(row["birth_month"]),
            "day": format_month_day(row["birth_day"]),
        },
        "sex": row["sex"],
        "expired_date": {
            "year": row["expired_year"],
            "western_year": convert_to_western_year(row["expired_year"]),
            "month": format_month_day(row["expired_month"]),
            "day": format_month_day(row["expired_day"]),
        },
        "config": DRIVER_LICENSE_CONFIG,
    }


def process_individual_number_data(row: Dict[str, str]) -> Dict[str, Any]:
    """マイナンバーカード用のデータを準備"""
    name = row["name"]
    base_data = process_driver_license_data(row)
    base_data["name"] = format_name_for_individual_number_card(name)
    base_data["config"] = INDIVIDUAL_NUMBER_CONFIG
    return base_data


def process_certificate_data(row: Dict[str, str]) -> Dict[str, Any]:
    """履歴事項全部証明書用のデータを準備"""
    return {
        "company_name": row["company_name"],
        "company_address": row["company_address"],
        "corporate_number": row["corporate_number"],
        "representative_name": row["representative_name"],
        "issue_year": row["issue_year"],
        "issue_month": row["issue_month"],
        "issue_day": row["issue_day"],
    }


def main():
    # コマンドライン引数の設定
    parser = argparse.ArgumentParser(description="運転免許証、マイナンバーカード、履歴事項全部証明書を生成します")
    parser.add_argument("csv_file", help="データを含むCSVファイルのパス")
    parser.add_argument(
        "--type",
        choices=["driver_license", "individual_number", "certificate"],
        required=True,
        help="生成する書類の種類（driver_license: 運転免許証, individual_number: マイナンバーカード, certificate: 履歴事項全部証明書）",
    )
    args = parser.parse_args()

    # 出力ディレクトリの作成
    os.makedirs("output", exist_ok=True)

    # CSVファイルからデータを読み込む
    with open(args.csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSVファイルにヘッダーが存在しません。")

        for row in reader:
            if args.type == "certificate":
                # 履歴事項全部証明書の生成
                data = process_certificate_data(row)
                generator = CertificateOfRegisteredMattersGenerator(TEMPLATE_PATHS["font"])
                output_prefix = os.path.join("output", f"{row['company_name']}_履歴事項全部証明書")
                generator.generate_certificates(data, output_prefix)
                print(f"履歴事項全部証明書生成完了: {output_prefix}_1.png, {output_prefix}_2.png, {output_prefix}_3.png")

            elif args.type == "driver_license":
                # 運転免許証の生成
                data = process_driver_license_data(row)
                generator = DriverLicenseGenerator(TEMPLATE_PATHS["driver_license"], TEMPLATE_PATHS["font"])
                output_path = os.path.join("output", get_filename(row["name"], "運転免許証"))
                generator.generate_license(data, output_path)
                print(f"運転免許証生成完了: {output_path}")

            elif args.type == "individual_number":
                # マイナンバーカードの生成
                data = process_individual_number_data(row)
                generator = IndividualNumberCardGenerator(TEMPLATE_PATHS["individual_number"], TEMPLATE_PATHS["font"])
                output_path = os.path.join("output", get_filename(row["name"], "マイナンバーカード"))
                generator.generate_card(data, output_path)
                print(f"マイナンバーカード生成完了: {output_path}")


if __name__ == "__main__":
    main()
