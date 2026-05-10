from prompts import PROMPT_A, PROMPT_B, PROMPT_C
from evaluator import evaluate

PROMPTS = {
    "1": ("Prompt A (Basic)", PROMPT_A),
    "2": ("Prompt B (Structured)", PROMPT_B),
    "3": ("Prompt C (Strict)", PROMPT_C),
}


def main():
    print("\n=== Prompt Optimization Evaluator ===\n")

    while True:

        # user input
        user_answer = input("Enter your answer: ")

        print("\nChoose Prompt Type:")
        print("1. Basic")
        print("2. Structured")
        print("3. Strict")

        choice = input("\nYour choice: ")

        if choice not in PROMPTS:
            print("\nInvalid choice.\n")
            continue

        prompt_name, prompt_type = PROMPTS[choice]

        print(f"\n🔹 Running {prompt_name}\n")

        results = evaluate(prompt_type, user_answer)

        print("Evaluation Results:\n")

        scores_only = []

        for i, (score, reason) in enumerate(results, start=1):
            print(f"Run {i} -> Score: {score} | Reason: {reason}")
            scores_only.append(score)

        # variance calculation
        avg = sum(scores_only) / len(scores_only)
        variance = sum((x - avg) ** 2 for x in scores_only) / len(scores_only)

        print(f"\nAverage Score: {round(avg, 2)}")
        print(f"Variance: {round(variance, 2)}")

        # continue?
        again = input("\nDo you want to test another answer? (y/n): ")

        if again.lower() != "y":
            print("\nExiting Evaluator...")
            break


if __name__ == "__main__":
    main()