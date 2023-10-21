import subprocess

class ChurnCalculator:

    @staticmethod
    def get_churn():
        result = subprocess.run(["git", "log", "--numstat", "--pretty=\"%H\""], capture_output=True, text=True, cwd='/project/')
        output = result.stdout.splitlines()

        churn = {}

        for line in output:
            if not line.startswith('"') and "complexity_vs_churn.png" not in line:
                parts = line.split('\t')
                if len(parts) >= 3:
                    additions, deletions, file_name = parts
                    if(additions == '-'):
                        additions = 0
                    if(deletions == '-'):
                        deletions = 0
                    churn[file_name] = churn.get(file_name, 0) + int(additions) + int(deletions)
        for(key,value) in churn.items():
            print(key,' Churn: ',value)
        return churn