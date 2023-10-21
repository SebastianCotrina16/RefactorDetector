import matplotlib.pyplot as plt

from complexity_analyzer import ComplexityAnalyzer
from churn_calculator import ChurnCalculator

class Analyzer:

    @staticmethod
    def plot_graph(complexities, churn):
        files = list(complexities.keys())
        x = [churn[file] for file in files]
        y = [complexities[file] for file in files]

        plt.scatter(x, y)
        plt.xlabel('Churn (# Commits for each file)')
        plt.ylabel('Cyclomatic Complexity')
        plt.title('Churn vs Cyclomatic Complexity')
        plt.savefig('complexity_vs_churn.png')

if __name__ == '__main__':
    complexities = ComplexityAnalyzer.get_cyclomatic_complexity()
    churn = ChurnCalculator.get_churn()
    Analyzer.plot_graph(complexities, churn)