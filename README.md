# ダミー画像生成ツール

運転免許証、マイナンバーカード、履歴事項全部証明書のダミー画像を生成するPythonツールです。

## 機能

- 運転免許証のダミー画像生成
- マイナンバーカードのダミー画像生成
- 履歴事項全部証明書のダミー画像生成（PDF形式）
- CSVファイルからの一括生成
- 和暦・西暦の自動変換
- カスタマイズ可能なフォントサイズと位置設定

## 必要条件

- Python 3.13以上
- [uv](https://github.com/astral-sh/uv) (Pythonパッケージマネージャー)
- Pillow (PIL Fork)

## セットアップ

1. リポジトリをクローン:
```bash
git clone https://github.com/miya10kei/dummy-image-generator.git
cd dummy-image-generator
```

2. 必要なパッケージをインストール:
```bash
uv sync
```

3. 必要なディレクトリとファイルを配置:
```
dummy-image-generator/
├── templates/
│   ├── driver_license_template.png  # 運転免許証のテンプレート画像
│   ├── individual_number_card_template.png  # マイナンバーカードのテンプレート画像
│   ├── certificate_of_registered_matters_template_1.png  # 履歴事項全部証明書（1ページ目）
│   ├── certificate_of_registered_matters_template_2.png  # 履歴事項全部証明書（2ページ目）
│   └── certificate_of_registered_matters_template_3.png  # 履歴事項全部証明書（3ページ目）
├── fonts/
│   └── NotoSansJP-Regular.ttf  # 日本語フォント
└── output/  # 生成された画像の出力先
```

## 使用方法

1. CSVファイルを準備:

運転免許証・マイナンバーカード用:
```csv
name,address,birth_year,birth_month,birth_day,sex,expired_year,expired_month,expired_day
山田　太郎,東京都渋谷区渋谷１−１−１,昭和51,12,12,男,令和10,12,12
佐藤　花子,東京都新宿区西新宿２−２−２,平成5,3,15,女,令和15,3,15
鈴木　一郎,東京都千代田区丸の内３−３−３,昭和63,7,7,男,令和13,7,7
```

履歴事項全部証明書用:
```csv
company_name,company_address,corporate_number,representative_name,issue_year,issue_month,issue_day
株式会社サンプル,東京都渋谷区渋谷１−１−１,1234567890123,山田太郎,令和6,3,15
```

2. スクリプトを実行:

運転免許証の生成:
```bash
uv run src/main.py data.csv --type driver_license
```

マイナンバーカードの生成:
```bash
uv run src/main.py data.csv --type individual_number
```

履歴事項全部証明書の生成:
```bash
uv run src/main.py data.csv --type certificate
```

3. 生成されたファイルは`output`ディレクトリに保存されます。
   - 運転免許証・マイナンバーカード: PNG形式の画像ファイル
   - 履歴事項全部証明書: PDF形式のファイル（3ページ）

## プロジェクト構造

```
dummy-image-generator/
├── src/
│   ├── __init__.py
│   ├── main.py              # メインスクリプト
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py        # 設定ファイル
│   ├── generators/
│   │   ├── __init__.py
│   │   └── generators.py    # カード生成クラス
│   └── utils/
│       ├── __init__.py
│       └── utils.py         # ユーティリティ関数
├── templates/               # テンプレート画像
├── fonts/                  # フォントファイル
└── output/                 # 出力ディレクトリ
```

## カスタマイズ

### フォントサイズと位置の変更

`src/config/config.py`の以下の設定を変更することで、フォントサイズと位置を調整できます：

```python
driver_license_config = {
    "name": {"position": (50, 17), "font_size": 24},
    "address": {"position": (50, 46), "font_size": 20},
    # ...
}

individual_number_config = {
    "name": {"position": (50, 17), "font_size": 16},
    "address": {"position": (50, 46), "font_size": 18},
    # ...
}

certificate_of_registered_matters_configs = {
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
```

## 注意事項

- このツールはテスト目的でのみ使用してください
- 生成された画像は個人情報を含むため、適切に管理してください
- テンプレート画像は著作権に注意して使用してください

## ライセンス

MITライセンス
