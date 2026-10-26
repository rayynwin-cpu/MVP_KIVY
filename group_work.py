import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("AMAZON_Order.csv")

# df['Total Price'].plot(kind='hist', bins=7, color='teal', edgecolor='black')

# plt.title('Total')
# plt.xlabel('Price')
# plt.ylabel('Quantity')
# plt.grid(axis='y', linestyle='--', alpha=0.9)

# plt.tight_layout()
# plt.savefig('Total Price.png')
# plt.show()
# plt.close()


# race_counts = df['Total'].value_counts().sort_index()
# fig, ax = plt.subplots(figsize=(8, 5))
# race_counts.plot(kind='barh', color='skyblue', edgecolor='black', ax=ax)

# ax.set_title('Total', fontsize=14, fontweight='bold')
# ax.set_xlabel('Price', fontsize=12)
# ax.set_ylabel('Quantity', fontsize=12)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
# ax.grid(axis='y', linestyle='--', alpha=0.7)

# plt.tight_layout()
# plt.savefig('Total Price2.png')
# # plt.show()
# plt.close()

# plt.figure(figsize=(8, 5))


# group_counts = df['Total'].value_counts()

# fig, ax = plt.subplots(figsize=(6, 6))

# ax.pie(
#     group_counts,
#     labels=group_counts.index,
#     autopct='%1.1f%%',
#     startangle=90,
#     colors=['skyblue', 'lightgreen', 'salmon', 'gold', 'orchid'],
#     wedgeprops={'edgecolor': 'black', 'linewidth': 1}
# )

# ax.set_title('Total', fontsize=14, fontweight='bold', pad=15)

# plt.tight_layout()
# plt.savefig('Total Price3.png')
# plt.show()
# plt.close()


# fig, ax = plt.subplots(figsize=(8, 6))
# ax.scatter(
#     df['Price'],
#     df['Quantity'], 
#     color='teal', edgecolor='black', 
#     s=100, 
#     alpha=0.8
#     )

# ax.set_title('Total', fontsize=14, fontweight='bold', pad=15)
# ax.set_xlabel('Price', fontsize=12)
# ax.set_ylabel('Quantity', fontsize=12)
# ax.grid(True, linestyle=':', alpha=0.6)

# plt.tight_layout()
# plt.savefig('Total Price4.png')
# # plt.show()
# plt.close()


fig, ax = plt.subplots(figsize=(8, 6))
sorted_categories = sorted(df['race/ethnicity'].dropna().unique())

grouped_data = [df[df['race/ethnicity'] == category]['reading score'].dropna() for category in sorted_categories]

ax.boxplot(
    grouped_data,
    labels=sorted_categories,
    patch_artist=True,
    boxprops={'facecolor': 'lightblue', 'edgecolor': 'black'},
    medianprops={'color': 'red', 'linewidth': 2},
    whiskerprops={'color': 'gray', 'linestyle': '--'},
    capprops={'color': 'black'},
    flierprops={'marker': 'o', 'markerfacecolor': 'salmon', 'markersize': 6}
)

ax.set_title('Reading Scores Distribution by Race/Ethnicity Group', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Race/Ethnicity Group', fontsize=12)
ax.set_ylabel('Reading Score', fontsize=12)
ax.grid(True, axis='y', linestyle=':', alpha=0.5)

plt.tight_layout()
plt.savefig('ethnicity_boxplot.png')
# plt.show()
plt.close()
