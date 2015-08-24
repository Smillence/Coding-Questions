static int diameterOfTree(Node root) {
  return diameterOfTreeHelper(root).diameter;
}

static Pair diameterOfTreeHelper(Node root) {
  if (root == null) {
    return new Pair(0,0);
  }
  Node L = root.left;
  Node R = root.right;
  Pair LP = diameterOfTreeHelper(L);
  Pair RP = diameterOfTreeHelper(R);
  int height = Math.max(LP.height+1, RP.height+1);
  int candidate3 = LP.height + RP.height + 1;
  int diameter = Math.max(candidate3, Math.max(LP.diameter, RP.diameter));
  return new Pair(height, diameter);
}

private static class Pair {
  int height, diameter;
  Pair(int h, int d) {
    height = h;
    diameter = d;
  }
}