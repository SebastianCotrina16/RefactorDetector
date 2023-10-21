import subprocess

class ChurnCalculator:

    @staticmethod
    def get_churn():
        result = subprocess.run(["git", "log", "--numstat", "--pretty=\"%H\""], capture_output=True, text=True)
        output = result.stdout.splitlines()

        churn = {}

        for line in output:
            if not line.startswith('"'):
                parts = line.split('\t')
                if len(parts) >= 3:
                    additions, deletions, file_name = parts
                    print(parts)
                    churn[file_name] = churn.get(file_name, 0) + int(additions) + int(deletions)
                
        return churn
if __name__ == '__main__':
    churn = ChurnCalculator.get_churn()
    for file_name, churn_value in churn.items():
        print(f'Archivo: {file_name}, Churn: {churn_value}')