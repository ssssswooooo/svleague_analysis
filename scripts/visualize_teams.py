import japanize_matplotlib  # noqa: F401
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

"""
SVリーグチーム可視化スクリプト
サントリーサンバーズ大阪 vs ジェイテクトSTINGS愛知の得点データの可視化
"""

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

def create_team_comparison_chart(df):
    """チームごとの得点構成比較グラフを作成"""
    # 対象チームを定義
    team1 = "サントリーサンバーズ大阪"
    team2 = "ジェイテクトSTINGS愛知"

    # 各チームの選手データを抽出
    suntory = df[df['チーム名'] == team1]
    jtekt = df[df['チーム名'] == team2]

    # チームごとの得点合計を計算
    team_stats = []

    for team_name, team_df in [(team1, suntory), (team2, jtekt)]:
        total_points = team_df['総得点'].sum()
        attack_points = team_df['アタック'].sum()
        block_points = team_df['ブロック'].sum()
        serve_points = team_df['サーブ'].sum()

        team_stats.append({
            'チーム': team_name,
            'アタック': attack_points,
            'ブロック': block_points,
            'サーブ': serve_points,
            '総得点': total_points,
            'アタック割合': attack_points / total_points * 100,
            'ブロック割合': block_points / total_points * 100,
            'サーブ割合': serve_points / total_points * 100
        })

    team_df = pd.DataFrame(team_stats)

    # 可視化
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # 左側：得点合計の棒グラフ
    sns.barplot(x='チーム', y='総得点', data=team_df, ax=ax1, palette='viridis', hue='チーム', legend=False)
    ax1.set_title('チーム総得点比較')
    ax1.set_ylabel('総得点')

    # 得点の数値を表示
    for i, total in enumerate(team_df['総得点']):
        ax1.text(i, total + 50, f"{total:.0f}", ha='center', va='bottom', fontweight='bold')

    # 右側：得点構成の円グラフ
    categories = ['アタック割合', 'ブロック割合', 'サーブ割合']
    colors = ['#3498DB', '#E74C3C', '#F1C40F']

    # サントリーの円グラフ
    suntory_data = team_df.iloc[0][categories].values
    jtekt_data = team_df.iloc[1][categories].values

    # 円グラフのサブプロット
    ax2.remove()  # 既存のaxを削除
    ax2 = fig.add_subplot(122)

    # 2つの円グラフを1つのサブプロットに表示
    wedges1, texts1, autotexts1 = ax2.pie(
        suntory_data,
        autopct='%1.1f%%',
        radius=0.5,
        pctdistance=0.85,
        colors=colors,
        wedgeprops=dict(width=0.3, edgecolor='w'),
        startangle=90,
        counterclock=False,
        textprops={'fontsize': 8}
    )

    wedges2, texts2, autotexts2 = ax2.pie(
        jtekt_data,
        autopct='%1.1f%%',
        radius=0.8,
        pctdistance=0.85,
        colors=[c + '80' for c in colors],  # 少し透明にする
        wedgeprops=dict(width=0.3, edgecolor='w'),
        startangle=90,
        counterclock=False,
        textprops={'fontsize': 8}
    )

    # 凡例の作成
    ax2.legend(
        wedges1,
        categories,
        title="得点構成",
        loc="center",
        bbox_to_anchor=(0.5, 0)
    )

    # 内側と外側のチーム名を表示
    ax2.text(0, 0, team1, ha='center', va='center', fontsize=10, fontweight='bold')
    ax2.text(0, 0.9, team2, ha='center', va='center', fontsize=10, fontweight='bold')

    ax2.set_title('チーム得点構成比較')

    plt.tight_layout()
    output_path = 'output/team_comparison.png'
    plt.savefig(output_path)
    print(f"チーム比較グラフを保存しました: {output_path}")
    plt.close()

    return team_df

