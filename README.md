# ダミー運転免許証ジェネレーター

このプロジェクトは、テスト用のダミー運転免許証画像を生成するためのPythonツールです。

## 機能

- テンプレート画像を使用して運転免許証を生成
- カスタマイズ可能なテキスト配置
- フォントサイズと色のカスタマイズ
- 日本語フォント対応

## 必要条件

- Python 3.6以上
- uv (Pythonパッケージマネージャー)
- Pillow (PIL)

## インストール

1. リポジトリをクローン:
```bash
git clone https://github.com/yourusername/dummy-image-generator.git
cd dummy-image-generator
```

2. 必要なパッケージをインストール:
```bash
uv sync
```

## 使用方法

1. `templates`ディレクトリに運転免許証のテンプレート画像を配置
2. `fonts`ディレクトリに使用したいフォントファイルを配置
3. 以下のようにPythonスクリプトを実行:

```python
from main import DriverLicenseGenerator

# ジェネレーターの初期化
generator = DriverLicenseGenerator(
    template_path="templates/driver_license_template.png",
    font_path="fonts/NotoSansJP-Regular.ttf"
)

# 運転免許証データの設定
data = {
    "name": "山　田　　太　郎",
    "address": "東京都渋谷区渋谷１−１−１",
    "birth_date": {
        "year": "昭和51",
        "month": "12",
        "day": "12"
    }
}

# 運転免許証の生成
generator.generate_license(data, "output/driver_license.png")
```

## プロジェクト構造

```
dummy-image-generator/
├── main.py              # メインスクリプト
├── templates/           # テンプレート画像ディレクトリ
├── fonts/              # フォントファイルディレクトリ
└── output/             # 生成された画像の出力ディレクトリ
```

## 注意事項

- このツールはテスト目的でのみ使用してください
- 生成された画像は本物の運転免許証として使用しないでください
- 個人情報の取り扱いには十分注意してください

## ライセンス

MIT License
