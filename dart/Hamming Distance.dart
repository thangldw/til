// Due to dartpad cannt use package:test
void customizeTest(String notify, Object expection, Object actual) {
  bool r = expection.toString() == actual.toString();
  print("Result $notify: $r");
}

int hammingDistance(String stringA, String stringB) {
  //Calculates Hamming Distance
  int distance;

  //strings must be of equal length
  if (stringA.length != stringB.length) {
    print('String lengths must be same!');
    return -1;
  } else {
    distance = 0;
    for (var i = 0; i < stringA.length; i++) {
      if (stringA[i] != stringB[i]) {
        distance += 1;
      }
    }
  }
  return distance;
}

void main() {
  String stringA;
  String stringB;
  int dist;

  stringA = 'karolin';
  stringB = 'kathrin';
  dist = hammingDistance(stringA, stringB);
  print('Hamming Distance between $stringA and $stringB is $dist');

  stringA = '1011101';
  stringB = '1001001';
  dist = hammingDistance(stringA, stringB);
  print('Hamming Distance between $stringA and $stringB is $dist');
}
