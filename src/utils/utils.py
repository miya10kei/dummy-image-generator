import re


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


def format_representative_name(name: str) -> str:
    """
    代表者名用のフォーマット
    半角・全角スペースを除去した後、文字の間に全角スペース1つを挿入した形式に変換する

    Args:
        name (str): 変換前の名前

    Returns:
        str: 変換後の名前（各文字の間に全角スペース1つを挿入）
    """
    # 半角・全角スペースを除去
    name_without_spaces = name.replace(" ", "").replace("　", "")
    # 文字の間に全角スペースを挿入
    return "　".join(name_without_spaces)


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
    match = re.match(r"(令和|平成|昭和|大正|明治)(\d+)", year)
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


def format_month_day(value: str) -> str:
    """
    月または日を2桁の文字列にフォーマットする
    1桁の場合は先頭に半角スペースを追加する

    Args:
        value (str): 月または日の値

    Returns:
        str: フォーマットされた2桁の文字列
    """
    return f" {value}" if len(value) == 1 else value
