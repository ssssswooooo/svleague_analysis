# 🏐 SVリーグ男子バレーボール優勝決定戦データ分析

[![Python Version](https://img.shields.io/badge/python-3.13.3-blue.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://pypi.org/)

[![pandas](https://img.shields.io/badge/pandas-2.2.3-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.1-11557c.svg)](https://matplotlib.org/)

このプロジェクトは、SVリーグ男子バレーボール2024-2025シーズンの優勝決定戦（サントリーサンバーズ大阪 vs ジェイテクトSTINGS愛知）の選手データを分析・可視化するためのものです。

## 📊 プロジェクト概要

SVリーグの公式データを基に、両チームの得点構成、選手個人の得点能力、チーム全体の戦力バランスを多角的に分析します。特に優勝決定戦に向けた両チームの強みと特徴を明らかにすることを目的としています。

## 🎯 主な分析内容

- 📈 両チームの総得点と得点構成の比較
- 🏃‍♂️ 主力選手の得点パターン分析
- 📊 チーム内の得点分散度合いの評価  
- 🔥 サーブとブロックの特徴的な選手の抽出
- 📌 セットあたり・試合あたりの得点効率分析

## 🚀 インストール・環境構築

### 1. リポジトリのクローン

```bash
git clone https://github.com/ssssswooooo/svleague_analysis.git
cd svleague_analysis
```

### 2. 仮想環境の作成（推奨）

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 必要なパッケージのインストール

```bash
pip install -r requirements.txt
```

## 📁 ディレクトリ構成

```
svleague_analysis/
├── 📂 data/              # 分析用データファイル
├── 📓 notebooks/         # Jupyter Notebook
├── 📂 scripts/           # 分析・可視化スクリプト
│   ├── analyze_finals.py      # 優勝決定戦の詳細分析
│   └── visualize_teams.py     # チーム比較可視化
├── 📂 output/            # 生成されたグラフ・分析結果
├── 📄 requirements.txt   # 依存パッケージ一覧
├── 📄 .gitignore        
└── 📄 README.md          
```

## 💻 使用方法

### 1. 優勝決定戦の分析実行

```bash
python scripts/analyze_finals.py
```

**実行結果:**
- ✅ チーム間の詳細な得点分析結果をコンソールに出力
- 📊 チーム得点構成の比較グラフ
- 📈 トップ選手のレーダーチャート比較
- 📊 サーブ・ブロック得点の特徴分析

### 2. チーム可視化の実行

```bash
python scripts/visualize_teams.py
```

**実行結果:**  
- 📊 チームの総得点と得点構成の円グラフ
- 📈 主力選手の得点パターン比較
- 📊 得点効率の散布図分析

### 3. Jupyter Notebookでのインタラクティブな分析

```bash
jupyter notebook notebooks/team_analysis.ipynb
```

## 📊 分析結果・出力ファイル

`output/`ディレクトリに以下のグラフが生成されます：

| ファイル名 | 説明 |
|------------|------|
| `team_composition.png` | チーム得点構成の比較 |
| `top_players_radar.png` | 主力選手の能力レーダーチャート |
| `serve_block_analysis.png` | サーブ・ブロック得点分析 |
| `score_distribution.png` | 得点分散度分析 |
| `team_comparison.png` | チーム全体の比較 |
| `top_players_comparison.png` | 主力選手の得点内訳 |
| `scoring_efficiency.png` | 得点効率の散布図 |

## 📚 データソース

- 📊 SVリーグ公式サイトの2024-2025シーズン選手データ
- 🏆 優勝決定戦出場チーム：
  - 🔶 サントリーサンバーズ大阪
  - 🔴 ジェイテクトSTINGS愛知

## 🛠️ 主な使用技術・ライブラリ

### コアライブラリ
![Python](https://img.shields.io/badge/Python-3.13.3-3776AB.svg?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.2.3-150458.svg?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.2.5-013243.svg?logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-F7931E.svg?logo=scikit-learn&logoColor=white)

### 可視化ライブラリ
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.1-11557c.svg)
![seaborn](https://img.shields.io/badge/seaborn-0.13.2-3776AB.svg)
![japanize-matplotlib](https://img.shields.io/badge/japanize--matplotlib-1.1.3-orange.svg)

### 開発環境
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg?logo=jupyter&logoColor=white)
![VSCode](https://img.shields.io/badge/VSCode-Recommended-007ACC.svg?logo=visual-studio-code&logoColor=white)

## ⭐ 注目の分析ポイント

1. 🏆 **トップスコアラー対決**: ドミトリー・ムセルスキー vs トリー・デファルコ
2. 🛡️ **ブロック力の差**: 両チームのディフェンス戦略の違い
3. 📊 **得点集中度**: トップ選手への依存度の比較
4. ⚖️ **チームバランス**: アタック・ブロック・サーブの比率分析

## 📋 必要な環境

![Python](https://img.shields.io/badge/Python-3.13.3+-3776AB.svg?logo=python&logoColor=white)
![pip](https://img.shields.io/badge/pip-Latest-3775A9.svg?logo=pypi&logoColor=white)
![venv](https://img.shields.io/badge/venv-Recommended-green.svg)
![OS](https://img.shields.io/badge/OS-Linux%20%7C%20macOS%20%7C%20Windows-blue.svg)

## 🔧 開発環境のセットアップ

```bash
# 仮想環境の作成
python -m venv venv

# 仮想環境の有効化
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 依存パッケージのインストール
pip install -r requirements.txt
```

## 🙏 謝辞

- SVリーグ公式サイトのデータ提供に感謝します
- 分析にあたり参考にした各種バレーボール統計手法

---

⭐ このプロジェクトが役に立ったら、スターをお願いします！
