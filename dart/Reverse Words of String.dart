// Due to dartpad cannt use package:test
void customizeTest(String notify, Object expection, Object actual) {
  bool r = expection.toString() == actual.toString();
  print("Result $notify: $r");
}

String reverseStringWords(String s) {
  String res = "";
  int m = s.length;
  int j = m - 1;
  for (int i = m - 1; i >= 0; i--) {
    if (s[i] == '.') {
      for (int j1 = i + 1; j1 <= j; j1++) {
        res += s[j1];
      }
      res += s[i];
      j = i - 1;
    } else if (i == 0) {
      for (int j1 = i; j1 <= j; j1++) {
        res += s[j1];
      }
    }
  }
  return res;
}

void main() {
  customizeTest(
      'test: ',
      reverseStringWords("reverseStringWords single word returns same word"),
      'word');
  customizeTest('test: ',
      reverseStringWords("reverseStringWords w1.w2 returns w2.w1"), 'w2.w1');
  customizeTest('test: ', reverseStringWords("boy.good.a.is.abhishek"),
      'abhishek.is.a.good.boy');
}
