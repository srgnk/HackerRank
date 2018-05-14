/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */


int max(int a, int b) {
    return (a > b) ? a : b;
}

int get_height(node *root) {
    if (!root) 
        return -1;
    else 
        return root->ht;
}

int set_height(node *root) {
    if (!root)
        return -1;
    else 
        return 1 + max(get_height(root->left), get_height(root->right));
}

int get_balance_factor(node *root) {
    return get_height(root->left) - get_height(root->right);
}

void print_tree(node *root) {
    if (!root)
        return;
    else {
        print_tree(root->left);
        printf("val = %d ht = %d bf = %d\n", root->val, root->ht, get_balance_factor(root));
        print_tree(root->right);
    }
}

node *rotate_right(node *root) {
    node *new_root = root->left;
    root->left = new_root->right;
    new_root->right = root;
    
    root->ht = set_height(root);
    new_root->ht = set_height(new_root);
    
    return new_root;
}

node *rotate_left(node *root) {
    node *new_root = root->right;
    root->right = new_root->left;
    new_root->left = root;
    
    root->ht = set_height(root);
    new_root->ht = set_height(new_root);
    
    return new_root;
}

node *new_node(int val) {
	node *nd = (struct node *) calloc(1, sizeof(struct node));
    nd->val = val;
    nd->left = NULL;
    nd->right = NULL;
    nd->ht = set_height(nd);
    
	return nd;
}

node *insert(node *root, int value) {
    if (!root)
        return new_node(value);
    
    // search for place to add new element
    if (value > root->val)
        root->right = insert(root->right, value);
    else
        root->left = insert(root->left, value);

    int bf = get_balance_factor(root);
    //printf("root = %d ht = %d BF = %d\n", root->val, root->ht, bf);

    if (bf > 1) {
        if (get_height(root->left->left) >= get_height(root->left->right)) {
            root = rotate_right(root);
        } else {
            root->left = rotate_left(root->left);
            root = rotate_right(root);
        }
    } else if (bf < -1) {
        if (get_height(root->right->right) >= get_height(root->right->left)) {
            root = rotate_left(root);
        } else {
            root->right = rotate_right(root->right);
            root = rotate_left(root);
        }
    } else {
        root->ht = set_height(root);
    }
    
    //print_tree(root);
    //printf("\n");
    return root;
}