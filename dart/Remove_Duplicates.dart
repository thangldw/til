// Due to dartpad cannt use package:test
void customizeTest(String notify, Object expection, Object actual) {
  bool r = expection.toString() == actual.toString();
  print("Result $notify: $r");
}

//function to remove dupplicate in string
String removeDup(String s) {
  var arr = new List.filled(256, 0);
  String l = '';
  int i = 0;

  for (i = 0; i < s.length; i++) {
    if (arr[s.codeUnitAt(i)] == 0) {
      l += s[i];
      arr[s.codeUnitAt(i)]++;
    }
  }
  return l;
}

void main() {
  customizeTest("test 1", removeDup("aaaab"), "ab");
}
