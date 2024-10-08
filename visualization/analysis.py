import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import seaborn as sns
import os

import warnings
warnings.filterwarnings("ignore")

def get_charts(dataset, root_path):
    # Total pie chart (accepted/not accepted)
    total_accepted = dataset['Accepted'].value_counts()['Accepted']
    total_not_accepted = dataset['Accepted'].value_counts().get('Not Accepted', 0)  # Handle cases where there may be no 'Not Accepted'

    fig1, ax1 = plt.subplots()
    ax1.pie([total_accepted, total_not_accepted], autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#F44336'])
    ax1.set_title('Total Test Cases Accepted vs Not Accepted')
    plt.legend(['Accepted', 'Not Accepted'], loc='upper right')
    plt.savefig(f"{root_path}/total_accepted_not.jpg")
    print("Total Accepted/Not Accepted ... Done!")

    # Accepted/not accepted per topic
    topic_counts = defaultdict(lambda: [0, 0])  # [Accepted, Not Accepted] counts for each topic
    for index, row in dataset.iterrows():
        topics = row['topicTags'].split(',')
        for topic in topics:
            if row['Accepted'] == 'Accepted':
                topic_counts[topic][0] += 1
            else:
                topic_counts[topic][1] += 1

    myDict1 = {key: val for key, val in topic_counts.items() if val != [0, 0]}
    fig2, axes2 = plt.subplots(nrows=len(myDict1)//3+1, ncols=3, figsize=(15, 30))
    axes2 = axes2.flatten()

    for i, (topic, counts) in enumerate(myDict1.items()):
        axes2[i].pie([counts[0], counts[1]], autopct='%0.1f%%', startangle=90, colors=['#4CAF50', '#F44336'])
        axes2[i].set_title(topic)
    for j in range(i+1, len(axes2)):
        axes2[j].set_visible(False)

    plt.savefig(f"{root_path}/accepted_not_topicwise.jpg")
    print("Topic Accepted/Not Accepted ... Done!")

    # Difficulty Analysis including Errors
    fig3, axes3 = plt.subplots(1, 3, figsize=(18, 6))  # Adjust as necessary to fit the layout
    plt.legend(['Accepted', 'Not Accepted'], loc='upper right')
    colors = ['#4CAF50', '#F44336', '#FFC107']
    labels = ['Accepted', 'Not Accepted', 'Errors']

    for i, diff in enumerate(['Easy', 'Medium', 'Hard']):
        data = dataset.loc[dataset['difficulty'] == diff]
        data = data[['Accepted', 'Errors', 'topicTags', 'title']]

        total_accepted = data['Accepted'].value_counts()['Accepted']
        total_not_accepted = data['Accepted'].value_counts().get('Not Accepted', 0)
        total_errors = data['Errors'].sum()

        patches, texts, autotexts = axes3[i].pie([total_accepted, total_not_accepted, total_errors], labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        axes3[i].set_title(f'Test Cases - {diff}')

    fig3.legend(patches, labels, loc='upper right')
    plt.tight_layout()
    plt.savefig(f"{root_path}/pie_difficulty.jpg")

    print("Difficulty Analysis ... Done!")

def is_accepted(row):
    return 'Accepted' if row['Failed'] == 0 and row['Errors'] == 0 else 'Not Accepted'


def comparative_analysis(datasets, all_data, root_path):
    # topic wise acceptance
    provided_acceptance_rates = datasets[0][['QID', 'acceptanceRate', 'topicTags']].copy()
    provided_acceptance_rates['topicTags'] = provided_acceptance_rates['topicTags'].astype(str).str.split(',')

    expanded_provided_rates = provided_acceptance_rates.explode('topicTags')

    provided_topic_acceptance = expanded_provided_rates.groupby('topicTags').agg(
        Provided_Acceptance_Rate=pd.NamedAgg(column='acceptanceRate', aggfunc='mean')
    ).reset_index()

    all_data['topicTags'] = all_data['topicTags'].astype(str).str.split(',')
    expanded_all_data = all_data.explode('topicTags')

    calculated_topic_acceptance = expanded_all_data.groupby('topicTags').agg(
        Calculated_Acceptance_Rate=pd.NamedAgg(column='Accepted', aggfunc=lambda x: (x == 'Accepted').mean()*100)
    ).reset_index()

    topic_acceptance_comparison = pd.merge(provided_topic_acceptance, calculated_topic_acceptance, on='topicTags')

    # Visualization
    plt.figure(figsize=(14, 7))
    sns.barplot(x='topicTags', y='Provided_Acceptance_Rate', data=topic_acceptance_comparison, color='blue', label='Provided', alpha=0.6)
    sns.barplot(x='topicTags', y='Calculated_Acceptance_Rate', data=topic_acceptance_comparison, color='red', label='Calculated', alpha=0.6)

    plt.xticks(rotation=90)
    plt.xlabel('Topic Tags')
    plt.ylabel('Acceptance Rate (%)')
    plt.title('Topic-wise Comparison of Provided vs. Calculated Acceptance Rates')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{root_path}/acceptance_topic_wise.jpg")
    print("Topicwise acceptance rates ... Done!")

    # total accepted per prompt
    prompt_summary = all_data.groupby('prompt_id').agg(
    total_passed=pd.NamedAgg(column='Passed', aggfunc='sum'),
    total_failed=pd.NamedAgg(column='Failed', aggfunc='sum'),
    total_accepted=pd.NamedAgg(column='Accepted', aggfunc=lambda x: (x == 'Accepted').sum())
    ).reset_index()

    best_prompt = prompt_summary.loc[prompt_summary['total_passed'].idxmax()]
    worst_prompt = prompt_summary.loc[prompt_summary['total_failed'].idxmax()]
    best_accepted_prompt = prompt_summary.loc[prompt_summary['total_accepted'].idxmax()]
    worst_accepted_prompt = prompt_summary.loc[prompt_summary['total_accepted'].idxmin()]

    print(f"Best Prompt (Most Passes): Prompt ID {best_prompt['prompt_id']} with {best_prompt['total_passed']} passes.")
    print(f"Worst Prompt (Most Fails): Prompt ID {worst_prompt['prompt_id']} with {worst_prompt['total_failed']} fails.")
    print(f"Best Prompt (Most Accepted): Prompt ID {best_accepted_prompt['prompt_id']} with {best_accepted_prompt['total_accepted']} accepted solutions.")
    print(f"Worst Prompt (Least Accepted): Prompt ID {worst_accepted_prompt['prompt_id']} with {worst_accepted_prompt['total_accepted']} accepted solutions.")

    plt.figure(figsize=(12, 6))
    sns.barplot(x='prompt_id', y='total_accepted', data=prompt_summary, palette='viridis')
    plt.xlabel('Prompt ID')
    plt.ylabel('Total Accepted Solutions')
    plt.title('Total Number of Accepted Solutions Per Prompt')
    plt.xticks(rotation=45)
    plt.savefig(f"{root_path}/prompt_acceptance.jpg")
    print("Prompt based acceptance ... Done!")



def main():
    results_dir = r"results"
    datasets = []
    files = os.listdir(results_dir)
    for i, file in enumerate(files):
        df = pd.read_csv(os.path.join(results_dir, file)).assign(prompt_id=i+1)
        df['Accepted'] = df.apply(is_accepted, axis=1)
        datasets.append(df)

        save_files_path = os.path.join(r"results", str(i+1))
        get_charts(df, save_files_path)

    # Concatenate all datasets for analysis
    comparative_path = r"results"
    all_data = pd.concat(datasets, ignore_index=True)
    comparative_analysis(datasets, all_data, comparative_path)


if __name__ == "__main__":
    main()
    print("All set. Goodbye!")