import matplotlib.pyplot as plt

from adjustText import adjust_text
from complexity_analyzer import ComplexityAnalyzer
from churn_calculator import ChurnCalculator

class Analyzer:

    @staticmethod
    def plot_graph(complexities, churn):
        files = [file for file in complexities if file in churn]
        x = [churn[file] for file in files]
        y = [complexities[file] for file in files]

        plt.figure(figsize=(12, 8))

        plt.scatter(x, y,alpha=0.6,edgecolors='w',linewidths=0.5)

        plt.xlabel('Churn (# Commits for each file)')
        plt.ylabel('Cyclomatic Complexity')
        plt.title('Churn vs Cyclomatic Complexity')

        texts = [plt.text(churn_value, complexity, file, ha='center', va='center') for file, churn_value, complexity in zip(files, x, y)]
        
        adjust_text(texts)

        plt.savefig('complexity_vs_churn.png')

if __name__ == '__main__':
    complexities = ComplexityAnalyzer.get_cyclomatic_complexity()
    churn = ChurnCalculator.get_churn()
    Analyzer.plot_graph(complexities, churn)