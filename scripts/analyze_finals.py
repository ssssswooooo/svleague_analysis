import japanize_matplotlib  # noqa: F401
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""
SVリーグ優勝決定戦分析スクリプト
サントリーサンバーズ大阪 vs ジェイテクトSTINGS愛知の得点データ分析
"""

# データの読み込み
def load_data(csv_path='data/svleague_data.csv'):
    """CSVファイルからデータを読み込み、前処理を行う"""
    print(f"データを読み込んでいます: {csv_path}")
    df = pd.read_csv(csv_path, encoding='utf-8')

    # 数値型に変換（念のため）
    numeric_columns = ['順位', '総得点', '試合数', 'セット数', 'アタック', 'ブロック', 'サーブ']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col])

    # 得点効率と構成比の計算
    df['試合あたり得点'] = df['総得点'] / df['試合数']
    df['セットあたり得点'] = df['総得点'] / df['セット数']
    df['アタック割合'] = df['アタック'] / df['総得点'] * 100
    df['ブロック割合'] = df['ブロック'] / df['総得点'] * 100
    df['サーブ割合'] = df['サーブ'] / df['総得点'] * 100

    print(f"データ読み込み完了: {len(df)}件")
    return df

# 優勝決定戦チームの分析
def analyze_finals_teams(df):
    """サントリーサンバーズ大阪とジェイテクトSTINGS愛知の比較分析"""
    # 2つのチーム名を定義
    team1 = "サントリーサンバーズ大阪"
    team2 = "ジェイテクトSTINGS愛知"

    # 各チームの選手データを抽出
    suntory = df[df['チーム名'] == team1].reset_index(drop=True)
    jtekt = df[df['チーム名'] == team2].reset_index(drop=True)

    # === 基本統計情報 ===
    print(f"\n=== {team1} vs {team2} の得点分析 ===")

    # 各チームの選手数
    print(f"\n{team1} 選手数: {len(suntory)}名")
    print(f"{team2} 選手数: {len(jtekt)}名")

    # 各チームの総得点合計（上位5名）
    suntory_total = suntory['総得点'].sum()
    jtekt_total = jtekt['総得点'].sum()
    print(f"\n{team1} 総得点合計: {suntory_total}点")
    print(f"{team2} 総得点合計: {jtekt_total}点")

    # トップ選手の表示
    print(f"\n{team1} トップ選手:")
    print(suntory[['氏名', '総得点', 'アタック', 'ブロック', 'サーブ']].head().to_string(index=False))

    print(f"\n{team2} トップ選手:")
    print(jtekt[['氏名', '総得点', 'アタック', 'ブロック', 'サーブ']].head().to_string(index=False))

    # === 得点構成の分析 ===
    # 各チームの得点構成の合計を計算
    suntory_attack = suntory['アタック'].sum()
    suntory_block = suntory['ブロック'].sum()
    suntory_serve = suntory['サーブ'].sum()

    jtekt_attack = jtekt['アタック'].sum()
    jtekt_block = jtekt['ブロック'].sum()
    jtekt_serve = jtekt['サーブ'].sum()

    # 得点構成の割合を計算
    suntory_attack_pct = suntory_attack / suntory_total * 100
    suntory_block_pct = suntory_block / suntory_total * 100
    suntory_serve_pct = suntory_serve / suntory_total * 100

    jtekt_attack_pct = jtekt_attack / jtekt_total * 100
    jtekt_block_pct = jtekt_block / jtekt_total * 100
    jtekt_serve_pct = jtekt_serve / jtekt_total * 100

    print(f"\n{team1} チーム全体の得点構成:")
    print(f"アタック: {suntory_attack}点 ({suntory_attack_pct:.1f}%)")
    print(f"ブロック: {suntory_block}点 ({suntory_block_pct:.1f}%)")
    print(f"サーブ: {suntory_serve}点 ({suntory_serve_pct:.1f}%)")
    print(f"総得点: {suntory_total}点")

    print(f"\n{team2} チーム全体の得点構成:")
    print(f"アタック: {jtekt_attack}点 ({jtekt_attack_pct:.1f}%)")
    print(f"ブロック: {jtekt_block}点 ({jtekt_block_pct:.1f}%)")
    print(f"サーブ: {jtekt_serve}点 ({jtekt_serve_pct:.1f}%)")
    print(f"総得点: {jtekt_total}点")

    # データフレームの作成（可視化用）
    team_stats = []
    for name, attack, block, serve, total in [
        (team1, suntory_attack, suntory_block, suntory_serve, suntory_total),
        (team2, jtekt_attack, jtekt_block, jtekt_serve, jtekt_total)
    ]:
        team_stats.append({
            'チーム': name,
            'アタック': attack,
            'ブロック': block,
            'サーブ': serve,
            '総得点': total,
            'アタック割合': attack / total * 100,
            'ブロック割合': block / total * 100,
            'サーブ割合': serve / total * 100
        })

    team_df = pd.DataFrame(team_stats)

    # === チーム得点構成の可視化 ===
    fig, ax = plt.subplots(figsize=(10, 6))

    # データ準備
    teams = [team1, team2]
    attack = [suntory_attack, jtekt_attack]
    block = [suntory_block, jtekt_block]
    serve = [suntory_serve, jtekt_serve]

    # 積み上げ棒グラフを作成
    bar_width = 0.5
    x = np.arange(len(teams))

    # プロット
    ax.bar(x, attack, bar_width, label='アタック', color='#3498DB')
    ax.bar(x, block, bar_width, bottom=attack, label='ブロック', color='#E74C3C')
    ax.bar(x, serve, bar_width, bottom=[a+b for a, b in zip(attack, block)], label='サーブ', color='#F1C40F')

    # グラフの体裁
    ax.set_xlabel('チーム')
    ax.set_ylabel('得点')
    ax.set_title('チーム別得点構成')
    ax.set_xticks(x)
    ax.set_xticklabels(teams)
    ax.legend()

    # 保存
    plt.tight_layout()
    output_path = 'output/team_composition.png'
    plt.savefig(output_path)
    print(f"\nチーム得点構成グラフを保存しました: {output_path}")
    plt.close()

    # === トップ選手の比較（レーダーチャート） ===
    # サントリーとジェイテクトのトップ選手を抽出
    suntory_top = suntory.iloc[0]  # ムセルスキー
    jtekt_top = jtekt.iloc[0]  # デファルコ

    # レーダーチャートの作成
    categories = ['アタック効率', 'ブロック貢献度', 'サーブ得点力', 'セット効率', '試合効率']

    # 正規化のための最大値
    max_values = {
        'アタック効率': max(suntory_top['アタック'] / suntory_top['セット数'], jtekt_top['アタック'] / jtekt_top['セット数']),
        'ブロック貢献度': max(suntory_top['ブロック'] / suntory_top['総得点'], jtekt_top['ブロック'] / jtekt_top['総得点']),
        'サーブ得点力': max(suntory_top['サーブ'] / suntory_top['セット数'], jtekt_top['サーブ'] / jtekt_top['セット数']),
        'セット効率': max(suntory_top['セットあたり得点'], jtekt_top['セットあたり得点']),
        '試合効率': max(suntory_top['試合あたり得点'], jtekt_top['試合あたり得点'])
    }

    # 正規化値の計算
    suntory_values = [
        (suntory_top['アタック'] / suntory_top['セット数']) / max_values['アタック効率'],
        (suntory_top['ブロック'] / suntory_top['総得点']) / max_values['ブロック貢献度'],
        (suntory_top['サーブ'] / suntory_top['セット数']) / max_values['サーブ得点力'],
        suntory_top['セットあたり得点'] / max_values['セット効率'],
        suntory_top['試合あたり得点'] / max_values['試合効率']
    ]

    jtekt_values = [
        (jtekt_top['アタック'] / jtekt_top['セット数']) / max_values['アタック効率'],
        (jtekt_top['ブロック'] / jtekt_top['総得点']) / max_values['ブロック貢献度'],
        (jtekt_top['サーブ'] / jtekt_top['セット数']) / max_values['サーブ得点力'],
        jtekt_top['セットあたり得点'] / max_values['セット効率'],
        jtekt_top['試合あたり得点'] / max_values['試合効率']
    ]

    # レーダーチャートの準備
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, polar=True)

    # 角度の計算
    N = len(categories)
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # 閉じるために最初の点を追加

    # 値リストも閉じる
    suntory_values += suntory_values[:1]
    jtekt_values += jtekt_values[:1]

    # プロット
    ax.plot(angles, suntory_values, 'b-', linewidth=2, label=f"{suntory_top['氏名']}")
    ax.fill(angles, suntory_values, 'b', alpha=0.1)
    ax.plot(angles, jtekt_values, 'r-', linewidth=2, label=f"{jtekt_top['氏名']}")
    ax.fill(angles, jtekt_values, 'r', alpha=0.1)

    # ラベルの追加
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)

    # タイトルと凡例
    plt.title('トップ選手比較')
    plt.legend(loc='upper right')

    # 保存
    output_path = 'output/top_players_radar.png'
    plt.savefig(output_path)
    print(f"トップ選手比較レーダーチャートを保存しました: {output_path}")
    plt.close()

    # === 特徴的な選手の分析 ===
    # サーブ得点が高い選手
    suntory_top_server = suntory.sort_values('サーブ', ascending=False).iloc[0]
    jtekt_top_server = jtekt.sort_values('サーブ', ascending=False).iloc[0]

    print("\nサーブ得点トップの選手:")
    print(f"{team1}: {suntory_top_server['氏名']} ({suntory_top_server['サーブ']}点)")
    print(f"{team2}: {jtekt_top_server['氏名']} ({jtekt_top_server['サーブ']}点)")

    # ブロック得点が高い選手
    suntory_top_blocker = suntory.sort_values('ブロック', ascending=False).iloc[0]
    jtekt_top_blocker = jtekt.sort_values('ブロック', ascending=False).iloc[0]

    print("\nブロック得点トップの選手:")
    print(f"{team1}: {suntory_top_blocker['氏名']} ({suntory_top_blocker['ブロック']}点)")
    print(f"{team2}: {jtekt_top_blocker['氏名']} ({jtekt_top_blocker['ブロック']}点)")

    # サーブとブロックの可視化
    server_names = [suntory_top_server['氏名'], jtekt_top_server['氏名']]
    server_values = [suntory_top_server['サーブ'], jtekt_top_server['サーブ']]
    server_colors = ['#3498DB', '#E74C3C']

    blocker_names = [suntory_top_blocker['氏名'], jtekt_top_blocker['氏名']]
    blocker_values = [suntory_top_blocker['ブロック'], jtekt_top_blocker['ブロック']]
    blocker_colors = ['#3498DB', '#E74C3C']

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # サーブグラフ
    ax1.bar(server_names, server_values, color=server_colors)
    ax1.set_title('サーブ得点比較')
    ax1.set_ylabel('得点')

    # ブロックグラフ
    ax2.bar(blocker_names, blocker_values, color=blocker_colors)
    ax2.set_title('ブロック得点比較')
    ax2.set_ylabel('得点')

    plt.tight_layout()
    output_path = 'output/serve_block_analysis.png'
    plt.savefig(output_path)
    print(f"サーブ・ブロック分析グラフを保存しました: {output_path}")
    plt.close()

    # === チーム間の得点分散度合いの分析 ===
    suntory_top3_pct = suntory.head(3)['総得点'].sum() / suntory_total * 100
    jtekt_top3_pct = jtekt.head(3)['総得点'].sum() / jtekt_total * 100

    print("\n得点集中度（トップ3選手の得点割合）:")
    print(f"{team1}: {suntory_top3_pct:.1f}%")
    print(f"{team2}: {jtekt_top3_pct:.1f}%")

    # 得点分散の可視化
    top_n = min(len(suntory), len(jtekt))

    # 累積得点割合の計算
    suntory_cum = np.cumsum(suntory['総得点'][:top_n]) / suntory_total * 100
    jtekt_cum = np.cumsum(jtekt['総得点'][:top_n]) / jtekt_total * 100

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, top_n+1), suntory_cum, 'b-', marker='o', label=team1)
    plt.plot(range(1, top_n+1), jtekt_cum, 'r-', marker='s', label=team2)
    plt.xlabel('選手数（得点順）')
    plt.ylabel('累積得点割合（%）')
    plt.title('得点分散度分析')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # 保存
    output_path = 'output/score_distribution.png'
    plt.savefig(output_path)
    print(f"得点分散度分析グラフを保存しました: {output_path}")
    plt.close()

    # === 分析結果のまとめ ===
    print("\n=== 優勝決定戦の見どころ（得点面） ===")

    # 注目の対決ポイントを抽出
    print("• トップスコアラー対決: ドミトリー・ムセルスキー vs トリー・デファルコ")
    print("• サーブ対決: デアルマス アライン vs 宮浦 健人")

    # 両チームの得点タイプによる戦略予想
    if suntory_block_pct > jtekt_block_pct:
        print(f"• {team1}のブロック力とディフェンスによる守備が鍵")
    else:
        print(f"• {team2}のブロック力とディフェンスによる守備が鍵")

    if suntory_serve_pct > jtekt_serve_pct:
        print(f"• {team1}のサーブ得点能力がラリー展開に影響を与えるか注目")
    else:
        print(f"• {team2}のサーブ得点能力がラリー展開に影響を与えるか注目")

    if suntory_top3_pct > jtekt_top3_pct:
        print(f"• {team1}はトップ選手への得点依存度が高く、{team2}の対策次第で試合展開が左右される")
    else:
        print(f"• {team2}はトップ選手への得点依存度が高く、{team1}の対策次第で試合展開が左右される")

    return team_df, suntory, jtekt

def main():
    """メイン関数"""
    # データの読み込み
    df = load_data()

    # 優勝決定戦チームの分析
    analyze_finals_teams(df)

    print("\n分析が完了しました。output/ ディレクトリに可視化結果が保存されています。")

if __name__ == "__main__":
    main()
