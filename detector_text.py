def simple_detector(text):
    """
    Dummy detector logic.
    Flags text based on presence of certain patterns.
    (Simulates behaviour, not a real AI model.)
    """
    keywords = ["buy now", "click here", "limited offer"]

    text_lower = text.lower()

    for word in keywords:
        if word in text_lower:
            return "Flagged"

    return "Not Flagged"


def run_experiment():
    original = "Buy now and get a limited offer"
    rephrased_versions = [
        "Purchase today to receive a special deal",
        "Click here for an exclusive discount",
        "Grab this opportunity before it ends"
    ]

    print("Original Text:")
    print(original)
    print("Detector Output:", simple_detector(original))

    print("\nRephrased Versions:")
    for text in rephrased_versions:
        print(text)
        print("Detector Output:", simple_detector(text))
        print("-" * 40)


if __name__ == "__main__":
    run_experiment()
