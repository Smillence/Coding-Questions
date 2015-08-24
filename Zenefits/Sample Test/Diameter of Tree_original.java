/* Write your custom functions here */
static int diameterOfTree(Node root) {
/* For your reference
   class Node {
       Node left, right;
       int data;
               Node(int newData) {
           left = right = null;
           data = newData;
       }
   }
*/     
    if (root==null) {
        return 0;
    }
    Node L = root.left;
    Node R = root.right;
    int l = heightOfTree(L);
    int r = heightOfTree(R);
    int c3 = l+r+1;
    int c1 = diameterOfTree(L);
    int c2 = diameterOfTree(R);
    return Math.max(c1,Math.max(c2,c3));
}

static int heightOfTree(Node root) {
    if (root==null) {
        return 0;
    }
    Node L = root.left;
    Node R = root.right;
    int l = heightOfTree(L);
    int r = heightOfTree(R);
    return Math.max(l+1,r+1);
 
}