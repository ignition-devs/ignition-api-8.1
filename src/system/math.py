"""Math Functions.

The following functions assist with running statistical analysis.
"""

from __future__ import print_function

__all__ = [
    "geometricMean",
    "kurtosis",
    "max",
    "mean",
    "meanDifference",
    "median",
    "min",
    "mode",
    "normalize",
    "percentile",
    "populationVariance",
    "product",
    "skewness",
    "standardDeviation",
    "sum",
    "sumDifference",
    "sumLog",
    "sumSquares",
    "variance",
]

import __builtin__ as builtins

from typing import List, Union

from org.apache.commons.math3.exception import DimensionMismatchException


def geometricMean(values):
    # type: (List[Union[float, int]]) -> float
    """Calculates the geometric mean.

    Geometric Mean is a type of average which indicates a typical value
    in a set of numbers by using the product of values in the set.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The geometric mean, or NaN if the input was empty or null.
        Because this uses logs to compute the geometric mean, will
        return NaN if any entries are negative.
    """
    print(values)
    return float(43)


def kurtosis(values):
    # type: (List[Union[float, int]]) -> float
    """Calculates the kurtosis of a sequence of values.

    Kurtosis measures if data is peaked or flat relative to normal
    distribution. A set of data with high kurtosis will have distinct
    peaks near the mean, while a set of data with low kurtosis will have
    a flat top near the mean. Uniform distribution is typically a flat
    line.

    Returns NaN (Not a Number) if passed an empty sequence measure of
    whether the data are heavy-tailed or light-tailed of a given
    distribution.

    Args:
        values: A sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The kurtosis, or NaN if the input was empty or null.
        Additionally, returns NaN if the values returned fewer than 4
        values.
    """
    print(values)
    return float(43)


def max(values):
    # type: (List[Union[float, int]]) -> float
    """Given a sequence of values, returns the greatest value in the
    sequence, also known as the "max" value.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The maximum value contained in the values parameter, or NaN if
        the input was empty or null.
    """
    return builtins.max(values)


def mean(values):
    # type: (List[Union[float, int]]) -> float
    """Given a sequence of values, calculates the arithmetic mean
    (average).

    Returns NaN (Not a Number) if passed an empty sequence, a null.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The arithmetic mean, or NaN if the input was empty or None.
    """
    print(values)
    return float(43)


def meanDifference(values1, values2):
    # type: (List[Union[float, int]], List[Union[float, int]]) -> float
    """Given two sequences of values, calculates the mean of the signed
    difference between both sequences.

    In other words, returns the absolute difference between the mean
    values of two different sets of data.

    Args:
        values1: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.
        values2: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The mean difference, or NaN if one of the parameters was empty
        or null.

    Raises:
        DimensionMismatchException: If the two sequences have different
            lengths.
    """
    if len(values1) != len(values2):
        raise DimensionMismatchException()
    return float(43)


def median(values):
    # type: (List[Union[float, int]]) -> float
    """Takes a sequence of values, and returns the median.

    The Median represents the middle value in a set of data.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The median, or NaN if the input was empty or null.
    """
    print(values)
    return float(43)


def min(values):
    # type: (List[Union[float, int]]) -> float
    """Given a Sequence of numerical values, returns the minimum value,
    also known as the "min" value.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The minimum value contained within the values parameter, or NaN
        if the input was empty or null.
    """
    return builtins.min(values)


def mode(values):
    # type: (List[Union[float, int]]) -> List[float]
    """Given a sequence of values, returns the 'mode', or most frequent
    values.

    Returns an empty list if the sequence was empty or None.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.

    Returns:
        A Java Array (functionally similar to a Python List) of floats
        representing the most frequent values in the values parameter.
        If the values parameter was empty, then an empty list will be
        returned instead.
    """
    print(values)
    return [float(43)]


def normalize(values):
    # type: (List[Union[float, int]]) -> List[float]
    """Given a sequence of values, normalizes the values.

    Normalizing data refers to adjusting values measured on different
    scales and brings them into alignment to allow the comparison of
    corresponding normalized values. This creates uniformity of values
    by eliminating the different units of measurement, and to more
    easily compare data from different places

    Returns an empty list if the sequence was empty or None.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.

    Returns:
        A Java Array (functionally similar to a Python List) of floats
        representing normalized input, with a mean of 0 and a standard
        deviation of 1. Returns an empty array if the input was empty or
        None. If the standard deviation is 0, will return an array of
        float NaN (Not a Number).
    """
    print(values)
    return [float(43)]


