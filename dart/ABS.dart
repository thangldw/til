abs_value(num) {
  return num < 0 ? -num : num;
}

void main() {
  print(abs_value(23));
  print(abs_value(-23));
}
