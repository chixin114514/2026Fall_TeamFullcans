#include "random_vector.h"
#include <cstdlib>

RandomVector::RandomVector(int size, double max_val) {
  if (size < 0) {
    size = 0;
  }
  if (max_val < 0) {
    max_val = 0;
  }

  vect.resize(static_cast<std::size_t>(size));
  for (std::size_t i = 0; i < vect.size(); ++i) {
    vect[i] = (static_cast<double>(std::rand()) / RAND_MAX) * max_val;
  }
}

void RandomVector::print() {
  for (std::size_t i = 0; i < vect.size(); ++i) {
    if (i != 0) {
      std::cout << ' ';
    }
    std::cout << vect[i];
  }
  std::cout << std::endl;
}

double RandomVector::mean() {
  if (vect.empty()) {
    return 0.0;
  }

  double sum = 0.0;
  for (std::size_t i = 0; i < vect.size(); ++i) {
    sum += vect[i];
  }
  return sum / static_cast<double>(vect.size());
}

double RandomVector::max() {
  if (vect.empty()) {
    return 0.0;
  }

  double result = vect[0];
  for (std::size_t i = 1; i < vect.size(); ++i) {
    if (vect[i] > result) {
      result = vect[i];
    }
  }
  return result;
}

double RandomVector::min() {
  if (vect.empty()) {
    return 0.0;
  }

  double result = vect[0];
  for (std::size_t i = 1; i < vect.size(); ++i) {
    if (vect[i] < result) {
      result = vect[i];
    }
  }
  return result;
}

void RandomVector::printHistogram(int bins) {
  if (bins <= 0 || vect.empty()) {
    return;
  }

  std::vector<int> counts(static_cast<std::size_t>(bins), 0);
  const double lower = min();
  const double upper = max();

  if (lower == upper) {
    counts[static_cast<std::size_t>(bins - 1)] =
        static_cast<int>(vect.size());
  } else {
    const double width = upper - lower;
    for (std::size_t i = 0; i < vect.size(); ++i) {
      int index = static_cast<int>(((vect[i] - lower) / width) * bins);
      if (index < 0) {
        index = 0;
      } else if (index >= bins) {
        index = bins - 1;
      }
      ++counts[static_cast<std::size_t>(index)];
    }
  }

  int tallest = counts[0];
  for (int i = 1; i < bins; ++i) {
    if (counts[static_cast<std::size_t>(i)] > tallest) {
      tallest = counts[static_cast<std::size_t>(i)];
    }
  }

  for (int level = tallest; level > 0; --level) {
    for (int i = 0; i < bins; ++i) {
      std::cout << (counts[static_cast<std::size_t>(i)] >= level ? "***" : "   ");
      if (i + 1 < bins) {
        std::cout << ' ';
      }
    }
    std::cout << std::endl;
  }
}
