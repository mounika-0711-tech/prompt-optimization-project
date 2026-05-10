import numpy as np

def analyze(results):
    analysis = {}

    for prompt, scores_list in results.items():
        flat_scores = []

        for answer_scores in scores_list:
            for item in answer_scores:
                # handle both formats safely
                if isinstance(item, tuple):
                    score = item[0]  # extract score from (score, reason)
                else:
                    score = item

                flat_scores.append(score)

        analysis[prompt] = {
            "mean": round(np.mean(flat_scores), 2),
            "variance": round(np.var(flat_scores), 2)
        }

    return analysis


def print_report(analysis):
    print("\n📊 FINAL REPORT\n")

    for prompt, data in analysis.items():
        print(f"{prompt}")
        print(f"Average Score: {data['mean']}")
        print(f"Variance: {data['variance']}")
        print("-" * 30)