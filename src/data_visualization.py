import pandas as pd
import matplotlib.pyplot as plt

def load_data(filepath):
    return pd.read_csv(filepath)

def plot_boxplot(df, column):
    plt.figure(figsize=(6, 4))
    plt.boxplot(df[column])
    plt.title(f'{column} 箱形圖')
    plt.show()

def plot_line_chart(df, x_column, y_column):
    plt.figure(figsize=(6, 4))
    plt.plot(df[x_column], df[y_column])
    plt.title(f'{y_column} 隨 {x_column} 的折線圖')
    plt.xticks(rotation=45)
    plt.show()

def plot_scatter_plot(df, x_column, y_column):
    plt.figure(figsize=(6, 4))
    plt.scatter(df[x_column], df[y_column])
    plt.title(f'{x_column} 與 {y_column} 的散點圖')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

# 假設您的數據文件名為 'ad_performance.csv'
# df = load_data('ad_performance.csv')
# plot_boxplot(df, '點擊次數')
# plot_line_chart(df, '日期', '曝光次數')
# plot_scatter_plot(df, '曝光次數', '點擊次數')
