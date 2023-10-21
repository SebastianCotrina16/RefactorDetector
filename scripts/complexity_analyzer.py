import subprocess

class ComplexityAnalyzer:

    @staticmethod
    def get_cyclomatic_complexity():
        result = subprocess.run(['radon', 'cc', '-s', '-a', 'scripts/analyze.py'], stdout=subprocess.PIPE)
        output = result.stdout.splitlines()

        complexities = {}

        for line in output[1:]:
            data = line.split(',')
            file_name = data[1]
            complexity = int(data[9])
            complexities[file_name] = complexity
        
        return complexities