class Solution {
  int reverse(int x) {

    int reverse = 0;

  int sign = x < 0 ? -1 : 1;
  x = x.abs();

  while (x != 0) {
    int num = x % 10;
    x ~/= 10;

    if (reverse > 214748364 || (reverse == 214748364 && num > 7)) {
      return 0;
    }

    if (reverse < -214748364 || (reverse == -214748364 && num < -8)) {
      return 0;
    }

    reverse = reverse * 10 + num;
  }

  return reverse*sign;

  }
}