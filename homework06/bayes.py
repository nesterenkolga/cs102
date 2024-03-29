import math
import typing as tp
from collections import defaultdict


class NaiveBayesClassifier:
    def __init__(self, alpha: float = 1.0) -> None:
        self.alpha = alpha
        self._class_freq: tp.Dict[str, float] = defaultdict(lambda: 0.0)
        self._separated_words_in_class: tp.Dict[tp.Tuple[str, str], int] = defaultdict(lambda: 0)
        self._words_in_class: tp.Dict[str, int] = defaultdict(lambda: 0)
        self._word_set: tp.Set[str] = set()

    def fit(self, X: tp.List[str], y: tp.List[str]) -> None:
        """ Fit Naive Bayes classifier according to X, y. """
        for feature, label in zip(X, y):
            self._class_freq[label] += 1
            for value in feature.split():
                self._separated_words_in_class[(value, label)] += 1
                self._words_in_class[label] += 1
                self._word_set.add(value)

        num_samples = len(X)
        for k in self._class_freq:
            self._class_freq[k] /= num_samples

    def predict(self, X: tp.List[str]) -> tp.List[str]:
        """ Perform classification on an array of test vectors X. """
        result = []
        for x in X:
            result.append(
                max(self._class_freq.keys(), key=lambda c: self.__calculate_class_freq(x, c))
            )
        return result

    def __calculate_class_freq(self, X: str, clss: str) -> float:
        """ Calculate frequency for current class """
        freq = math.log(self._class_freq[clss])

        for feat in X.split():
            freq += math.log(
                (self._separated_words_in_class[feat, clss] + self.alpha)
                / (self._words_in_class[clss] + self.alpha * len(self._word_set))
            )
        return freq

    def score(self, X_test: tp.List[str], y_test: tp.List[str]) -> float:
        """ Returns the mean accuracy on the given test data and labels. """
        results = self.predict(X_test)
        return sum(y_test[x] == results[x] for x in range(len(y_test))) / len(y_test)