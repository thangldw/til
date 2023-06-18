// Due to dartpad cannt use package:test
void customizeTest(String notify, Object expection, Object actual) {
  bool r = expection.toString() == actual.toString();
  print("Result $notify: $r");
}

bool magicNo(var x) {
  var result = x % 9;
  return result == 1;
}

void main() {
  customizeTest(
      "Test Magic_no returns false for non-magic numbers", magicNo(0), "false");
  customizeTest("Test Magic_no returns false for non-magic numbers",
      magicNo(371), "false");
  customizeTest("Test Magic_no returns false for non-magic numbers",
      magicNo(10), "false");
  customizeTest("Test Magic_no returns false for non-magic numbers",
      magicNo(370), "false");
}
