// Due to dartpad cannt use package:test
void customizeTest(String notify, Object expection, Object actual) {
  bool r = expection.toString() == actual.toString();
  print("Result $notify: $r");
}

// Reverse string Solution 1
String reverseString1(String str) {
  return str.split('').reversed.join();
}

// Reverse string Solution 2
String reverseString2(String str) {
  String reversed = "";
  for (int i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  return reversed;
}

void main() {
  String stringToReverse = "The Algorithms:Dart";
  print('Method 1 =>  $stringToReverse\t   ${reverseString1(stringToReverse)}');
  print('Method 2 =>  $stringToReverse\t   ${reverseString2(stringToReverse)}');
}
