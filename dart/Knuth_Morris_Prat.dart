// Due to dartpad cannt use package:test
void customizeTest(String notify, Object expection, Object actual) {
  bool r = expection.toString() == actual.toString();
  print("Result $notify: $r");
}

/// Preprocess pattern to identify any suffixes that are identical to prefixes
/// in the given string.
///
/// Build a pattern which tells us where to continue iteration from if we
///  get a mismatch between the character
///
/// Step through the text one character at a time and compare it to a character in
/// the pattern updating our location within the pattern if necessary
bool stringCompare(String string, String subString) {
  if (subString.isEmpty) {
    return false;
  }

  List<int> pattern = List<int>.generate(subString.length, (int index) => -1);

  int i = 1;
  int j = 0;

  while (i < subString.length) {
    if (subString[i] == subString[j]) {
      pattern[i] = j;
      i++;
      j++;
    } else if (j > 0) {
      j = pattern[j - 1] + 1;
    } else {
      i++;
    }
  }

  return stringCompareHelper(string, subString, pattern);
}

bool stringCompareHelper(String string, String subString, List<int> pattern) {
  int i = 0;
  int j = 0;

  while (i + subString.length - j <= string.length) {
    if (string[i] == subString[j]) {
      if (j == subString.length - 1) {
        return true;
      }
      i++;
      j++;
    } else if (j > 0) {
      j = pattern[j - 1] + 1;
    } else {
      i++;
    }
  }
  return false;
}

void main() {
  customizeTest("KMP: ",
      stringCompare('aefoaefcdaefcdaed', 'aefcdaed').toString(), 'true');
  customizeTest(
      "KMP: ",
      stringCompare(
              'testwafwafawfawfawfawfawfawfawfa', 'aefcfawfawfawfawfadaed')
          .toString(),
      'true');
  customizeTest("KMP: ",
      stringCompare('aefoaefcdaefcdaed', 'aefcdaed').toString(), 'aefcdaed');
}
