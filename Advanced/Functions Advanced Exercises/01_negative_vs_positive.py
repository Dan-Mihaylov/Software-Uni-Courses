def negative_vs_positive(numbers):
    positives = 0
    negatives = 0
    for num in numbers:
        if num >= 0:
            positives += num
        else:
            negatives += num
    stronger = ""

    if abs(positives) > abs(negatives):
        stronger = "The positives are stronger than the negatives"
    else:
        stronger = "The negatives are stronger than the positives"

    return f"{negatives}\n{positives}\n{stronger}"


nums = [int(x) for x in input().split()]
print(negative_vs_positive(nums))
