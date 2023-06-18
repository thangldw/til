void customizeTest(String notify, Object expection, Object actual) {
  bool r = expection.toString() == actual.toString();
  print("Result $notify: $r");
}

void pigeonholeSort(List arr) {
  //The length of the list
  int n = arr.length;

  //checking the size
  if (n <= 0) {
    return;
  }

  //Find minimum and maximum values in arr
  int min = arr[0];
  int max = arr[0];

  for (int i = 1; i < n; i++) {
    if (arr[i] < min) min = arr[i];
    if (arr[i] > max) max = arr[i];
  }

  int range = max - min;
  range++;

  var phole = List.filled(range, 0);
  for (int i = 0; i < range; i++) {
    phole[i] = 0;
  }

  //Populate the pigeonholes.
  for (int i = 0; i < n; i++) {
    phole[arr[i] - min];
    phole[arr[i] - min] = phole[arr[i] - min] + 1;
  }

  //Put the elements back into the array in order
  int index = 0;

  for (int j = 0; j < range; j++) while (phole[j]-- > 0) arr[index++] = j + min;
}

void main() {
  List list = [87, 48, 5, 7, 135, 85];
  List backup_list = [5, 7, 48, 85, 87, 135];
  pigeonholeSort(list);

  customizeTest("Sort : ", list, backup_list);
}