def visualize_player_comparison(df):
    """主力選手の得点比較可視化"""
    # 対象チームを定義
    team1 = "サントリーサンバーズ大阪"
    team2 = "ジェイテクトSTINGS愛知"

    # 各チームの選手データを抽出
    suntory = df[df['チーム名'] == team1].reset_index(drop=True)
    jtekt = df[df['チーム名'] == team2].reset_index(drop=True)

    # トップ3選手を抽出
    suntory_top3 = suntory.head(3)
    jtekt_top3 = jtekt.head(3)

    # 選手名を取得
    suntory_players = suntory_top3['氏名'].tolist()
    jtekt_players = jtekt_top3['氏名'].tolist()

    # データ準備
    suntory_attack = suntory_top3['アタック'].tolist()
    suntory_block = suntory_top3['ブロック'].tolist()
    suntory_serve = suntory_top3['サーブ'].tolist()

    jtekt_attack = jtekt_top3['アタック'].tolist()
    jtekt_block = jtekt_top3['ブロック'].tolist()
    jtekt_serve = jtekt_top3['サーブ'].tolist()

    # 可視化
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # サントリー選手の可視化
    x1 = np.arange(len(suntory_players))
    bar_width = 0.6

    ax1.bar(x1, suntory_attack, bar_width, label='アタック', color='#3498DB')
    ax1.bar(x1, suntory_block, bar_width, bottom=suntory_attack, label='ブロック', color='#E74C3C')
    ax1.bar(x1, suntory_serve, bar_width, bottom=[a+b for a, b in zip(suntory_attack, suntory_block)], label='サーブ', color='#F1C40F')

    ax1.set_title(f'{team1} トップ選手')
    ax1.set_ylabel('得点')
    ax1.set_xticks(x1)
    ax1.set_xticklabels(suntory_players)
    ax1.legend()

    # 得点を表示
    for i, player in enumerate(suntory_top3.itertuples()):
        ax1.text(i, 50, f"総得点: {player.総得点}", ha='center')

    # ジェイテクト選手の可視化
    x2 = np.arange(len(jtekt_players))

    ax2.bar(x2, jtekt_attack, bar_width, label='アタック', color='#3498DB')
    ax2.bar(x2, jtekt_block, bar_width, bottom=jtekt_attack, label='ブロック', color='#E74C3C')
    ax2.bar(x2, jtekt_serve, bar_width, bottom=[a+b for a, b in zip(jtekt_attack, jtekt_block)], label='サーブ', color='#F1C40F')

    ax2.set_title(f'{team2} トップ選手')
    ax2.set_ylabel('得点')
    ax2.set_xticks(x2)
    ax2.set_xticklabels(jtekt_players)
    ax2.legend()

    # 得点を表示
    for i, player in enumerate(jtekt_top3.itertuples()):
        ax2.text(i, 50, f"総得点: {player.総得点}", ha='center')

    plt.tight_layout()
    output_path = 'output/top_players_comparison.png'
    plt.savefig(output_path)
    print(f"選手比較グラフを保存しました: {output_path}")
    plt.close()

    return suntory_top3, jtekt_top3

def visualize_scoring_efficiency(df):
    """セットあたり・試合あたりの得点効率の可視化"""
    # 対象チームを定義
    team1 = "サントリーサンバーズ大阪"
    team2 = "ジェイテクトSTINGS愛知"

    # 各チームの選手データを抽出
    suntory = df[df['チーム名'] == team1].reset_index(drop=True)
    jtekt = df[df['チーム名'] == team2].reset_index(drop=True)

    # トップ5選手を抽出
    suntory_top5 = suntory.head(5)
    jtekt_top5 = jtekt.head(5)

    # 効率データの準備
    efficiency_data = []

    for i, player in enumerate(suntory_top5.itertuples()):
        efficiency_data.append({
            '選手名': player.氏名,
            'チーム': team1,
            'セットあたり得点': player.セットあたり得点,
            '試合あたり得点': player.試合あたり得点,
            '総得点': player.総得点
        })

    for i, player in enumerate(jtekt_top5.itertuples()):
        efficiency_data.append({
            '選手名': player.氏名,
            'チーム': team2,
            'セットあたり得点': player.セットあたり得点,
            '試合あたり得点': player.試合あたり得点,
            '総得点': player.総得点
        })

    efficiency_df = pd.DataFrame(efficiency_data)

    # 可視化
    plt.figure(figsize=(12, 8))

    # チームごとに色分け
    colors = {'サントリーサンバーズ大阪': '#1F77B4', 'ジェイテクトSTINGS愛知': '#FF7F0E'}

    # 散布図（試合あたり得点 vs セットあたり得点）
    sns.scatterplot(
        data=efficiency_df,
        x='試合あたり得点',
        y='セットあたり得点',
        hue='チーム',
        size='総得点',
        sizes=(100, 500),
        alpha=0.7,
        palette=colors
    )

    # 選手名のラベル付け
    for i, row in efficiency_df.iterrows():
        plt.text(
            row['試合あたり得点'] + 0.2,
            row['セットあたり得点'],
            row['選手名'],
            fontsize=9
        )

    plt.title('得点効率比較')
    plt.xlabel('試合あたり得点')
    plt.ylabel('セットあたり得点')
    plt.grid(True, linestyle='--', alpha=0.7)

    # 可視化グラフの保存
    output_path = 'output/scoring_efficiency.png'
    plt.savefig(output_path)
    print(f"得点効率比較グラフを保存しました: {output_path}")
    plt.close()

    return efficiency_df

def main():
    """メイン関数"""
    # データの読み込み
    df = load_data()

    # チーム比較グラフの作成
    create_team_comparison_chart(df)

    # 選手比較グラフの作成
    visualize_player_comparison(df)

    # 得点効率比較グラフの作成
    visualize_scoring_efficiency(df)

    print("\n可視化が完了しました。output/ ディレクトリにグラフが保存されています。")

if __name__ == "__main__":
    main()
