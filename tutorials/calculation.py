def get_average_scores(scores):
    """
    Calculates the average score of all candidates
    Args:
        scores: A list of scores.
    Returns:
        The average of the scores.
    """

    total_score = sum(scores)

    number_of_scores = len(scores)

    return total_score / number_of_scores


def add(scores):
    """
    Sum all scores of all candidates
    Args:
        scores: A list of scores.
    Returns:
        The total score.
    """
    total_score = sum(scores)

    return total_score


if __name__ == "__main__":
    scores = []
    candidate = int(
        input("Number of candidates: ")
    )  # Ask the user to input the number of candidates
    for i in range(candidate):
        while True:
            score = int(
                input("Score: ")
            )  # Ask the user to input the score of each candidate
            if 100 <= score <= 999:
                scores.append(score)
                break  # Exit the loop if the score is valid
            else:
                print("Score must be in the range of 100 and 999")

    # Call function get_average_scores() to calculate the average score of all candidates
    average_score = get_average_scores(scores)
    total_score = add(scores)

    # Print the average score of all candidates
    print(f"Average score: {average_score:1.2f}")
    print(f"Total scores: {total_score}")