def percentile(values, percentile):
    # type: (List[Union[float, int]], float) -> float
    """Given a sequence of numerical values, estimates the percentile of
    input.

    The percentile is a value on a scale that represents a percentage
    position in a list of data that can be equal to or below that value:
    i.e., the 25th percentile is a value below which 25% of observable
    data points may be found.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.
        percentile: The percentile to compute. A float greater than 0
            and less than or equal to 100. Will throw an exception if
            the percentile is out of bounds.

    Returns:
        An estimate of the requested percentile of the input, or NaN if
        the input was empty or null.
    """
    print(values, percentile)
    if 0 > percentile > 100:
        raise ValueError("percentile out of bounds.")
    return float(43)


def populationVariance(values):
    # type: (List[Union[float, int]]) -> float
    """Given a sequence of values, returns the Population Variance.

    Population variance calculates how values in a dataset are spread
    out from their average value.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The population variance, or NaN if the input was empty or null.
    """
    print(values)
    return float(43)


def product(values):
    # type: (List[Union[float, int]]) -> float
    """Given a sequence of values, calculates the product of the
    sequence: the result of multiplying of all values in the sequence
    together.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The product of all values in the values parameter, or NaN if the
        input was empty or null.
    """
    print(values)
    return float(43)


def skewness(values):
    # type: (List[Union[float, int]]) -> float
    """Calculates the skewness given a sequence of values.

    Skewness is a measure of the degree of asymmetry of a distribution
    of the mean. If skewed to the left, the distribution has a long tail
    in the negative direction. If skewed to the right, the tail will be
    skewed in the positive direction.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The skewness of the values parameter, or NaN if values was empty
        or null.
    """
    print(values)
    return float(43)


def standardDeviation(values):
    # type: (List[Union[float, int]]) -> float
    """Given a Sequence of numerical values, calculates the standard
    deviation.

    Standard deviation is a calculated number for how close, or how far
    the values of that dataset are in relation to the mean.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The standard deviation of the values parameter, or NaN if the
        values was empty or null.
    """
    print(values)
    return float(43)


def sum(values):
    # type: (List[Union[float, int]]) -> float
    """Given a sequence of values, calculates the sum of all values.

    The sum is the number returned by addition.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The sum of all values in the values parameter, or NaN if values
        was empty or null.
    """
    return builtins.sum(values)


def sumDifference(values1, values2):
    # type: (List[Union[float, int]], List[Union[float, int]]) -> float
    """Given two sequences of values, calculates the sum of the signed
    difference between both sequences.

    In other words, the sum and difference between two sets of numbers.

    Args:
        values1: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.
        values2: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The sum difference, or NaN if one of the parameters was empty or
        null.

    Raises:
        DimensionMismatchException: If the two sequences have different
            lengths.
    """
    if len(values1) != len(values2):
        raise DimensionMismatchException()
    return float(43)


def sumLog(values):
    # type: (List[Union[float, int]]) -> float
    """Given a sequence of values, calculates the sum of the natural
    logs.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The sum of the natural logs of the input values, or NaN if the
        input was empty, None, or contains negative numbers.
    """
    print(values)
    return float(43)


def sumSquares(values):
    # type: (List[Union[float, int]]) -> float
    """Given a sequence of values, calculates the sum of the squares of
    all values.

    Sum squares measures how far individual values are from the mean by
    calculating how much variation there is in a set of values.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The sum of all squares of the values parameter, or NaN if the
        input was empty or null.
    """
    return builtins.sum(value**2 for value in values)


def variance(values):
    # type: (List[Union[float, int]]) -> float
    """Given a sequence of values, calculates the variance of all
    values.

    Variance measures how far values in a set are spread out from their
    mean value.

    Returns NaN (Not a Number) if passed an empty sequence.

    Args:
        values: A Sequence of numerical values. Accepts both Integers
            and Floats. The sequence may not contain None type values.
            However, passing a None type object instead of a Sequence of
            numerical values will return NaN.

    Returns:
        The variance of all values in the values parameter, or NaN if
        the input was empty or null.
    """
    print(values)
    return float(43)
