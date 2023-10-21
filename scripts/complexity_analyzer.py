import subprocess

class ComplexityAnalyzer:

    @staticmethod
    def get_cyclomatic_complexity():
        result = subprocess.run(['lizard', '-x', './venv/*'], stdout=subprocess.PIPE, text=True)
        output = result.stdout.splitlines()

        complexities = {}

        for line in output[3:]:
            data = line.split()
            if len(data) == 6:
                file_location = data[-1]
                file_name = file_location.split('@')[-1].replace('\\', '/').lstrip('./')
                ccn = data[1]
                if ccn.isdigit():
                    complexities[file_name] = ccn
                

        return complexities
if(__name__ == '__main__'):
    complexities = ComplexityAnalyzer.get_cyclomatic_complexity()
    for file_name, ccn in complexities.items():
        print(f'Archivo: {file_name}, CCN: {ccn}')